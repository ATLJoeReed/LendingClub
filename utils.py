#!/usr/bin/python3
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


def get_loans(headers, loan_grade, min_probability_score, logger):
    scored_loans = []
    url = url_builder('get_loans')
    r = requests.get(url, headers=headers)
    response = r.json()
    loans = response['loans']

    logger.info("Total loans located: {}".format(len(loans)))

    for loan in loans:
        if loan['grade'] in loan_grade:
            score = loan_scorer(loan)
            if score >= min_probability_score:
                acceptable_loan = {}
                acceptable_loan['id'] = loan['id']
                acceptable_loan['term'] = loan['term']
                acceptable_loan['grade'] = loan['grade']
                acceptable_loan['score'] = round(score, 4)
                scored_loans.append(acceptable_loan)
    if scored_loans:
        results = sorted(
            scored_loans,
            key=itemgetter('score'),
            reverse=True
        )

    return results


def header_builder(authorization_token):
    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['Authorization'] = authorization_token
    headers['Accept'] = 'application/json'
    return headers


def loan_scorer(loan_details):
    score = scores.BASE
    home_ownership_score = scores.HOME_OWNERSHIP_SCORES.get(
        loan_details['homeOwnership'], 0
    )
    verification_score = scores.VERIFICATION_SCORES.get(
        loan_details['isIncV'], 0
    )
    for k in scores.LOAN_ATTRIBUTE_WEIGHTS:
        score += loan_details[k] * scores.LOAN_ATTRIBUTE_WEIGHTS.get(
            k, 0
        )
    score += home_ownership_score
    score += verification_score
    return 1 / (1 + math.exp(score))


def loans_owned_getter(headers, account_number):
    results = []
    url = url_builder('account_details', account_number)
    r = requests.get(url, headers=headers)
    response = r.json()
    notes = response.get('myNotes', [])
    for note in notes:
        results.append(note['loanId'])
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
