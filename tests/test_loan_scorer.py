#!/usr/bin/python3
import utils


def test_loan_scorer_1():
    loan_details = {
        'id': 104043925,
        'term': 60,
        'grade': 'F',
        'annualInc': 44460.0,
        'collections12MthsExMed': 0,
        'dti': 14.44,
        'ficoRangeLow': 685,
        'inqLast6Mths': 2,
        'installment': 378.65,
        'loanAmount': 12000.0,
        'openAcc': 7,
        'pubRec': 0,
        'totalAcc': 29,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }

    score = utils.loan_scorer(loan_details)
    assert round(score, 10) == round(0.627904547727398, 10)


def test_loan_scorer_2():
    loan_details = {
        'id': 100095416,
        'term': 60,
        'grade': 'F',
        'annualInc': 50000.0,
        'collections12MthsExMed': 0,
        'dti': 21.29,
        'ficoRangeLow': 680,
        'inqLast6Mths': 1,
        'installment': 419.67,
        'loanAmount': 13300.0,
        'openAcc': 5,
        'pubRec': 0,
        'totalAcc': 8,
        'homeOwnership': 'RENT',
        'isIncV': 'NOT_VERIFIED'
    }

    score = utils.loan_scorer(loan_details)
    assert round(score, 10) == round(0.450748630346258, 10)


def test_loan_scorer_3():
    loan_details = {
        'id': 103338107,
        'term': 60,
        'grade': 'F',
        'annualInc': 58000.0,
        'collections12MthsExMed': 0,
        'dti': 13.22,
        'ficoRangeLow': 680,
        'inqLast6Mths': 0,
        'installment': 832.71,
        'loanAmount': 25500.0,
        'openAcc': 10,
        'pubRec': 0,
        'totalAcc': 18,
        'homeOwnership': 'OWN',
        'isIncV': 'SOURCE_VERIFIED'
    }

    score = utils.loan_scorer(loan_details)
    assert round(score, 10) == round(0.514282389832506, 10)


def test_loan_scorer_4():
    loan_details = {
        'id': 103127873,
        'term': 60,
        'grade': 'G',
        'annualInc': 50000.0,
        'collections12MthsExMed': 0,
        'dti': 23.57,
        'ficoRangeLow': 680,
        'inqLast6Mths': 0,
        'installment': 690.3,
        'loanAmount': 21000.0,
        'openAcc': 12,
        'pubRec': 0,
        'totalAcc': 23,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'SOURCE_VERIFIED'
    }

    score = utils.loan_scorer(loan_details)
    assert round(score, 10) == round(0.488146930528796, 10)


def test_loan_scorer_5():
    loan_details = {
        'id': 102977476,
        'term': 60,
        'grade': 'G',
        'annualInc': 120000.0,
        'collections12MthsExMed': 0,
        'dti': 5.37,
        'ficoRangeLow': 660,
        'inqLast6Mths': 3,
        'installment': 988,
        'loanAmount': 30000.0,
        'openAcc': 9,
        'pubRec': 0,
        'totalAcc': 36,
        'homeOwnership': 'OWN',
        'isIncV': 'VERIFIED'
    }

    score = utils.loan_scorer(loan_details)
    assert round(score, 10) == round(0.615937627336136, 10)
