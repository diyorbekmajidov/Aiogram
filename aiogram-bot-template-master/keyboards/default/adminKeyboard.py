from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_kurs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar Statistika"),
            KeyboardButton(text="Post yaratish")]]
            ,resize_keyboard=True)

admin_postButton = ReplyKeyboardMarkup(
    keyboard = [
       [ KeyboardButton("Text"),
         KeyboardButton("photo")],
        [KeyboardButton('video'),
         KeyboardButton('Orqaga')
         ]
    ],resize_keyboard=True

)

