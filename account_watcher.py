#!/usr/bin/python3.6
import utils


def watch(preview, account_number, logger):
    logger.info("=====START WATCHER RUN=====") # noqa

    authorization_token = utils.get_account_watcher_auth_token(account_number)
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

    if available_cash < 25:
        logger.info("Not enough available cash...")
        return

    try:
        loans_owned = utils.get_loans_owned(headers, account_number)
    except Exception as e:
        logger.error("Getting loans owned: {}".format(e))
        return

    monitoring_account_number = utils.get_account_to_monitor(account_number)
    monitoring_auth_token = utils.get_monitoring_auth_token(
        monitoring_account_number
    )

    monitoring_headers = utils.header_builder(monitoring_auth_token)

    try:
        recent_monitoring_loans = utils.get_recent_loans(
            monitoring_headers,
            monitoring_account_number,
            15
        )
    except Exception as e:
        logger.error("Getting recent loans: {}".format(e))
        return

    if not recent_monitoring_loans:
        logger.info("No recent monitoring loans found...")
        return

    logger.info("Recent monitoring loans found: {}".format(recent_monitoring_loans)) # noqa

    payload = {}
    payload['aid'] = account_number
    payload['orders'] = []

    for loan in recent_monitoring_loans:
        try:
            match_loan = utils.get_matching_loan(
                headers,
                loan.get('grade', None),
                loan.get('term', None),
                loans_owned,
                logger
            )
        except Exception as e:
            logger.error("Getting match loan: {}".format(e))
            continue

        if not match_loan:
            logger.info("No matching loan found...")
            return

        logger.info("Loan found: {}".format(match_loan))
        investment_amount = loan.get('noteAmount', 0)
        if available_cash < investment_amount:
            logger.info("You do not have enough cash to make the purchase...")
            break
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
