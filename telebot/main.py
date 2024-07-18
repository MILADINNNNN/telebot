import telebot
from random import choice
token = '7217309586:AAE8PxbGrMr8X_ISlAAY6ZHIdrkwj49reoo'

bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """\
# Hi there, I am EchoBot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


greetings = ["Привет", "Здравствуйте", "Добрый день", "Хелоу", "Приветстваю"]

@bot.message_handler(commands=['greet'])
def greet_handler(message):
    greeting = choice(greetings)
    bot.reply_to(message, greeting)

bot.infinity_polling()