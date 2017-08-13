#!/usr/bin/python3.6
import argparse
import os

from config import settings
import utils


def runner(preview=True):
    logger = utils.setup_logger('lending_club', 'lending_club.log')

    logger.info("=========================START RUN=========================") # noqa

    for account in settings.ACCOUNTS:

        account_number = account['account_number']
        authorization_token = account['authorization_token']
        loan_grades = account['loan_grades']
        min_probability_score = account['min_probability_score']
        max_loan_invest = account['max_loan_invest']

        headers = utils.header_builder(authorization_token)

        logger.info("Processing orders for account: {}".format(account_number))
        logger.info("Preview mode: {}".format(preview))

        try:
            available_cash = utils.available_cash_getter(
                headers,
                account_number
            )
        except Exception as e:
            logger.error("Getting available cash: {}".format(e))
            break
        logger.info("Available Cash Balance :${}".format(available_cash))
        if not available_cash:
            logger.info("You have no available cash...")
            break

        max_number_loans = utils.get_max_number_loans(
            available_cash,
            max_loan_invest
        )
        logger.info(
            "Max number of loans to invest in: {}".format(max_number_loans)
        )
        if not max_number_loans:
            logger.info("You do not have enough available cash to place and order...") # noqa
            break

        try:
            loans_owned = utils.loans_owned_getter(headers, account_number)
        except Exception as e:
            logger.error("Getting loans owned: {}".format(e))
            break

        if loans_owned:
            logger.info("Loans owned: {}".format(loans_owned))

        try:
            loans = utils. get_loans(
                headers,
                loan_grades,
                min_probability_score,
                logger
            )
        except Exception as e:
            logger.error("Getting scored loans: {}".format(e))
            break

        new_loans = [l for l in loans if l not in loans_owned]
        if not new_loans:
            logger.info("No scored loans found...")
            break

        payload = {}
        payload['aid'] = account_number
        payload['orders'] = []
        for loan in new_loans[:max_number_loans]:
            logger.info("Loan found: {}".format(loan))

            payload['orders'].append(
                {
                    'loanId': loan['id'],
                    'requestedAmount': max_loan_invest
                }
            )

        logger.info("Payload: {}".format(payload))

        if not preview:
            try:
                order_results = utils.order_placer(
                    headers,
                    account_number,
                    payload
                )
            except Exception as e:
                logger.error("Placing order: {}".format(e))
                break

            logger.info("Order results: {}".format(order_results))

    logger.info("==========================END RUN==========================")


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
