from ai_engine import ai_probability,value_check

def safe_picks(data):

    picks = []

    for match in data["response"]:

        try:

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            prob = ai_probability()

            if prob > 0.70:

                picks.append((home,away,"Home Win",prob))

        except:
            continue

    return picks[:3]


def value_picks(data):

    picks = []

    for match in data["response"]:

        try:

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            odds = 2.10

            prob = ai_probability()

            if value_check(prob,odds):

                picks.append((home,away,"Over 2.5",prob))

        except:
            continue

    return picks[:3]
