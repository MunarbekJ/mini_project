import telebot
from decouple import config
from parsing.db_utilsimport get_keyboard


bot = telebot.TeleBot(config("TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    @bot.callback_query_handler(lambda x: True)
def send_data(call):
    db = get_db()
    page = call.data
    products = db[page]
    for prod in products:
        text = f"""
Title: {prod['title']}
Price: {prod['price']}
"""
        bot.send_message(call.from_user.id, text)
    text = "Hello, we are parsing http"
    bot.send_message(message.chat.id, text disable)
    bot
    if not 
bot.polling()