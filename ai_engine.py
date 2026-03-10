import random

def ai_probability():

    return random.uniform(0.60,0.85)


def value_check(prob,odds):

    implied = 1/odds

    if prob > implied:

        return True

    return False
