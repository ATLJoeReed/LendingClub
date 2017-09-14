#!/usr/bin/python3.6
import argparse
import os

from config import settings
import utils


def runner(preview=True):
    logger = utils.setup_logger('lending_club', 'lending_club.log')

    logger.info("=========================START WATCHER RUN=========================") # noqa

    account_number = settings.ACCOUNT_WATCHER['account_number']
    authorization_token = settings.ACCOUNT_WATCHER['authorization_token']

    headers = utils.header_builder(authorization_token)

    logger.info(
        "Processing orders for account: {}"
        .format(account_number)
    )
    logger.info("Preview mode: {}".format(preview))

    try:
        available_cash = utils.available_cash_getter(
            headers,
            account_number
        )
    except Exception as e:
        logger.error("Getting available cash: {}".format(e))

    logger.info("Available Cash Balance :${}".format(available_cash))

    if available_cash < 50:
        logger.info("Not enough available cash...")

    try:
        loans_owned = utils.get_loans_owned(headers, account_number)
    except Exception as e:
        logger.error("Getting loans owned: {}".format(e))

    print(loans_owned)

    watcher_account_number = \
        settings.ACCOUNT_WATCHER['watch_account_number']

    watcher_auth_token = utils.get_watcher_auth_token(
        watcher_account_number
    )

    watcher_headers = utils.header_builder(watcher_auth_token)

    recent_watcher_loans = utils.get_recent_loans(
        watcher_headers,
        watcher_account_number,
        800
    )

    print(recent_watcher_loans)

    logger.info("=========================END WATCHER RUN=========================") # noqa


if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--live",
        help="start placing orders",
        action="store_true"
    )
    args = parser.parse_args()
    if args.live:
        preview = False
    else:
        preview = True

    runner(preview)
