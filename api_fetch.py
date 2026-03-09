import requests

API_KEY = "309ccb7ddf229c9ca71d2865df1d8e5d"

def get_matches():
    url = "https://v3.football.api-sports.io/fixtures?next=50"

    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)

    return response.json()
