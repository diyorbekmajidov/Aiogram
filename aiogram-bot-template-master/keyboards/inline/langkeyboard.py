from aiogram import types
keyboard = types.InlineKeyboardMarkup(row_width=2)
buttons = [
        types.InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data='uz'),
        types.InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data='ru')
    ]
keyboard.add(*buttons)