from aiogram import types
keyboard = types.InlineKeyboardMarkup(row_width=2)
buttons = [
        types.InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data='uz'),
        types.InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data='ru')
    ]
buttons1 = [
    types.InlineKeyboardButton(text='🇬🇧 English', callback_data='en')
]
keyboard.add(*buttons)
keyboard.insert(*buttons1)

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
    [types.InlineKeyboardButton(text="✉️Поделиться", switch_inline_query="Premium Education")],
    ])

Social_Networks_en = types.InlineKeyboardMarkup(
    inline_keyboard=[[
    types.InlineKeyboardButton(text="Our Telegram page", url="https://t.me/premium_ed"),
    types.InlineKeyboardButton(text="Our Instagram page", url="https://www.instagram.com/premium_education.uz?igsh=MW45NjQ3ZjJvZWgyYw==")],
    [types.InlineKeyboardButton(text="✉️Sharing", switch_inline_query="Zo'r bot ekan")],
    ])
