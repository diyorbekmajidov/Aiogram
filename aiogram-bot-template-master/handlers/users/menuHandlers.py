from aiogram import types
from loader import dp, bot
from keyboards.default.startMenuKeyboard import settings_keyboard_uz, settings_keyboard_ru, keyboard_ru, keyboard_uz
from aiogram.dispatcher import FSMContext
from states.userlang_update import LanguagesUpdate
from keyboards.inline.langkeyboard import keyboard

from .start import databs

@dp.message_handler(text=["⚙️ Texnik yordam", "⚙️ Техническая поддержка:"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=settings_keyboard_uz
        )
        # await message.delete()
    else:
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=settings_keyboard_ru
        )
        # await message.delete()

@dp.message_handler(text=["⚙️ tillni almashtirish", "⚙️ изменение языка"], state=None)
async def update_lang(message: types.Message):
    # await message.delete()
    await message.answer(
            text="O'zgartirishni xohlagan tilizni tanlang!!!",
            reply_markup=keyboard
        )
    await LanguagesUpdate.up_lang.set()

@dp.callback_query_handler(lambda c: c.data in ['uz', 'ru'], state=LanguagesUpdate.up_lang)
async def update_lang_callback(call: types.CallbackQuery, state: FSMContext):
    lang = call.data
    databs.update_user(call.from_user.id, lang)
    lang=databs.get_user(call.from_user.id)['lang']
    if lang == 'uz':
        await call.message.answer("Bo‘limni tanlang:", reply_markup=keyboard_uz)
    else:
        await call.message.answer("Выберите раздел:", reply_markup=keyboard_ru)
    await call.answer(cache_time=60)
    # await call.message.delete()
    await state.finish()

@dp.message_handler(text=["⬅️ Orqaga", "⬅️ Назад"])
async def back_menu(message: types.Message):
    user_info = databs.get_user(message.from_user.id)['lang']
    if user_info=='uz':
        await message.answer("Siz bosh  sahifaga qaytdingiz.", reply_markup=keyboard_uz)
        # await message.delete()
    else:
        await message.answer("Вы вернулись на домашнюю страницу.", reply_markup=keyboard_ru)
        # await message.delete()
