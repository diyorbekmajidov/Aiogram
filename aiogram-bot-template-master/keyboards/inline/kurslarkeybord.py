from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.callback_data import course_callback

coursesMenu = InlineKeyboardMarkup(row_width=2)
python = InlineKeyboardButton(text="🐍 SAT", callback_data=course_callback.new(item_name="SAT"))
coursesMenu.insert(python)

django = InlineKeyboardButton(text="🌐 Umumiy matematika", callback_data=course_callback.new(item_name="Umumiy matematika"))
coursesMenu.insert(django)

telegram = InlineKeyboardButton(text="🤖 Bolalar uchun matematika", callback_data="course:Bolalar uchun matematika")
coursesMenu.insert(telegram)

algorithm = InlineKeyboardButton(text="📈 DTM", callback_data="course:DTM")
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text=" Ingliz tili", callback_data="course:Ingliz tili")
coursesMenu.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="course:cancel")
coursesMenu.insert(back_button)



coursesMenu_ru = InlineKeyboardMarkup(row_width=2)
python = InlineKeyboardButton(text="🐍 SAT", callback_data=course_callback.new(item_name="SAT"))
coursesMenu_ru.insert(python)

django = InlineKeyboardButton(text="🌐 Общая математика", callback_data=course_callback.new(item_name="Umumiy matematika"))
coursesMenu_ru.insert(django)

telegram = InlineKeyboardButton(text="🤖 Математика для детей", callback_data="course:Bolalar uchun matematika")
coursesMenu_ru.insert(telegram)

algorithm = InlineKeyboardButton(text="📈 ДТМ", callback_data="course:DTM")
coursesMenu_ru.insert(algorithm)

algorithm = InlineKeyboardButton(text=" английский язык", callback_data="course:Ingliz tili")
coursesMenu_ru.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Назад", callback_data="course:cancel")
coursesMenu_ru.insert(back_button)


course_registration_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Kontaktingizni yuboring", request_contact=True)],
        [KeyboardButton(text="🔙 Ortga qaytish",)]
    ]
)

course_registaration_ru = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton("Отправьте свой контакт",request_contact=True)],
        [KeyboardButton(text="🔙 Назад",)]
    ]
)