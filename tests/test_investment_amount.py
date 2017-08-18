#!/usr/bin/python3.6
import utils


def test_get_investment_amount_1():
    results = utils.get_investment_amount('F', 36, .6425, 950, 150)
    assert results == 0


def test_get_investment_amount_2():
    results = utils.get_investment_amount('F', 60, .6505, 950, 150)
    assert results == 50


def test_get_investment_amount_3():
    results = utils.get_investment_amount('G', 60, .8125, 150, 150)
    assert results == 100


def test_get_investment_amount_4():
    results = utils.get_investment_amount('G', 36, .9000, 150, 150)
    assert results == 150


def test_get_investment_amount_5():
    results = utils.get_investment_amount('G', 60, .6505, 48, 150)
    assert results == 0


def test_get_investment_amount_6():
    results = utils.get_investment_amount('G', 36, .801, 75, 150)
    assert results == 75


def test_get_investment_amount_7():
    results = utils.get_investment_amount('G', 60, .901, 56, 150)
    assert results == 56


def test_get_investment_amount_8():
    results = utils.get_investment_amount('F', 36, .649, 950, 150)
    assert results == 0


def test_get_investment_amount_9():
    results = utils.get_investment_amount('F', 60, .845, 49, 150)
    assert results == 0


def test_get_investment_amount_10():
    results = utils.get_investment_amount('G', 36, .845, 95, 150)
    assert results == 95


def test_get_investment_amount_11():
    results = utils.get_investment_amount('G', 60, .9, 145, 150)
    assert results == 145


def test_get_investment_amount_12():
    results = utils.get_investment_amount('A', 60, .9799, 500, 50)
    assert results == 50


def test_get_investment_amount_13():
    results = utils.get_investment_amount('A', 60, .9999, 49, 50)
    assert results == 0
