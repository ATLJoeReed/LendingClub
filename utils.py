import math

from config import scores


def loan_scorer(loan_details):

    score = scores.BASE

    home_ownership_score = scores.HOME_OWNERSHIP_SCORES.get(
        loan_details['homeOwnership'], 0
    )

    verification_score = scores.VERIFICATION_SCORES.get(
        loan_details['isIncV'], 0
    )

    for k in scores.LOAN_ATTRIBUTE_WEIGHTS:
        score += loan_details[k] * scores.LOAN_ATTRIBUTE_WEIGHTS.get(
            k, 0
        )

    score += home_ownership_score
    score += verification_score

    return 1 / (1 + math.exp(score))
