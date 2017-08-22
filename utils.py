#!/usr/bin/python3.6
import datetime
import logging
from operator import itemgetter
import math

import requests

from config import scores, settings


def available_cash_getter(headers, account_number):
    url = url_builder('account_details', account_number)
    r = requests.get(url, headers=headers)
    response = r.json()
    available_cash = response['availableCash']
    return available_cash


def get_investment_amount(loan, available_cash):
    results = 0
    if available_cash < 50:
        return results
    score = loan['score']
    min_probability_score = loan['min_probability_score']
    max_investment_amount = loan['max_investment_amount']
    if loan['grade'] in ['F', 'G']:
        if score < min_probability_score:
            return results
        if score >= min_probability_score and score < .80:
            return 50
        if score >= .80 and score < .90:
            if available_cash >= 100:
                return 100
            else:
                return available_cash
        if score >= .90:
            if available_cash >= 150:
                return 150
            else:
                return available_cash
    else:
        if score >= min_probability_score:
            if available_cash >= max_investment_amount:
                return max_investment_amount
            else:
                return available_cash
        else:
            return results
    return results


def get_loans(headers, logger):
    results = []
    scored_loans = []
    url = url_builder('get_loans')
    r = requests.get(url, headers=headers)
    response = r.json()
    loans = response['loans']
    logger.info("Total loans located: {}".format(len(loans)))
    for loan in loans:
        if loan['grade'] in settings.LOAN_GRADES:
            scored_results = loan_scorer(loan)
            if scored_results['score'] >= scored_results['min_probability_score']: # noqa
                acceptable_loan = {}
                acceptable_loan['id'] = loan['id']
                acceptable_loan['term'] = loan['term']
                acceptable_loan['grade'] = loan['grade']
                acceptable_loan['score'] = round(scored_results['score'], 4)
                acceptable_loan['max_investment_amount'] = \
                    scored_results['max_investment_amount']
                acceptable_loan['min_probability_score'] = \
                    scored_results['min_probability_score']
                scored_loans.append(acceptable_loan)
    if scored_loans:
        results = sorted(
            scored_loans,
            key=itemgetter('grade', 'score'),
            reverse=True
        )
    return results


def get_seconds_to_sleep():
    now = datetime.datetime.now()
    top_hour = now.replace(
        hour=now.hour,
        minute=59,
        second=57,
        microsecond=250
    )
    return (top_hour - now).seconds


def get_loans_owned(headers, account_number):
    results = []
    url = url_builder('loans_owned', account_number)
    r = requests.get(url, headers=headers)
    response = r.json()
    notes = response.get('myNotes', [])
    for note in notes:
        results.append(note['loanId'])
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
