#!/usr/bin/python3.6
import utils

test_authorization_token = 'abcdefghijk1234567890'


def test_header_builer_1():
    headers = utils.header_builder(test_authorization_token)
    print(headers)
    assert headers == {
        'Content-Type': 'application/json',
        'Authorization': 'abcdefghijk1234567890',
        'Accept': 'application/json'
    }
