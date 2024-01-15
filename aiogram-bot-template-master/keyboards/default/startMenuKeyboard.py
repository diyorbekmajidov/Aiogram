from aiogram import types

keyboard_uz = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
keyboard_uz.add(
    types.KeyboardButton(text="Kurslarimiz"),
    types.KeyboardButton(text="⚙️ Texnik yordam"),
    types.KeyboardButton(text="Bepul darslar"),
    )
# keyboard_uz.insert(
#         types.KeyboardButton("Boshqalarga ulashish", url="https://example.com"),
# )

keyboard_ru = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
keyboard_ru.add(
    types.KeyboardButton(text="Наши курсы"),
    types.KeyboardButton(text="⚙️ Техническая поддержка"),
    types.KeyboardButton(text="Бесплатные уроки"),
    )


settings_keyboard_uz = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
settings_keyboard_uz.add(
    types.KeyboardButton(text="⚙️ tillni almashtirish"),
    types.KeyboardButton(text="ℹ️ info"),
    types.KeyboardButton("📍Manzil",),
)

settings_keyboard_ru = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
settings_keyboard_ru.add(
    types.KeyboardButton(text="⚙️ изменение языка"),
    types.KeyboardButton(text="ℹ️ info"),
    types.KeyboardButton("📍Адрес"),
)
