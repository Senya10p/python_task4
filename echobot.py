import telebot

token = ''

bot = telebot.TeleBot(token)

name = 'Сеня'

@bot.message_handler(content_types=["text"])
def echo(message):
    word = message.text
    if word in name:
        word = 'Ба! Знакомые все лица!'
    bot.send_message(message.chat.id, word)

bot.polling(none_stop=True)