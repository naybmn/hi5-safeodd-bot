def select_safe(data):

    picks = []

    for match in data["response"]:

        try:

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            status = match["fixture"]["status"]["short"]

            if status != "NS":
                continue

            tip = home + " Win"

            picks.append((home, away, tip))

            if len(picks) >= 2:
                break

        except:
            continue

    return picks
def live_alert(data):

    alerts = []

    for match in data["response"]:

        try:

            minute = match["fixture"]["status"]["elapsed"]

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            goals_home = match["goals"]["home"]
            goals_away = match["goals"]["away"]

            total_goals = goals_home + goals_away

            if minute >= 60 and total_goals <= 1:

                alerts.append((home, away, minute))

        except:
            continue

    return alerts
