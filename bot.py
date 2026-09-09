from transliterate import to_latin, to_cyrillic

import telebot


TOKEN = "8771634564:AAHawf-IM9n2W7uIs3h2Taa45zr-GfN1ilM"
bot = telebot.TeleBot(TOKEN, parse_mode=None)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob =  "Assalom aleykum @shahriyor_developer\n"
    javob += "matn kiriting: "
    bot.reply_to(message, javob)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)


      

bot.infinity_polling()