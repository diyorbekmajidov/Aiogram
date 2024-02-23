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
         KeyboardButton(text="👥 So'rovnoma", web_app=WebAppInfo(url='https://docs.google.com/forms/d/e/1FAIpQLSfaz5GMsD1_Yju8OHL_gpAlupLJnWHqisxuW9VuJ6wnSlEbXg/viewform?usp=sf_link'))]
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
         KeyboardButton(text="👥 Анкета", web_app=WebAppInfo(url='https://docs.google.com/forms/d/e/1FAIpQLScX_XrIarGis_9On_7EyfaDTQRypiV3v4m9YAolAtqx6MKzmg/viewform?usp=sf_link'))],
        ],
    resize_keyboard=True
)

keyboard_en = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Our courses"),
        KeyboardButton(text="Social networks")],
        [
            KeyboardButton(text="💰Free lessons"),
            KeyboardButton(text="📍Choose a branch:"),],
        [KeyboardButton(text="⚙️ Technical support"),
         KeyboardButton(text="👥 Questionnaire", web_app=WebAppInfo(url='https://docs.google.com/forms/d/e/1FAIpQLSfaz5GMsD1_Yju8OHL_gpAlupLJnWHqisxuW9VuJ6wnSlEbXg/viewform?usp=sf_link'))]
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

settings_keyboard_en = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
settings_keyboard_en.add(
    KeyboardButton(text="⚙️ change language"),
    KeyboardButton(text="📢 Your courses"),
    KeyboardButton("⬅️ Back",),
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

location_keyboard_en = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='A single window')],  # city id in v
        [KeyboardButton(text='School 37')],
        [KeyboardButton("⬅️ Back")]
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
