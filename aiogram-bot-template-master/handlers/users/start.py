from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states.user_lang import UserLang
from keyboards.inline.langkeyboard import keyboard
from keyboards.default.startMenuKeyboard import keyboard_uz, keyboard_ru

from utils.db_api.db import DB
databs = DB('db.json')

@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(
        text=f"Salom {message.from_user.full_name}!\nBotdan foydalanish uchun tilni tanlang",
        reply_markup=keyboard
    )
    await UserLang.lang.set()

@dp.callback_query_handler(lambda c: c.data in ['uz', 'ru'], state=UserLang.lang)
async def lang_user_callback(call: types.CallbackQuery, state: FSMContext):
    lang = call.data
    if databs.get_user(call.from_user.id) is None:
        databs.add_user(call.from_user.id, lang)
        if lang == 'uz':
            await call.message.answer("Bo‘limni tanlang:", reply_markup=keyboard_uz)
        else:
            await call.message.answer("Выберите раздел:", reply_markup=keyboard_ru)
        await call.answer(cache_time=60)
        await call.message.delete()
        await state.finish()
    else:
        databs.update_user(call.from_user.id, lang)
        lang=databs.get_user(call.from_user.id)['lang']
        if lang == 'uz':
            await call.message.answer("Bo‘limni tanlang:", reply_markup=keyboard_uz)
        else:
            await call.message.answer("Выберите раздел:", reply_markup=keyboard_ru)
        await call.answer(cache_time=60)
        await call.message.delete()
        await state.finish()


# @dp.message_handler(commands='set_lang', state=None)
# async def update_lang(message: types.Message):
#     await message.answer(
#         text="O'zgartirishni xohlagan tilizni tanlang!!!",
#         reply_markup=keyboard
#     )
#     await LanguagesUpdate.up_lang.set()
#
# @dp.callback_query_handler(lambda c: c.data in ['uz', 'ru'], state=LanguagesUpdate.up_lang)
# async def update_lang_callback(call: types.CallbackQuery, state: FSMContext):
#     lang = call.data
#     if databs.get_user(call.from_user.id):
#         databs.update_user(call.from_user.id, lang)
#         await call.answer("Til muvaqqaiy sozlandi o'zgartirildi")
#         await call.answer(cache_time=60)
#         await call.message.delete()
#
#         await state.finish()
#     else:
#         await bot.send_message(call.from_user.id,
#                                text="Till allaqochon sozlangan")
#         await call.answer(cache_time=60)
#         await call.message.delete()
#         await state.finish()




