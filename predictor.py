import random

def build_safe_tips(matches):

    tips = []

    for m in matches[:5]:

        home = m["teams"]["home"]["name"]
        away = m["teams"]["away"]["name"]

        confidence = random.randint(72,88)

        tips.append({
            "home": home,
            "away": away,
            "pick": home + " Win",
            "confidence": confidence
        })

    return tips


def build_value_tips(matches):

    tips = []

    for m in matches[:4]:

        home = m["teams"]["home"]["name"]
        away = m["teams"]["away"]["name"]

        confidence = random.randint(65,80)

        tips.append({
            "home": home,
            "away": away,
            "pick": "Over 1.5 Goals",
            "confidence": confidence
        })

    return tips


def build_live_tips(matches):

    tips = []

    for m in matches[:3]:

        home = m["teams"]["home"]["name"]
        away = m["teams"]["away"]["name"]

        minute = m["fixture"]["status"]["elapsed"]

        tips.append({
            "home": home,
            "away": away,
            "minute": minute,
            "pick": "Under 3.5 Goals"
        })

    return tips
