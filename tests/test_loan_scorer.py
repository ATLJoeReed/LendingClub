#!/usr/bin/python3.6
import utils


def test_loan_scorer_A_36_1():
    loan_details = {
        'id': 99897605,
        'term': 36,
        'grade': 'A',
        'annualInc': 55000.0,
        'collections12MthsExMed': 0,
        'dti': 13.95,
        'ficoRangeLow': 755,
        'inqLast6Mths': 0,
        'installment': 289.11,
        'loanAmount': 9600.0,
        'openAcc': 5,
        'pubRec': 0,
        'totalAcc': 22,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.960959208494436, 10)


def test_loan_scorer_A_36_2():
    loan_details = {
        'id': 103841197,
        'term': 36,
        'grade': 'A',
        'annualInc': 102315.0,
        'collections12MthsExMed': 0,
        'dti': 13.69,
        'ficoRangeLow': 830,
        'inqLast6Mths': 0,
        'installment': 464.81,
        'loanAmount': 15000.0,
        'openAcc': 10,
        'pubRec': 0,
        'totalAcc': 27,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.983438898102987, 10)


def test_loan_scorer_A_36_3():
    loan_details = {
        'id': 103698656,
        'term': 36,
        'grade': 'A',
        'annualInc': 88000.0,
        'collections12MthsExMed': 1,
        'dti': 18.04,
        'ficoRangeLow': 690,
        'inqLast6Mths': 1,
        'installment': 309.87,
        'loanAmount': 10000.0,
        'openAcc': 16,
        'pubRec': 0,
        'totalAcc': 49,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.910296226095271, 10)


def test_loan_scorer_B_36_1():
    loan_details = {
        'id': 103508049,
        'term': 36,
        'grade': 'B',
        'annualInc': 25000.0,
        'collections12MthsExMed': 0,
        'dti': 11.71,
        'ficoRangeLow': 675,
        'inqLast6Mths': 1,
        'installment': 98.92,
        'loanAmount': 3000.0,
        'openAcc': 11,
        'pubRec': 2,
        'totalAcc': 31,
        'homeOwnership': 'RENT',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.847739873433882, 10)


def test_loan_scorer_B_36_2():
    loan_details = {
        'id': 103548164,
        'term': 36,
        'grade': 'B',
        'annualInc': 42000.0,
        'collections12MthsExMed': 0,
        'dti': 7.8,
        'ficoRangeLow': 695,
        'inqLast6Mths': 0,
        'installment': 158.98,
        'loanAmount': 4825.0,
        'openAcc': 6,
        'pubRec': 0,
        'totalAcc': 7,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.914198488093488, 10)


def test_loan_scorer_B_60_1():
    loan_details = {
        'id': 102967417,
        'term': 60,
        'grade': 'B',
        'annualInc': 200000.0,
        'collections12MthsExMed': 0,
        'dti': 17.5,
        'ficoRangeLow': 695,
        'inqLast6Mths': 0,
        'installment': 768.69,
        'loanAmount': 35000.0,
        'openAcc': 21,
        'pubRec': 0,
        'totalAcc': 32,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.829875678247567, 10)


def test_loan_scorer_B_60_2():
    loan_details = {
        'id': 103208104,
        'term': 60,
        'grade': 'B',
        'annualInc': 86000.0,
        'collections12MthsExMed': 0,
        'dti': 20.78,
        'ficoRangeLow': 775,
        'inqLast6Mths': 0,
        'installment': 658.88,
        'loanAmount': 30000.0,
        'openAcc': 14,
        'pubRec': 0,
        'totalAcc': 36,
        'homeOwnership': 'OWN',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.854824816239662, 10)


def test_loan_scorer_B_60_3():
    loan_details = {
        'id': 103208104,
        'term': 60,
        'grade': 'B',
        'annualInc': 86000.0,
        'collections12MthsExMed': 0,
        'dti': 20.78,
        'ficoRangeLow': 775,
        'inqLast6Mths': 0,
        'installment': 658.88,
        'loanAmount': 30000.0,
        'openAcc': 14,
        'pubRec': 0,
        'totalAcc': 36,
        'homeOwnership': 'OTHER',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.0, 10)


