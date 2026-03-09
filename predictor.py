def select_safe(matches):

    safe = []

    for match in matches["response"]:

        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        safe.append((home, away, "Home Win"))

    return safe[:6]
