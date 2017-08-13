#!/usr/bin/python3.6
import utils


def test_max_number_loans_1():
    results = utils.get_max_number_loans(980, 50)
    assert results == 19


def test_max_number_loans_2():
    results = utils.get_max_number_loans(1000, 255)
    assert results == 3
