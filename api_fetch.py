import requests

API_KEY = "309ccb7ddf229c9ca71d2865df1d8e5d"

headers = {
    "x-apisports-key": API_KEY
}

def get_matches():

    url = "https://v3.football.api-sports.io/fixtures?next=100"

    r = requests.get(url,headers=headers)

    return r.json()

headers = {
    "x-apisports-key": API_KEY
}

def get_matches():

    url = "https://v3.football.api-sports.io/fixtures?next=30"

    r = requests.get(url,headers=headers)

    return r.json()
