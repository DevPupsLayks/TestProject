import telebot

bot = telebot.TeleBot('7162762804:AAFpHcd57Ns6KjyEWnAwWTqsIM3eSLjsq9k')

@bot.message_handler(content_types=['text'])

def handle_text(message):

    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(content_types=['document', 'audio'])

def handle_other(message):
    pass

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)