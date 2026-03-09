import telebot
import schedule
import time

from api_fetch import get_matches
from predictor import select_safe

TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"
CHAT_ID = "@gaolguru"

bot = telebot.TeleBot(TOKEN)


def send_tip():

    matches = get_matches()
    picks = select_safe(matches)

    if len(picks) < 2:
        return

    message = "⚽ SAFE ODD SLIP\n\n"

    for h, a, t in picks:
        message += f"{h} vs {a}\nTip: {t}\n\n"

    message += "💰 Total Odd ≈ 2.00"

    bot.send_message(CHAT_ID, message)


schedule.every(1).hours.do(send_tip)
send_tip()
while True:
    schedule.run_pending()
    time.sleep(30)
