import constants
import telebot
from telebot import types

bot = telebot.TeleBot(constants.token)

markup = types.ReplyKeyboardMarkup(True, True)
item1 = types.KeyboardButton("Instagram")
item2 = types.KeyboardButton("VK")
item3 = types.KeyboardButton("Twitter")
markup.add(item1, item2, item3)


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Это LinkBot. Введите username")


@bot.message_handler(commands=["help"])
def help_handler(message):
    bot.send_message(message.chat.id, "Возникли вопросы? Пишите: @Vasily_Esipenko")


@bot.message_handler(content_types=["text"])
def text_handler(message):
    if message.text != "Instagram" and message.text != "VK" and message.text != "Twitter":
        global username
        username = message.text
        bot.send_message(message.chat.id, "Отлично, теперь выберите соцсеть:", reply_markup=markup)
    elif message.text == "Instagram":
        bot.send_message(message.chat.id, "https://www.instagram.com/{}".format(username))
    elif message.text == "VK":
        bot.send_message(message.chat.id, "https://vk.com/{}".format(username))
    elif message.text == "Twitter":
        bot.send_message(message.chat.id, "https://twitter.com/{}".format(username))


bot.polling()
