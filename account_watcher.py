#!/usr/bin/python3.6
from config import settings
import utils


def watch(preview, logger):
    logger.info("=====START WATCHER RUN=====") # noqa

    account_number = settings.ACCOUNT_WATCHER['account_number']
    authorization_token = settings.ACCOUNT_WATCHER['authorization_token']

    headers = utils.header_builder(authorization_token)

    logger.info(
        "Processing orders for account: {}"
        .format(account_number)
    )

    try:
        available_cash = utils.available_cash_getter(
            headers,
            account_number
        )
    except Exception as e:
        logger.error("Getting available cash: {}".format(e))
        return

    logger.info("Available Cash Balance :${}".format(available_cash))

    if available_cash < 50:
        logger.info("Not enough available cash...")
        return

    try:
        loans_owned = utils.get_loans_owned(headers, account_number)
    except Exception as e:
        logger.error("Getting loans owned: {}".format(e))
        return

    watcher_account_number = \
        settings.ACCOUNT_WATCHER['watch_account_number']

    watcher_auth_token = utils.get_watcher_auth_token(
        watcher_account_number
    )

    watcher_headers = utils.header_builder(watcher_auth_token)

    try:
        recent_watcher_loans = utils.get_recent_loans(
            watcher_headers,
            watcher_account_number,
            2400
        )
    except Exception as e:
        logger.error("Getting recent loans: {}".format(e))
        return

    payload = {}
    payload['aid'] = account_number
    payload['orders'] = []
    for loan in recent_watcher_loans:
        try:
            match_loan = utils.get_matching_loan(
                headers,
                loan['grade'],
                loan['term'],
                loans_owned,
                logger
            )
        except Exception as e:
            logger.error("Getting match loan: {}".format(e))
            continue

        logger.info("Loan found: {}".format(match_loan))
        if available_cash < 50:
            logger.info("You are out of cash...")
            break
        investment_amount = loan['noteAmount']
        logger.info("Investment amount: ${}".format(investment_amount))
        if investment_amount:
            payload['orders'].append(
                {
                    'loanId': match_loan['id'],
                    'requestedAmount': investment_amount
                }
            )

        available_cash -= investment_amount
        loans_owned.append(match_loan['id'])

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
            return

        logger.info("Order results: {}".format(order_results))

    logger.info("=====END WATCHER RUN=====") # noqa
