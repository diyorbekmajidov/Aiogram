from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import course_callback

coursesMenu = InlineKeyboardMarkup(row_width=2)
python = InlineKeyboardButton(text="🐍 SAT", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

django = InlineKeyboardButton(text="🌐 Umumiy matematika", callback_data=course_callback.new(item_name="django"))
coursesMenu.insert(django)

telegram = InlineKeyboardButton(text="🤖 Bolalar uchun matematika", callback_data="course:telegram")
coursesMenu.insert(telegram)

algorithm = InlineKeyboardButton(text="📈 DTM", callback_data="course:algorithm")
coursesMenu.insert(algorithm)

algorithm = InlineKeyboardButton(text=" Ingliz tili", callback_data="course:algorithm")
coursesMenu.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
coursesMenu.insert(back_button)