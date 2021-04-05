import telebot
TOKEN = "1783464274:AAE14dAfYnGMZtPAKzGT_nANmKMlGJbJ0tY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy222, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()