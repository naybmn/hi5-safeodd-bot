def live_tip_model(data):

    tips = []

    for match in data["response"]:

        try:

            minute = match["fixture"]["status"]["elapsed"]

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            goals_home = match["goals"]["home"]
            goals_away = match["goals"]["away"]

            total_goals = goals_home + goals_away

            if minute >= 60 and total_goals <= 2:

                tip = "Over 1.5"

                tips.append((home, away, minute, tip))

        except:
            continue

    return tips
