import telebot
from telebot import types
token = "" #bot token
bot = telebot.TeleBot(token)
	
f = "Bot Firstname: {}".format(bot.get_me().first_name)
u = "\nBot username: {}".format(bot.get_me().username)
c = "\nBot ID: {}".format(bot.get_me().id)
k = "\n\nThank you for using this source :) \n                 \e[41m@Mrhalix"
print(f + u + c + k)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup()
	itembtna = types.InlineKeyboardButton('Bot Source',url='http://github.com/mrhalix/py-echo-bot')
	markup.row(itembtna)
    	bot.reply_to(message, "*Hi* i'm a `echo bot` written in [Python](http://python.org) language",reply_markup=markup,parse_mode='markdown',disable_web_page_preview=True)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
