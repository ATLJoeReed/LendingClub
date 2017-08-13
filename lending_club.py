#!/usr/bin/python3.6
import argparse
import os
import time

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
        if available_cash < 50:
            logger.info("You do not have enough available cash...")
            break

        time.sleep(.500)

        try:
            loans_owned = utils.loans_owned_getter(headers, account_number)
        except Exception as e:
            logger.error("Getting loans owned: {}".format(e))
            break

        if loans_owned:
            logger.info("Loans owned: {}".format(loans_owned))

        time.sleep(.500)

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

        if not loans:
            logger.info("No scored loans found...")
            break

        new_loans = [l for l in loans if l not in loans_owned]
        if not new_loans:
            logger.info("No scored loans (not owned) found...")
            break

        payload = {}
        payload['aid'] = account_number
        payload['orders'] = []
        for loan in new_loans:
            logger.info("Loan found: {}".format(loan))
            investment_amount = utils.get_investment_amount(
                loan['score'],
                available_cash
            )
            logger.info("Investment amount: ${}".format(investment_amount))

            if investment_amount > settings.MAX_INVESTMENT_AMOUNT:
                logger.error("Investment amount above maximum amount...")
                investment_amount = 50

            if investment_amount:
                payload['orders'].append(
                    {
                        'loanId': loan['id'],
                        'requestedAmount': investment_amount
                    }
                )
            else:
                break
            available_cash -= investment_amount

        logger.info("Payload: {}".format(payload))
        logger.info("Avaiable cash left: ${}".format(available_cash))

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
