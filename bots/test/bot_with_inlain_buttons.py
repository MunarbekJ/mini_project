import telebot
from decouple import config

token = config('TOKEN')

# стикеры 
yes_sticker = 'CAACAgIAAxkBAAEIBZtkBYfN8TWLPhTz2k2wDeTzAfTtjQACfBkAAmuosElV4eHOstyHPy4E'
no_sticker = 'CAACAgIAAxkBAAEIBZ1kBYfXk1cWsBq4IO1h7XdsMLdlxAACGQAD6dgTKFdhEtpsYKrLLgQ'

# клавиатура под сообщением 
Keyboard = telebot.types.InlineKeyboardMarkup()
b1  = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
b2  = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
Keyboard.add(b1, b2)


bot = telebot.TeleBot(token)


# func - функция фильтр в данном ситуация разрешаются все сообщение
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes'
        bot.send_sticker(call.from_user.id, yes_sticker)
        elif message.text
        bot.send_sticker(call.from_user.id, no_sticker)

bot.polling()