def test_loan_scorer_C_36_1():
    loan_details = {
        'id': 103648530,
        'term': 36,
        'grade': 'C',
        'annualInc': 50000.0,
        'collections12MthsExMed': 0,
        'dti': 16.54,
        'ficoRangeLow': 680,
        'inqLast6Mths': 1,
        'installment': 302.12,
        'loanAmount': 9000,
        'openAcc': 11,
        'pubRec': 0,
        'totalAcc': 13,
        'homeOwnership': 'RENT',
        'isIncV': 'VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.73549110586747, 10)


def test_loan_scorer_C_36_2():
    loan_details = {
        'id': 103754498,
        'term': 36,
        'grade': 'C',
        'annualInc': 60000.0,
        'collections12MthsExMed': 0,
        'dti': 13.32,
        'ficoRangeLow': 680,
        'inqLast6Mths': 0,
        'installment': 173.31,
        'loanAmount': 5000,
        'openAcc': 5,
        'pubRec': 0,
        'totalAcc': 17,
        'homeOwnership': 'OWN',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.820926603236312, 10)


def test_loan_scorer_C_36_3():
    loan_details = {
        'id': 103537578,
        'term': 36,
        'grade': 'C',
        'annualInc': 73000.0,
        'collections12MthsExMed': 0,
        'dti': 12.05,
        'ficoRangeLow': 675,
        'inqLast6Mths': 0,
        'installment': 241.70,
        'loanAmount': 7200,
        'openAcc': 7,
        'pubRec': 1,
        'totalAcc': 24,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.863419298456295, 10)


def test_loan_scorer_C_60_1():
    loan_details = {
        'id': 103991607,
        'term': 60,
        'grade': 'C',
        'annualInc': 178500.0,
        'collections12MthsExMed': 0,
        'dti': 16.69,
        'ficoRangeLow': 725,
        'inqLast6Mths': 0,
        'installment': 348.95,
        'loanAmount': 15000,
        'openAcc': 27,
        'pubRec': 0,
        'totalAcc': 63,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.868770310315056, 10)


def test_loan_scorer_C_60_2():
    loan_details = {
        'id': 103167243,
        'term': 60,
        'grade': 'C',
        'annualInc': 55000.0,
        'collections12MthsExMed': 0,
        'dti': 13.68,
        'ficoRangeLow': 690,
        'inqLast6Mths': 0,
        'installment': 442.5,
        'loanAmount': 18200,
        'openAcc': 9,
        'pubRec': 1,
        'totalAcc': 16,
        'homeOwnership': 'RENT',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.706840286357261, 10)


def test_loan_scorer_C_60_3():
    loan_details = {
        'id': 103618013,
        'term': 60,
        'grade': 'C',
        'annualInc': 60000.0,
        'collections12MthsExMed': 0,
        'dti': 21.42,
        'ficoRangeLow': 710,
        'inqLast6Mths': 2,
        'installment': 372.21,
        'loanAmount': 16000,
        'openAcc': 9,
        'pubRec': 0,
        'totalAcc': 27,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.773734013380495, 10)


def test_loan_scorer_D_36_1():
    loan_details = {
        'id': 103487929,
        'term': 36,
        'grade': 'D',
        'annualInc': 85000.0,
        'collections12MthsExMed': 0,
        'dti': 0.35,
        'ficoRangeLow': 665,
        'inqLast6Mths': 0,
        'installment': 1071.13,
        'loanAmount': 29225.0,
        'openAcc': 3,
        'pubRec': 1,
        'totalAcc': 8,
        'homeOwnership': 'RENT',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.71953140281854, 10)


def test_loan_scorer_D_36_2():
    loan_details = {
        'id': 102774529,
        'term': 36,
        'grade': 'D',
        'annualInc': 42640.0,
        'collections12MthsExMed': 0,
        'dti': 11.82,
        'ficoRangeLow': 725,
        'inqLast6Mths': 2,
        'installment': 154.18,
        'loanAmount': 4325.0,
        'openAcc': 3,
        'pubRec': 0,
        'totalAcc': 3,
        'homeOwnership': 'RENT',
        'isIncV': 'VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.753131944234832, 10)


def test_loan_scorer_D_36_3():
    loan_details = {
        'id': 103417445,
        'term': 36,
        'grade': 'D',
        'annualInc': 100000.0,
        'collections12MthsExMed': 0,
        'dti': 15.82,
        'ficoRangeLow': 670,
        'inqLast6Mths': 1,
        'installment': 356.48,
        'loanAmount': 10000.0,
        'openAcc': 7,
        'pubRec': 0,
        'totalAcc': 20,
        'homeOwnership': 'OWN',
        'isIncV': 'VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.776594518432753, 10)


def test_loan_scorer_D_36_4():
    loan_details = {
        'id': 102354104,
        'term': 36,
        'grade': 'D',
        'annualInc': 100000.0,
        'collections12MthsExMed': 0,
        'dti': 7.93,
        'ficoRangeLow': 675,
        'inqLast6Mths': 2,
        'installment': 1140.73,
        'loanAmount': 32000.0,
        'openAcc': 5,
        'pubRec': 0,
        'totalAcc': 31,
        'homeOwnership': 'RENT',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.694579357092067, 10)


def test_loan_scorer_D_60_1():
    loan_details = {
        'id': 103215582,
        'term': 60,
        'grade': 'D',
        'annualInc': 80000.0,
        'collections12MthsExMed': 0,
        'dti': 8.07,
        'ficoRangeLow': 765,
        'inqLast6Mths': 1,
        'installment': 648.38,
        'loanAmount': 25000.0,
        'openAcc': 11,
        'pubRec': 0,
        'totalAcc': 19,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.77708875660573, 10)


def test_loan_scorer_D_60_2():
    loan_details = {
        'id': 103678446,
        'term': 60,
        'grade': 'D',
        'annualInc': 105000.0,
        'collections12MthsExMed': 0,
        'dti': 18.53,
        'ficoRangeLow': 670,
        'inqLast6Mths': 3,
        'installment': 765.24,
        'loanAmount': 28000.0,
        'openAcc': 23,
        'pubRec': 0,
        'totalAcc': 42,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.60762275715444, 10)


def test_loan_scorer_D_60_3():
    loan_details = {
        'id': 103387529,
        'term': 60,
        'grade': 'D',
        'annualInc': 72000.0,
        'collections12MthsExMed': 0,
        'dti': 25.43,
        'ficoRangeLow': 685,
        'inqLast6Mths': 0,
        'installment': 287.88,
        'loanAmount': 11100.0,
        'openAcc': 5,
        'pubRec': 0,
        'totalAcc': 26,
        'homeOwnership': 'RENT',
        'isIncV': 'VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.668264696103141, 10)


def test_loan_scorer_E_36_1():
    loan_details = {
        'id': 102324952,
        'term': 36,
        'grade': 'E',
        'annualInc': 45000.0,
        'collections12MthsExMed': 0,
        'dti': 30.93,
        'ficoRangeLow': 665,
        'inqLast6Mths': 0,
        'installment': 647.26,
        'loanAmount': 16500.0,
        'openAcc': 9,
        'pubRec': 1,
        'totalAcc': 21,
        'homeOwnership': 'RENT',
        'isIncV': 'VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.535662091446566, 10)


def test_loan_scorer_E_36_2():
    loan_details = {
        'id': 103752965,
        'term': 36,
        'grade': 'E',
        'annualInc': 21000.0,
        'collections12MthsExMed': 0,
        'dti': 6.97,
        'ficoRangeLow': 660,
        'inqLast6Mths': 1,
        'installment': 198.12,
        'loanAmount': 5000.0,
        'openAcc': 4,
        'pubRec': 0,
        'totalAcc': 25,
        'homeOwnership': 'RENT',
        'isIncV': 'VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.762876206380062, 10)


def test_loan_scorer_E_36_3():
    loan_details = {
        'id': 103667760,
        'term': 36,
        'grade': 'E',
        'annualInc': 95000.0,
        'collections12MthsExMed': 0,
        'dti': 34.7,
        'ficoRangeLow': 700,
        'inqLast6Mths': 0,
        'installment': 176.53,
        'loanAmount': 4500.0,
        'openAcc': 15,
        'pubRec': 0,
        'totalAcc': 20,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.662687328450222, 10)


def test_loan_scorer_E_60_1():
    loan_details = {
        'id': 103497615,
        'term': 60,
        'grade': 'E',
        'annualInc': 85000.0,
        'collections12MthsExMed': 0,
        'dti': 22.31,
        'ficoRangeLow': 720,
        'inqLast6Mths': 1,
        'installment': 481.33,
        'loanAmount': 16000.0,
        'openAcc': 26,
        'pubRec': 0,
        'totalAcc': 46,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.681519483143842, 10)


def test_loan_scorer_E_60_2():
    loan_details = {
        'id': 102407162,
        'term': 60,
        'grade': 'E',
        'annualInc': 52000.0,
        'collections12MthsExMed': 0,
        'dti': 3.06,
        'ficoRangeLow': 695,
        'inqLast6Mths': 1,
        'installment': 782.16,
        'loanAmount': 26000.0,
        'openAcc': 7,
        'pubRec': 0,
        'totalAcc': 19,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.764644431523134, 10)


def test_loan_scorer_E_60_3():
    loan_details = {
        'id': 103486259,
        'term': 60,
        'grade': 'E',
        'annualInc': 90000.0,
        'collections12MthsExMed': 0,
        'dti': 9.04,
        'ficoRangeLow': 705,
        'inqLast6Mths': 0,
        'installment': 392.58,
        'loanAmount': 14000.0,
        'openAcc': 10,
        'pubRec': 0,
        'totalAcc': 24,
        'homeOwnership': 'RENT',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.7388540711759, 10)


def test_loan_scorer_F_60_1():
    loan_details = {
        'id': 104043925,
        'term': 60,
        'grade': 'F',
        'annualInc': 44460.0,
        'collections12MthsExMed': 0,
        'dti': 14.44,
        'ficoRangeLow': 685,
        'inqLast6Mths': 2,
        'installment': 378.65,
        'loanAmount': 12000.0,
        'openAcc': 7,
        'pubRec': 0,
        'totalAcc': 29,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.627904547727398, 10)


def test_loan_scorer_F_60_2():
    loan_details = {
        'id': 100095416,
        'term': 60,
        'grade': 'F',
        'annualInc': 50000.0,
        'collections12MthsExMed': 0,
        'dti': 21.29,
        'ficoRangeLow': 680,
        'inqLast6Mths': 1,
        'installment': 419.67,
        'loanAmount': 13300.0,
        'openAcc': 5,
        'pubRec': 0,
        'totalAcc': 8,
        'homeOwnership': 'RENT',
        'isIncV': 'NOT_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.450748630346258, 10)


def test_loan_scorer_F_60_3():
    loan_details = {
        'id': 103338107,
        'term': 60,
        'grade': 'F',
        'annualInc': 58000.0,
        'collections12MthsExMed': 0,
        'dti': 13.22,
        'ficoRangeLow': 680,
        'inqLast6Mths': 0,
        'installment': 832.71,
        'loanAmount': 25500.0,
        'openAcc': 10,
        'pubRec': 0,
        'totalAcc': 18,
        'homeOwnership': 'OWN',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.514282389832506, 10)


def test_loan_scorer_G_60_1():
    loan_details = {
        'id': 103127873,
        'term': 60,
        'grade': 'G',
        'annualInc': 50000.0,
        'collections12MthsExMed': 0,
        'dti': 23.57,
        'ficoRangeLow': 680,
        'inqLast6Mths': 0,
        'installment': 690.3,
        'loanAmount': 21000.0,
        'openAcc': 12,
        'pubRec': 0,
        'totalAcc': 23,
        'homeOwnership': 'MORTGAGE',
        'isIncV': 'SOURCE_VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.488146930528796, 10)


def test_loan_scorer_G_60_2():
    loan_details = {
        'id': 102977476,
        'term': 60,
        'grade': 'G',
        'annualInc': 120000.0,
        'collections12MthsExMed': 0,
        'dti': 5.37,
        'ficoRangeLow': 660,
        'inqLast6Mths': 3,
        'installment': 988,
        'loanAmount': 30000.0,
        'openAcc': 9,
        'pubRec': 0,
        'totalAcc': 36,
        'homeOwnership': 'OWN',
        'isIncV': 'VERIFIED'
    }
    results = utils.loan_scorer(loan_details)
    assert round(results['score'], 10) == round(0.615937627336136, 10)
