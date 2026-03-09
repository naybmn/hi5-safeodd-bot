import requests

API_KEY = "YOUR_API_KEY"

def get_matches():
    url = "https://v3.football.api-sports.io/fixtures?next=20"

    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)

    return response.json()
