import requests

API_KEY = "309ccb7ddf229c9ca71d2865df1d8e5d"

HEADERS = {
    "x-apisports-key": API_KEY
}

BASE_URL = "https://v3.football.api-sports.io"

def get_upcoming_matches():

    url = BASE_URL + "/fixtures?next=50"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        data = r.json()

        if "response" not in data:
            return []

        return data["response"]

    except Exception as e:
        print("API ERROR:", e)
        return []


def get_live_matches():

    url = BASE_URL + "/fixtures?live=all"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        data = r.json()

        if "response" not in data:
            return []

        return data["response"]

    except:
        return []
