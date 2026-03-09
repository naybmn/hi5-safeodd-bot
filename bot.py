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

    slip1 = picks[0:2]
    slip2 = picks[2:4]
    slip3 = picks[4:6]

    message = "⚽ DAILY SAFE SLIPS\n\n"

    message += "🔥 Slip 1\n"
    for h,a,t in slip1:
        message += f"{h} vs {a} - {t}\n"

    message += "\n🔥 Slip 2\n"
    for h,a,t in slip2:
        message += f"{h} vs {a} - {t}\n"

    message += "\n🔥 Slip 3\n"
    for h,a,t in slip3:
        message += f"{h} vs {a} - {t}\n"

    bot.send_message(CHAT_ID, message)

schedule.every().day.at("16:10").do(send_tip)
while True:
    schedule.run_pending()
    time.sleep(30)
 def send_tip():

    matches = get_matches()
    picks = select_safe(matches)

    if len(picks) < 6:
        bot.send_message(CHAT_ID, "⚠️ Not enough matches today")
        return

    slip1 = picks[0:2]
    slip2 = picks[2:4]
    slip3 = picks[4:6]

    message = "⚽ DAILY SAFE SLIPS\n\n"

    message += "🔥 Slip 1\n"
    for h,a,t in slip1:
        message += f"{h} vs {a} - {t}\n"

    message += "\n🔥 Slip 2\n"
    for h,a,t in slip2:
        message += f"{h} vs {a} - {t}\n"

    message += "\n🔥 Slip 3\n"
    for h,a,t in slip3:
        message += f"{h} vs {a} - {t}\n"

    bot.send_message(CHAT_ID, message)
