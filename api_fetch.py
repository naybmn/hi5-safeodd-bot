import requests

API_KEY = "309ccb7ddf229c9ca71d2865df1d8e5d"

headers = {
    "x-apisports-key": API_KEY
}

def get_matches():

    url = "https://v3.football.api-sports.io/fixtures?next=50"

    response = requests.get(url, headers=headers)

    return response.json()


def get_live_matches():

    url = "https://v3.football.api-sports.io/fixtures?live=all"

    response = requests.get(url, headers=headers)

    return response.json()
