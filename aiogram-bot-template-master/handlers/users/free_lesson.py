from aiogram import types
from loader import dp, bot
from .start import databs
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def send_free_lessons(message: types.Message, text_data, keyboard):
    await message.answer(text_data, reply_markup=keyboard)

@dp.message_handler(text=['💰Bepul darslar','💰Бесплатные уроки:','💰Free lessons'])
async def free_lessons(message: types.Message):
    lang = databs.get_user(message.from_user.id)['lang']
    data = databs.get_free_lesson()
    text_data = ''
    keyboard = InlineKeyboardMarkup(row_width=5)

    for k, lesson in enumerate(data, start=1):
        if lang == "uz":
            text_data += f'{k}. {lesson["name_uz"]}\n'
        elif lang == 'en':
            text_data += f'{k}. {lesson["name_en"]}\n'
        else:
            text_data += f'{k}. {lesson["name_ru"]}\n'
        
        keyboard.insert(InlineKeyboardButton(text=str(k), callback_data=str(k), url=lesson["link"]))

    await send_free_lessons(message, text_data, keyboard)


