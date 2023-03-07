from telebot.types import InLineKeyboardMarkup, InlineKeyboardButton
from parsing.db_utils import get_pages
def get_keyboard()
    pages = get_pages()

    pages_Keyboard = InLineKeyboardMarkup()

buttons = []
for page in pages:
    button = InlineKeyboardButton(page, callback_data=page)
    buttons.append(button)

pages_Keyboard.add(*buttons)
return pages_keyboard
