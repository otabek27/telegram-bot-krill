from transliterate import to_latin, to_cyrillic

import telebot

# botni token qismi
TOKEN = "8771634564:AAFUcqWe61z1oU1_VGWIAX5klIwm6eyUvm0"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

#bu o'zini nima qila olishini tanishtirish qismi.
@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "👋 Assalomu alaykum!\n\n"
    javob += "🤖 Lotin ↔ Kirill botiga xush kelibsiz!\n\n"
    javob += "🔄 Men siz yuborgan matnni avtomatik ravishda boshqa alifboga o'girib beraman.\n\n"
    javob += "✍️ Marhamat, matningizni yuboring:"
    bot.reply_to(message, javob)

#bu lotinchani kirilchaga o'zgartiradigan qismi.
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg).title()
    else:
        javob = to_latin(msg).title()
    bot.reply_to(message, javob)

bot.infinity_polling()