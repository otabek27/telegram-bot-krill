import telebot
TOKEN = "8771634564:AAEGVhx1ZsvhFK9G-MQkwJ5RW-AYyJoEnWM"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "👋 Assalomu alaykum!\n" \
    "Tug'ilgan yilingizni kiriting,men yoshingizni topaman" 
    bot.reply_to(message, javob)
 
#bu lotinchani kirilchaga o'zgartiradigan qismi.
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    son = message.text
    if son.isdigit():
        yosh = 2026 - int(son)
        javob = f"Siz {yosh} yoshdasiz"
    else:
        javob = "Iltimos, faqat raqam kiriting(masalan: 2005)"
    bot.reply_to(message, javob)

bot.infinity_polling()