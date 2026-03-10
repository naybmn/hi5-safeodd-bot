import requests

API_KEY = "YOUR_API_KEY"

headers = {
    "x-apisports-key": API_KEY
}


def get_matches():

    url = "https://v3.football.api-sports.io/fixtures?next=300"

    response = requests.get(url, headers=headers)

    return response.json()


def get_live_matches():

    url = "https://v3.football.api-sports.io/fixtures?live=all"

    response = requests.get(url, headers=headers)

    return response.json()
