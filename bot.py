import telebot
import requests

TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"

bot = telebot.TeleBot(TOKEN)

API_KEY = "309ccb7ddf229c9ca71d2865df1d8e5d"

headers = {
    "x-apisports-key": API_KEY
}


def get_matches():

    url = "https://v3.football.api-sports.io/fixtures?next=30"

    r = requests.get(url, headers=headers)

    return r.json()


def safe_model(data):

    picks = []

    for match in data["response"]:

        try:

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            league = match["league"]["name"]

            picks.append((home, away, league, "Home Win"))

        except:
            continue

    return picks[:3]


def value_model(data):

    picks = []

    for match in data["response"]:

        try:

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            league = match["league"]["name"]

            picks.append((home, away, league, "Over 2.5"))

        except:
            continue

    return picks[:3]


@bot.message_handler(commands=['start'])
def start(message):

    bot.reply_to(message,
    "⚽ Goal Guru Pro Bot Ready\n\nCommands:\n/safe\n/value\n/live")


@bot.message_handler(commands=['safe'])
def safe(message):

    data = get_matches()

    tips = safe_model(data)

    if len(tips) == 0:

        bot.reply_to(message,"❌ No safe tips today")

        return

    msg = "🔥 SAFE PICKS\n\n"

    for h,a,l,t in tips:

        msg += f"{h} vs {a}\nLeague: {l}\nTip: {t}\n\n"

    bot.reply_to(message,msg)


@bot.message_handler(commands=['value'])
def value(message):

    data = get_matches()

    tips = value_model(data)

    if len(tips) == 0:

        bot.reply_to(message,"❌ No value bets today")

        return

    msg = "💎 VALUE BETS\n\n"

    for h,a,l,t in tips:

        msg += f"{h} vs {a}\nLeague: {l}\nTip: {t}\n\n"

    bot.reply_to(message,msg)


@bot.message_handler(commands=['live'])
def live(message):

    bot.reply_to(message,"Live scan coming soon ⚡")


bot.infinity_polling()
