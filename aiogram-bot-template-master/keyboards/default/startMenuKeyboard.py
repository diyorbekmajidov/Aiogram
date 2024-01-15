from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard_uz = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Kurslarimiz")],
        [
            KeyboardButton(text="💰Bepul darslar"),
            KeyboardButton(text="📍Filialni tanlang:"),],
        [KeyboardButton(text="⚙️ Texnik yordam"),
         KeyboardButton(text="📢 Siznig kurslaringiz")],
        ],
    resize_keyboard=True
)

keyboard_ru = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Наши курсы")],
        [
            KeyboardButton(text="💰Бесплатные уроки:"),
            KeyboardButton(text="📍Выберите филиал:"),
        ],
        [KeyboardButton(text="⚙️ Техническая поддержка:"),
         KeyboardButton(text="📢 Ваши курсы:")],
        ],
    resize_keyboard=True
)



settings_keyboard_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
settings_keyboard_uz.add(
    KeyboardButton(text="⚙️ tillni almashtirish"),
    KeyboardButton(text="ℹ️ info"),
    KeyboardButton("⬅️ Orqaga",),
)

settings_keyboard_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
settings_keyboard_ru.add(
    KeyboardButton(text="⚙️ изменение языка"),
    KeyboardButton(text="ℹ️ info"),
    KeyboardButton("⬅️ Назад"),
)
