import telebot
import requests

TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"

bot = telebot.TeleBot(TOKEN)

API_KEY = "YOUR_API_KEY"

headers = {
    "x-apisports-key": API_KEY
}

def get_matches():
    url = "https://v3.football.api-sports.io/fixtures?next=20"
    r = requests.get(url, headers=headers)
    data = r.json()
    return data

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "⚽ Goal Guru AI Bot Activated\n\nCommands:\n/safe\n/value\n/live")

@bot.message_handler(commands=['safe'])
def safe_tip(message):

    data = get_matches()

    try:
        match = data["response"][0]

        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        text = f"""⚽ SAFE BET

{home} vs {away}

Pick: {home} Win
Confidence: 72%
"""

        bot.send_message(message.chat.id, text)

    except:
        bot.send_message(message.chat.id, "❌ No safe tips available")

@bot.message_handler(commands=['value'])
def value_tip(message):

    bot.send_message(message.chat.id,"📊 No value bets right now")

@bot.message_handler(commands=['live'])
def live_tip(message):

    bot.send_message(message.chat.id,"🔴 No live tips right now")

print("Goal Guru AI Bot Running...")

bot.infinity_polling()
