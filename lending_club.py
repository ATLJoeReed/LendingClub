import requests

from config import settings
import utils


r = requests.get(
    settings.GET_LOAN_URL,
    headers=settings.HEADERS
)

response = r.json()

loans = response['loans']

print("Total loans located: {}".format(len(loans)))

for loan in loans:
    if loan['grade'] in ['F', 'G']:  # and loan['term'] == 36:
        score = utils.loan_scorer(loan)
        print(
            "LoanID: {} - Term: {} - Grade: {} - "
            "Probablilty to fully pay: {}".format(
                loan['id'],
                loan['term'],
                loan['grade'],
                round(score, 4)
            )
        )
