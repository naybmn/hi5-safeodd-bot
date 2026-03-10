import telebot
import requests

TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"

bot = telebot.TeleBot(TOKEN)

API_KEY = "309ccb7ddf229c9ca71d2865df1d8e5d"

headers = {
    "x-apisports-key": API_KEY
}


def get_live_matches():

    url = "https://v3.football.api-sports.io/fixtures?live=all"

    r = requests.get(url, headers=headers)

    return r.json()


def get_next_matches():

    url = "https://v3.football.api-sports.io/fixtures?next=20"

    r = requests.get(url, headers=headers)

    return r.json()


# ---------------- LIVE MODEL ----------------

def live_model(data):

    tips = []

    for match in data["response"]:

        try:

            minute = match["fixture"]["status"]["elapsed"]

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            gh = match["goals"]["home"]
            ga = match["goals"]["away"]

            total = gh + ga

            if minute >= 60 and total <= 2:

                tips.append((home, away, minute, "Over 1.5"))

        except:
            continue

    return tips


# ---------------- SAFE MODEL ----------------

def safe_model(data):

    tips = []

    for match in data["response"]:

        try:

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            tips.append((home, away, "Home Win"))

        except:
            continue

    return tips[:5]


# ---------------- VALUE MODEL ----------------

def value_model(data):

    tips = []

    for match in data["response"]:

        try:

            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]

            tips.append((home, away, "Over 2.5"))

        except:
            continue

    return tips[:5]


# ---------------- COMMANDS ----------------


@bot.message_handler(commands=['start'])
def start(message):

    bot.reply_to(message,"⚽ Goal Guru Pro Bot Ready\n\nCommands:\n/live\n/safe\n/value")


@bot.message_handler(commands=['live'])
def live(message):

    data = get_live_matches()

    tips = live_model(data)

    if len(tips) == 0:

        bot.reply_to(message,"❌ No live tips right now")

        return

    msg = "🔥 LIVE BETTING TIPS\n\n"

    for h,a,m,t in tips:

        msg += f"{h} vs {a}\nMinute {m}\nTip: {t}\n\n"

    bot.reply_to(message,msg)


@bot.message_handler(commands=['safe'])
def safe(message):

    data = get_next_matches()

    tips = safe_model(data)

    if len(tips) == 0:

        bot.reply_to(message,"❌ No safe tips available")

        return

    msg = "✅ SAFE PICKS\n\n"

    for h,a,t in tips:

        msg += f"{h} vs {a}\nTip: {t}\n\n"

    bot.reply_to(message,msg)


@bot.message_handler(commands=['value'])
def value(message):

    data = get_next_matches()

    tips = value_model(data)

    if len(tips) == 0:

        bot.reply_to(message,"❌ No value bets right now")

        return

    msg = "💎 VALUE BETS\n\n"

    for h,a,t in tips:

        msg += f"{h} vs {a}\nTip: {t}\n\n"

    bot.reply_to(message,msg)


bot.infinity_polling()
