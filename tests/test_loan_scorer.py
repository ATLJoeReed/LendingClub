#!/usr/bin/python3.6
import utils


def test_loan_scorer_A_36_1():
    loan_details = {
        'id': 99897605,
        'term': 36,
        'grade': 'A',
        'annualInc': 55000.0,
        'collections12MthsExMed': 0,
        'dti': 13.95,
        'ficoRangeLow': 755,
        'inqLast6Mths': 0,
        'installment': 289.11,
        'loanAmount': 9600.0,
        'openAcc': 5,
        'pubRec': 0,
        'totalAcc': 22,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.960959208494436, 10)


def test_loan_scorer_A_36_2():
    loan_details = {
        'id': 103841197,
        'term': 36,
        'grade': 'A',
        'annualInc': 102315.0,
        'collections12MthsExMed': 0,
        'dti': 13.69,
        'ficoRangeLow': 830,
        'inqLast6Mths': 0,
        'installment': 464.81,
        'loanAmount': 15000.0,
        'openAcc': 10,
        'pubRec': 0,
        'totalAcc': 27,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.983438898102987, 10)


def test_loan_scorer_A_36_3():
    loan_details = {
        'id': 103698656,
        'term': 36,
        'grade': 'A',
        'annualInc': 88000.0,
        'collections12MthsExMed': 1,
        'dti': 18.04,
        'ficoRangeLow': 690,
        'inqLast6Mths': 1,
        'installment': 309.87,
        'loanAmount': 10000.0,
        'openAcc': 16,
        'pubRec': 0,
        'totalAcc': 49,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.910296226095271, 10)


def test_loan_scorer_B_36_1():
    loan_details = {
        'id': 103508049,
        'term': 36,
        'grade': 'B',
        'annualInc': 25000.0,
        'collections12MthsExMed': 0,
        'dti': 11.71,
        'ficoRangeLow': 675,
        'inqLast6Mths': 1,
        'installment': 98.92,
        'loanAmount': 3000.0,
        'openAcc': 11,
        'pubRec': 2,
        'totalAcc': 31,
        'homeOwnership': 'RENT',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.847739873433882, 10)


def test_loan_scorer_B_36_2():
    loan_details = {
        'id': 103548164,
        'term': 36,
        'grade': 'B',
        'annualInc': 42000.0,
        'collections12MthsExMed': 0,
        'dti': 7.8,
        'ficoRangeLow': 695,
        'inqLast6Mths': 0,
        'installment': 158.98,
        'loanAmount': 4825.0,
        'openAcc': 6,
        'pubRec': 0,
        'totalAcc': 7,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.914198488093488, 10)


def test_loan_scorer_F_60_1():
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
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.627904547727398, 10)


def test_loan_scorer_F_60_2():
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
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.450748630346258, 10)


def test_loan_scorer_F_60_3():
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
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.514282389832506, 10)


def test_loan_scorer_G_60_1():
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
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.488146930528796, 10)


def test_loan_scorer_G_60_2():
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
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.615937627336136, 10)
