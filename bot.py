import telebot

from api_fetch import get_upcoming_matches, get_live_matches
from predictor import build_safe_tips, build_value_tips, build_live_tips

TOKEN = "8447450102:AAF9znuSEuuJ0Uk-qdZD-QiQ36KUWzSUWxg"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

    text = """
⚽ Goal Guru AI V7

Commands

/safe   → Safe bets
/value  → Value bets
/live   → Live match tips
/today  → Today's matches
/help   → Help
"""

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def help_cmd(message):

    text = """
Goal Guru AI Commands

/safe
/value
/live
/today
"""

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['today'])
def today(message):

    matches = get_upcoming_matches()

    if not matches:
        bot.send_message(message.chat.id,"❌ No matches found")
        return

    text = "📅 Upcoming Matches\n\n"

    for m in matches[:10]:

        home = m["teams"]["home"]["name"]
        away = m["teams"]["away"]["name"]

        text += f"{home} vs {away}\n"

    bot.send_message(message.chat.id,text)


@bot.message_handler(commands=['safe'])
def safe(message):

    matches = get_upcoming_matches()

    if not matches:
        bot.send_message(message.chat.id,"❌ No safe tips available")
        return

    tips = build_safe_tips(matches)

    text = "⚽ SAFE BETS\n\n"

    for t in tips:

        text += f"""{t['home']} vs {t['away']}
Pick: {t['pick']}
Confidence: {t['confidence']}%

"""

    bot.send_message(message.chat.id,text)


@bot.message_handler(commands=['value'])
def value(message):

    matches = get_upcoming_matches()

    if not matches:
        bot.send_message(message.chat.id,"❌ No value bets right now")
        return

    tips = build_value_tips(matches)

    text = "📊 VALUE BETS\n\n"

    for t in tips:

        text += f"""{t['home']} vs {t['away']}
Pick: {t['pick']}
Confidence: {t['confidence']}%

"""

    bot.send_message(message.chat.id,text)


@bot.message_handler(commands=['live'])
def live(message):

    matches = get_live_matches()

    if not matches:
        bot.send_message(message.chat.id,"🔴 No live tips right now")
        return

    tips = build_live_tips(matches)

    text = "🔴 LIVE TIPS\n\n"

    for t in tips:

        text += f"""{t['home']} vs {t['away']}
Minute: {t['minute']}
Pick: {t['pick']}

"""

    bot.send_message(message.chat.id,text)


print("Goal Guru AI V7 Running...")

bot.infinity_polling()
