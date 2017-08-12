from config import settings
import utils


logger = utils.setup_logger('lending_clug', 'lending_club.log')

logger.info("=========================START RUN=========================")

for account in settings.ACCOUNTS:

    account_number = account['account_number']
    authorization_token = account['authorization_token']
    loan_grades = account['loan_grades']
    min_probability_score = account['min_probability_score']
    max_loan_invest = account['max_loan_invest']

    headers = utils.header_builder(authorization_token)

    try:
        available_cash = utils.available_cash_getter(
            headers,
            account_number
        )
    except Exception as e:
        logger.error("Getting available cash: {}".format(e))
        raise SystemExit

    try:
        loans_owned = utils.loans_owned_getter(headers, account_number)
    except Exception as e:
        logger.error("Getting loans owned: {}".format(e))
        raise SystemExit

    try:
        loans = utils. get_loans(
            headers,
            loan_grades,
            min_probability_score,
            logger
        )
    except Exception as e:
        logger.error("Getting all open loans: {}".format(e))
        raise SystemExit

    logger.info("Available Cash Balance :${}".format(available_cash))

    new_loans = [l for l in loans if l not in loans_owned]
    payload = {}
    payload['aid'] = account_number
    payload['orders'] = []
    for loan in new_loans:
        logger.info("Loan found: {}".format(loan))

        payload['orders'].append(
            {
                'loanId': loan['id'],
                'requestedAmount': max_loan_invest
            }
        )

    logger.info("Payload: {}".format(payload))

    order_results = utils.order_placer(headers, account_number, payload)
    logger.info("Order results: {}".format(order_results))

logger.info("==========================END RUN==========================")
