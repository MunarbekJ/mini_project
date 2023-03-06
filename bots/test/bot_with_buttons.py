import telebot
from decouple import config

token = config('TOKEN')

# стикеры 
yes_sticker = 'CAACAgIAAxkBAAEIBZtkBYfN8TWLPhTz2k2wDeTzAfTtjQACfBkAAmuosElV4eHOstyHPy4E'
no_sticker = 'CAACAgIAAxkBAAEIBZ1kBYfXk1cWsBq4IO1h7XdsMLdlxAACGQAD6dgTKFdhEtpsYKrLLgQ'

bot = telebot.TeleBot(token)

#клавиатура под сообщением 
keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
b1 = telebot.types.KeyboardButton('Да')
b2 = telebot.types.KeyboardButton('Нет')
keyboard.add(b1, b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'Да':
        bot.send_sticker(message.chat.id, yes_sticker)
    elif message.text == 'Нет':
        bot.send_sticker(message.chat.id, no_sticker)
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку')

    bot.register_next_step_handler(message, reply_to_button)
bot.polling()