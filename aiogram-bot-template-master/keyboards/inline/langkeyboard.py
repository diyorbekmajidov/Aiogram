from aiogram import types
keyboard = types.InlineKeyboardMarkup(row_width=2)
buttons = [
        types.InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data='uz'),
        types.InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data='ru')
    ]
keyboard.add(*buttons)

Social_Networks_uz = types.InlineKeyboardMarkup(
    inline_keyboard=[[
    types.InlineKeyboardButton(text="Telegram sahifamiz", url="https://t.me/premium_ed"),
    types.InlineKeyboardButton(text="Instagram sahifamiz", url="https://www.instagram.com/premium_education.uz?igsh=MW45NjQ3ZjJvZWgyYw==")],
    [types.InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Zo'r bot ekan")],
    ])


Social_Networks_ru = types.InlineKeyboardMarkup(
inline_keyboard = [[
    types.InlineKeyboardButton(text="Наша страница в Telegram", url="https://t.me/premium_ed"),
    types.InlineKeyboardButton(text="Наша страница в Инстаграм", url="https://www.instagram.com/premium_education.uz?igsh=MW45NjQ3ZjJvZWgyYw==")],
    [types.InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Premium Education")],
    ])
