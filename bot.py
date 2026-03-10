import telebot
import schedule
import time

from api_fetch import get_live_matches
from predictor import live_tip_model


TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"
CHAT_ID = "@gaolguru"

bot = telebot.TeleBot(TOKEN)


def scan_live_matches():

    data = get_live_matches()

    tips = live_tip_model(data)

    if len(tips) == 0:
        return

    message = "🔥 LIVE MATCH ALERT\n\n"

    for h,a,m,t in tips:

        message += f"{h} vs {a}\nMinute: {m}\nTip: {t}\n\n"

    bot.send_message(CHAT_ID, message)


# check every 5 minutes
schedule.every(5).minutes.do(scan_live_matches)

scan_live_matches()

while True:

    schedule.run_pending()

    time.sleep(20)
