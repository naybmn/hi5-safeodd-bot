def select_safe(data):

    picks = []

    for match in data["response"]:

        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        home_win = match["fixture"]["status"]["short"]

        # simple favorite logic
        if home and away:

            tip = f"{home} Win"

            picks.append((home, away, tip))

        if len(picks) >= 6:
            break

    return picks