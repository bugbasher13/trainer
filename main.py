from os import environ

import telebot

if  __name__ == "__main__":
    print('Hellow World')
    bot = telebot.TeleBot(environ.get("TELEBOT_TOKEN"))

    @bot.message_handler(commands=['ping'])
    def ping_command(message):
        bot.send_message(message.chat.id, 'pong')


    bot.infinity_polling(timeout=20, long_polling_timeout=45)
