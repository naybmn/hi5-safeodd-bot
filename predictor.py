def select_safe(matches):

    safe = []

    if "response" not in matches:
        return safe

    for match in matches["response"]:

        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        tip = "Home Win"

        safe.append((home, away, tip))

    return safe
