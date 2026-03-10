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
