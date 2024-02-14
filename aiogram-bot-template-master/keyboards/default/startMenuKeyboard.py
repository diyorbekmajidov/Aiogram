from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

keyboard_uz = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Kurslarimiz"),
        KeyboardButton(text="Ijtimoiy tarmoqlar")],
        [
            KeyboardButton(text="💰Bepul darslar"),
            KeyboardButton(text="📍Filialni tanlang:"),],
        [KeyboardButton(text="⚙️ Texnik yordam"),
         KeyboardButton(text="👥 So'rovnoma", web_app=WebAppInfo(url='https://forms.gle/17cZ3ZFDGSkGLAqr6'))]
        ],
    resize_keyboard=True
)

keyboard_ru = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Наши курсы"),
         KeyboardButton(text="Социальные сети"),
         ],
        [
            KeyboardButton(text="💰Бесплатные уроки:"),
            KeyboardButton(text="📍Выберите филиал:"),
        ],
        [KeyboardButton(text="⚙️ Техническая поддержка:"),
         KeyboardButton(text="👥 Анкета", web_app=WebAppInfo(url='https://forms.gle/4MgGb7vustYQoTY19'))],
        ],
    resize_keyboard=True
)


settings_keyboard_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
settings_keyboard_uz.add(
    KeyboardButton(text="⚙️ tillni almashtirish"),
    KeyboardButton(text="📢 Siznig kurslaringiz"),
    KeyboardButton("⬅️ Orqaga",),
)

settings_keyboard_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
settings_keyboard_ru.add(
    KeyboardButton(text="⚙️ изменение языка"),
    KeyboardButton(text="📢 Ваши курсы:"),
    KeyboardButton("⬅️ Назад"),
)

location_keyboard_uz = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Yagona daricha ')],  # city id in v
        [KeyboardButton(text='37-maktab')],
        [KeyboardButton("⬅️ Orqaga",),]
    ],resize_keyboard=True
)

location_keyboard_ru = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Единое окно')],  # city id in v
        [KeyboardButton(text='Школа 37')],
        [KeyboardButton("⬅️ Назад")]
    ],resize_keyboard=True
)

back_botton_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("⬅Orqaga",),]
    ],resize_keyboard=True)


back_botton_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("⬅Назад",),]
    ],resize_keyboard=True)
