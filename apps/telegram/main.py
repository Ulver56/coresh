# сделайте свой файл settings.py на основе settings.exemple
import settings
import telebot


print (settings.tg_token)



#bot = telebot.TeleBot(settings.tg_token)

#@bot.message_handler(content_types=['text'])
#def lalala(message):
#    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)