from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_kurs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar Statistika"),
            KeyboardButton(text="Post yaratish")],
            [
             KeyboardButton("Bepul darslar qushish",),
             KeyboardButton("🛠 Admin qushish")
             ],
             [KeyboardButton("⬅️ Orqaga",),]
            ]
            ,resize_keyboard=True)


post_true_or_false = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("Ha"),
            KeyboardButton('Yuq')
            ]
        ],resize_keyboard=True
)

back_admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton('◀️ Orqaga')
    ]],resize_keyboard=True
)

