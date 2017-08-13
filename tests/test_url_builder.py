#!/usr/bin/python3.6
import utils

test_account_number = '1234567890'


def test_url_builer_1():
    url = utils.url_builder('account_details', test_account_number)
    assert url == 'https://api.lendingclub.com/api/investor/v1/accounts/1234567890/summary' # noqa


def test_url_builer_2():
    url = utils.url_builder('get_loans')
    assert url == 'https://api.lendingclub.com/api/investor/v1/loans/listing?showAll=True' # noqa


def test_url_builer_3():
    url = utils.url_builder('loans_owned', test_account_number)
    assert url == 'https://api.lendingclub.com/api/investor/v1/accounts/1234567890/notes' # noqa


def test_url_builer_4():
    url = utils.url_builder('place_order', test_account_number)
    assert url == 'https://api.lendingclub.com/api/investor/v1/accounts/1234567890/orders' # noqa
