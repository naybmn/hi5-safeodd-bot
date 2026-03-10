import telebot
import schedule
import time

from api_fetch import get_matches
from predictor import select_safe

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "@gaolguru"

bot = telebot.TeleBot(TOKEN)


def send_tip():

    matches = get_matches()
    picks = select_safe(matches)

    message = "⚽ SAFE ODD SLIP\n\n"

    if len(picks) == 0:
        message += "No safe matches found right now."
    else:
        for h, a, t in picks:
            message += f"{h} vs {a}\nTip: {t}\n\n"

    bot.send_message(CHAT_ID, message)


schedule.every(1).hours.do(send_tip)

while True:
    schedule.run_pending()
    time.sleep(30)
from api_fetch import get_live_matches
from predictor import live_alert
