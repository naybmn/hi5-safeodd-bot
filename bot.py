import telebot
import schedule
import time

TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"
CHAT_ID = "@gaolguru"

bot = telebot.TeleBot(TOKEN)

def send_tip():

    message = """
⚽ SAFE ODD ~2 DAILY SLIP

1️⃣ Team A vs Team B
League: Premier League
Tip: Team A Win

2️⃣ Team C vs Team D
League: La Liga
Tip: Over 1.5 Goals

💰 Total Odd ≈ 2.05
"""

    bot.send_message(CHAT_ID, message)

schedule.every().day.at("16:00").do(send_tip)

while True:
    schedule.run_pending()
    time.sleep(30)
