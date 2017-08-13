#!/usr/bin/python3.6
import utils


def test_get_investment_amount_1():
    results = utils.get_investment_amount(.6425, 950)
    assert results == 0


def test_get_investment_amount_2():
    results = utils.get_investment_amount(.6505, 950)
    assert results == 50


def test_get_investment_amount_3():
    results = utils.get_investment_amount(.8125, 150)
    assert results == 100


def test_get_investment_amount_4():
    results = utils.get_investment_amount(.9000, 150)
    assert results == 150


def test_get_investment_amount_5():
    results = utils.get_investment_amount(.6505, 48)
    assert results == 0


def test_get_investment_amount_6():
    results = utils.get_investment_amount(.801, 75)
    assert results == 75


def test_get_investment_amount_7():
    results = utils.get_investment_amount(.901, 56)
    assert results == 56


def test_get_investment_amount_8():
    results = utils.get_investment_amount(.649, 950)
    assert results == 0


def test_get_investment_amount_9():
    results = utils.get_investment_amount(.845, 49)
    assert results == 0


def test_get_investment_amount_10():
    results = utils.get_investment_amount(.845, 95)
    assert results == 95


def test_get_investment_amount_11():
    results = utils.get_investment_amount(.9, 145)
    assert results == 145
