import telebot
import schedule
import time

from api_fetch import get_matches
from predictor import safe_picks,value_picks

TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"

CHANNEL = "@gaolguru"

bot = telebot.TeleBot(TOKEN)


def post_tips():

    data = get_matches()

    safe = safe_picks(data)

    value = value_picks(data)

    message = "⚽ GOAL GURU AI BETTING BOT\n\n"

    if len(safe) > 0:

        message += "🔥 SAFE PICKS\n\n"

        for h,a,t,p in safe:

            message += f"{h} vs {a}\nTip: {t}\nConfidence: {round(p*100)}%\n\n"


    if len(value) > 0:

        message += "💎 VALUE BETS\n\n"

        for h,a,t,p in value:

            message += f"{h} vs {a}\nTip: {t}\nAI Edge: {round(p*100)}%\n\n"


    if len(safe)==0 and len(value)==0:

        return


    bot.send_message(CHANNEL,message)


schedule.every(30).minutes.do(post_tips)

print("Goal Guru AI Bot Running...")


while True:

    schedule.run_pending()

    time.sleep(20)
