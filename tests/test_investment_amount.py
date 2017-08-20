#!/usr/bin/python3.6
import utils


def test_get_investment_amount_1():
    loan = {
        'grade': 'F',
        'score': .6499,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 950)
    assert results == 0


def test_get_investment_amount_2():
    loan = {
        'grade': 'F',
        'score': .6505,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 950)
    assert results == 50


def test_get_investment_amount_3():
    loan = {
        'grade': 'G',
        'score': .8125,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 150)
    assert results == 100


def test_get_investment_amount_4():
    loan = {
        'grade': 'G',
        'score': .9000,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 150)
    assert results == 150


def test_get_investment_amount_5():
    loan = {
        'grade': 'G',
        'score': .6505,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 48)
    assert results == 0


def test_get_investment_amount_6():
    loan = {
        'grade': 'G',
        'score': .801,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 75)
    assert results == 75


def test_get_investment_amount_7():
    loan = {
        'grade': 'G',
        'score': .901,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 56)
    assert results == 56


def test_get_investment_amount_8():
    loan = {
        'grade': 'F',
        'score': .649,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 950)
    assert results == 0


def test_get_investment_amount_9():
    loan = {
        'grade': 'F',
        'score': .845,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 49)
    assert results == 0


def test_get_investment_amount_10():
    loan = {
        'grade': 'G',
        'score': .845,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 95)
    assert results == 95


def test_get_investment_amount_11():
    loan = {
        'grade': 'G',
        'score': .900,
        'min_probability_score': .6500,
        'max_investment_amount': 150
    }
    results = utils.get_investment_amount(loan, 145)
    assert results == 145


def test_get_investment_amount_12():
    loan = {
        'grade': 'A',
        'score': .9799,
        'min_probability_score': .9800,
        'max_investment_amount': 50
    }
    results = utils.get_investment_amount(loan, 500)
    assert results == 0


def test_get_investment_amount_13():
    loan = {
        'grade': 'A',
        'score': .9999,
        'min_probability_score': .9800,
        'max_investment_amount': 50
    }
    results = utils.get_investment_amount(loan, 49)
    assert results == 0


def test_get_investment_amount_14():
    loan = {
        'grade': 'A',
        'score': .9999,
        'min_probability_score': .9800,
        'max_investment_amount': 50
    }
    results = utils.get_investment_amount(loan, 51)
    assert results == 50


def test_get_investment_amount_15():
    loan = {
        'grade': 'B',
        'score': .9499,
        'min_probability_score': .9500,
        'max_investment_amount': 50
    }
    results = utils.get_investment_amount(loan, 250)
    assert results == 0


def test_get_investment_amount_16():
    loan = {
        'grade': 'B',
        'score': .950,
        'min_probability_score': .9500,
        'max_investment_amount': 50
    }
    results = utils.get_investment_amount(loan, 250)
    assert results == 50
