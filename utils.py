#!/usr/bin/python3.6
from datetime import datetime, timedelta
import logging
from operator import itemgetter
import math
import random

from pytz import timezone
import requests

from config import scores, settings


def available_cash_getter(headers, account_number):
    url = url_builder('account_details', account_number)
    r = requests.get(url, headers=headers)
    response = r.json()
    available_cash = response['availableCash']
    return available_cash


def build_acceptable_loan(loan, scored_results):
    acceptable_loan = {}
    acceptable_loan['id'] = loan['id']
    acceptable_loan['term'] = loan['term']
    acceptable_loan['grade'] = loan['grade']
    acceptable_loan['score'] = round(scored_results['score'], 4)
    acceptable_loan['max_investment_amount'] = \
        scored_results['max_investment_amount']
    acceptable_loan['min_probability_score'] = \
        scored_results['min_probability_score']
    return acceptable_loan


def get_account_to_monitor(account_number):
    for account in settings.ACCOUNT_WATCHER:
        if account['account_number'] == account_number:
            return account['account_to_monitor']


def get_account_watcher_auth_token(account_number):
    for account in settings.ACCOUNT_WATCHER:
        if account['account_number'] == account_number:
            return account['authorization_token']


def get_all_loans(headers, logger):
    url = url_builder('get_loans')
    try:
        r = requests.get(url, headers=headers)
    except Exception as e:
        logger.error("Getting all loans: {}".format(e))
        return []
    response = r.json()
    loans = response.get('loans', None)
    logger.info("Total loans located: {}".format(len(loans)))
    return loans


def get_investment_amount(loan, available_cash):
    results = 0
    if available_cash < 25:
        return results
    score = loan['score']
    min_probability_score = loan['min_probability_score']
    max_investment_amount = loan['max_investment_amount']
    if score >= min_probability_score:
        if available_cash >= max_investment_amount:
            return max_investment_amount
        else:
            return available_cash
    else:
        return results


def get_loans(headers, logger):
    results = []
    scored_loans = []
    loans = get_all_loans(headers, logger)
    for loan in loans:
        if loan['grade'] in settings.LOAN_GRADES:
            scored_results = loan_scorer(loan)
            if scored_results['score'] >= scored_results['min_probability_score']: # noqa
                acceptable_loan = build_acceptable_loan(loan, scored_results)
                scored_loans.append(acceptable_loan)
    if scored_loans:
        results = sorted(
            scored_loans,
            key=itemgetter('grade', 'score'),
            reverse=True
        )
    return results


def get_loans_owned(headers, account_number):
    results = []
    url = url_builder('loans_owned', account_number)
    r = requests.get(url, headers=headers)
    response = r.json()
    notes = response.get('myNotes', [])
    for note in notes:
        results.append(note['loanId'])
    return results


def get_matching_loan(headers, grade, term, loans_owned, logger):
    scored_loans = []
    loans = get_all_loans(headers, logger)
    for loan in loans:
        if loan['grade'] == grade and loan['term'] == term:
            scored_results = loan_scorer(loan)
            loan_score = scored_results.get('score', 0)
            if loan_score >= .1 and loan_score <= .7:
                acceptable_loan = build_acceptable_loan(loan, scored_results)
                scored_loans.append(acceptable_loan)
    results = [l for l in scored_loans if l['id'] not in loans_owned]
    if results:
        return random.choice(results)
    else:
        return None


def get_monitoring_auth_token(account_number):
    for account in settings.ACCOUNTS:
        if account['account_number'] == account_number:
            return account['authorization_token']


def get_seconds_to_sleep():
    now = datetime.now()
    top_hour = now.replace(
        hour=now.hour,
        minute=59,
        second=59,
        microsecond=500
    )
    return (top_hour - now).seconds


def get_recent_loans(headers, account_number, minutes_since_loan):
    results = []
    pacific_time = datetime.now(timezone('US/Pacific'))
    watch_time = pacific_time - timedelta(minutes=minutes_since_loan)
    url = url_builder('loans_owned', account_number)
    r = requests.get(url, headers=headers)
    response = r.json()
    notes = response.get('myNotes', [])
    for note in notes:
        order_date = ''.join(note.get('orderDate', None).rsplit(':', 1))
        order_date = datetime.strptime(order_date, "%Y-%m-%dT%H:%M:%S.%f%z")
        if order_date >= watch_time:
            results.append(
                {
                    'loanId': note.get('loanId', None),
                    'grade': note.get('grade', None),
                    'term': note.get('loanLength', None),
                    'orderDate': note.get('orderDate', None),
                    'noteAmount': note.get('noteAmount', None),
                }
            )
    return results


def header_builder(authorization_token):
    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['Authorization'] = authorization_token
    headers['Accept'] = 'application/json'
    return headers


def loan_scorer(loan_details):
    results = {}
    score_identifier = loan_details['grade'] + '_' + str(loan_details['term'])
    score_model = scores.SCORES[score_identifier]
    score = score_model['base']
    home_ownership_score = score_model['home_ownership_scores'].get(
        loan_details['homeOwnership'], 0
    )
    verification_score = score_model['verification_scores'].get(
        loan_details['isIncV'], 0
    )
    for k in score_model['loan_attribute_weights']:
        score += loan_details[k] * score_model['loan_attribute_weights'].get(
            k, 0
        )
    score += home_ownership_score
    score += verification_score
    results['score'] = 1 / (1 + math.exp(score))
    results['min_probability_score'] = score_model['min_probability_score']
    results['max_investment_amount'] = score_model['max_investment_amount']
    if loan_details['homeOwnership'] not in list(score_model['home_ownership_scores']): # noqa
        results['score'] = 0
    return results


def order_placer(headers, account_number, payload):
    url = url_builder('place_order', account_number)
    r = requests.post(url, headers=headers, json=payload)
    response = r.json()
    return response


def setup_logger(logger_name, log_file_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file_name)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def url_builder(url_type, account_number=None):
    if url_type == 'account_details':
        url = settings.GET_ACCOUNT_DETAILS_URL.format(
            settings.CURRENT_VERSION,
            account_number
        )
    elif url_type == 'get_loans':
        url = settings.GET_LOAN_URL.format(settings.CURRENT_VERSION)
    elif url_type == 'loans_owned':
        url = settings.GET_LOANS_OWNED_URL.format(
            settings.CURRENT_VERSION,
            account_number
        )
    elif url_type == 'place_order':
        url = settings.PLACE_ORDER_URL.format(
            settings.CURRENT_VERSION,
            account_number
        )
    else:
        url = None
    return url
