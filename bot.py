import telebot
import schedule
import time

from api_fetch import get_matches, get_live_matches
from predictor import safe_prediction, live_under_model, value_bet_model


TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "@gaolguru"

bot = telebot.TeleBot(TOKEN)


def send_safe_slip():

    data = get_matches()

    picks = safe_prediction(data)

    message = "⚽ SAFE ODD SLIP\n\n"

    if len(picks) == 0:

        message += "No safe picks today."

    else:

        for h,a,t in picks:

            message += f"{h} vs {a}\nTip: {t}\n\n"

    bot.send_message(CHAT_ID, message)


def send_live_under():

    data = get_live_matches()

    alerts = live_under_model(data)

    if len(alerts) == 0:
        return

    message = "🔥 LIVE UNDER ALERT\n\n"

    for h,a,m in alerts:

        message += f"{h} vs {a}\nMinute: {m}\nTip: Under 2.5\n\n"

    bot.send_message(CHAT_ID, message)


def send_value_bet():

    data = get_live_matches()

    alerts = value_bet_model(data)

    if len(alerts) == 0:
        return

    message = "💎 VALUE BET ALERT\n\n"

    for h,a,m in alerts:

        message += f"{h} vs {a}\nMinute: {m}\nTip: Over 1.5\n\n"

    bot.send_message(CHAT_ID, message)


schedule.every().day.at("16:00").do(send_safe_slip)

schedule.every(10).minutes.do(send_live_under)

schedule.every(5).minutes.do(send_value_bet)


while True:

    schedule.run_pending()

    time.sleep(30)
