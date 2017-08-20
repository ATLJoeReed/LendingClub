#!/usr/bin/python3.6
import utils


def test_get_investment_amount_1():
    results = utils.get_investment_amount('F', .6499, 950, 150, .6500)
    assert results == 0


def test_get_investment_amount_2():
    results = utils.get_investment_amount('F', .6505, 950, 150, .6500)
    assert results == 50


def test_get_investment_amount_3():
    results = utils.get_investment_amount('G', .8125, 150, 150, .6500)
    assert results == 100


def test_get_investment_amount_4():
    results = utils.get_investment_amount('G', .9000, 150, 150, .6500)
    assert results == 150


def test_get_investment_amount_5():
    results = utils.get_investment_amount('G', .6505, 48, 150, .6500)
    assert results == 0


def test_get_investment_amount_6():
    results = utils.get_investment_amount('G', .801, 75, 150, .6500)
    assert results == 75


def test_get_investment_amount_7():
    results = utils.get_investment_amount('G', .901, 56, 150, .6500)
    assert results == 56


def test_get_investment_amount_8():
    results = utils.get_investment_amount('F', .649, 950, 150, .6500)
    assert results == 0


def test_get_investment_amount_9():
    results = utils.get_investment_amount('F', .845, 49, 150, .6500)
    assert results == 0


def test_get_investment_amount_10():
    results = utils.get_investment_amount('G', .845, 95, 150, .6500)
    assert results == 95


def test_get_investment_amount_11():
    results = utils.get_investment_amount('G', .9, 145, 150, .6500)
    assert results == 145


def test_get_investment_amount_12():
    results = utils.get_investment_amount('A', .9799, 500, 50, .9800)
    assert results == 0


def test_get_investment_amount_13():
    results = utils.get_investment_amount('A', .9999, 49, 50, .9800)
    assert results == 0


def test_get_investment_amount_14():
    results = utils.get_investment_amount('A', .9999, 51, 50, .9800)
    assert results == 50


def test_get_investment_amount_15():
    results = utils.get_investment_amount('B', .9499, 250, 50, .9500)
    assert results == 0


def test_get_investment_amount_16():
    results = utils.get_investment_amount('B', .950, 250, 50, .9500)
    assert results == 50
