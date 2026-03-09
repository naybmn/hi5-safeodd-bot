import telebot
import schedule
import time

TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"
CHAT_ID = "@gaolguru"

bot = telebot.TeleBot(TOKEN)

def send_tip():

    message = """
⚽ DAILY SAFE SLIPS

🔥 Slip 1
1️⃣ Team A vs Team B
Tip: Team A Win

2️⃣ Team C vs Team D
Tip: Over 1.5

💰 Total Odd ≈ 2.00


🔥 Slip 2
1️⃣ Team E vs Team F
Tip: Under 3.5

2️⃣ Team G vs Team H
Tip: Double Chance

💰 Total Odd ≈ 2.05


🔥 Slip 3
1️⃣ Team I vs Team J
Tip: Over 1.5

2️⃣ Team K vs Team L
Tip: Team K Win

💰 Total Odd ≈ 2.10
"""

    bot.send_message(CHAT_ID, message)

schedule.every().day.at("16:00").do(send_tip)
while True:
    schedule.run_pending()
    time.sleep(30)
