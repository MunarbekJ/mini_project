import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEIBU5kBXd5Sguj7Dqc8ouCxfKK_YaQLQACjRAAAl_bkUp3Bt1MNp18Sy4E' )
    bot.send_photo(message.chat.id, '')

def aaaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Сообщение не распознано')


@bot.message_handler(content_types=['sticker'])
def bbbb(message):
    bot.send_sticker(message.chat.id, message.sticker)


bot.polling()