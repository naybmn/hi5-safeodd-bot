import telebot
import schedule
import time

from api_fetch import get_live_matches
from predictor import live_tip_model


TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"

CHANNEL_ID = "@gaolguru"

bot = telebot.TeleBot(TOKEN)

users = []


@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.chat.id

    if user_id not in users:
        users.append(user_id)

    bot.send_message(user_id,"Goal Guru Bot Activated ⚽")


def scan_live_matches():

    data = get_live_matches()

    tips = live_tip_model(data)

    if len(tips) == 0:
        return

    message = "🔥 LIVE MATCH ALERT\n\n"

    for h,a,m,t in tips:

        message += f"{h} vs {a}\nMinute: {m}\nTip: {t}\n\n"

    # send to channel
    bot.send_message(CHANNEL_ID,message)

    # send to bot users
    for user in users:
        bot.send_message(user,message)


schedule.every(5).minutes.do(scan_live_matches)


scan_live_matches()


import threading

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()


while True:

    schedule.run_pending()

    time.sleep(20)
