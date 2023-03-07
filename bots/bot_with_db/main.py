import telebot
from decouple import config
from buttons import Keyboard
from utils import get_db

token = config("TOKEN")


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello", reply_markup=Keyboard)

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

bot.polling()