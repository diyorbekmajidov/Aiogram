from aiogram import types
from loader import dp, bot
from keyboards.default.startMenuKeyboard import settings_keyboard_uz, settings_keyboard_ru, settings_keyboard_en,keyboard_ru, keyboard_uz,keyboard_en
from aiogram.dispatcher import FSMContext
from states.userlang_update import LanguagesUpdate
from keyboards.inline.langkeyboard import keyboard,Social_Networks_uz,Social_Networks_ru,Social_Networks_en

from .start import databs

@dp.message_handler(text=['Ijtimoiy tarmoqlar','Социальные сети','Social networks'])
async def Social(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="Bizning ijtimoiy tarmoqlarimiz", 
            reply_markup=Social_Networks_uz
            )
    elif  databs.get_user(message.from_user.id)['lang'] == 'en':
        await message.answer(
            text="Our social networks", 
            reply_markup=Social_Networks_en
            )
    else:
        await message.answer(
            text="Наши социальные сети",
            reply_markup=Social_Networks_ru
        )

@dp.message_handler(text=["⚙️ Texnik yordam", "⚙️ Техническая поддержка:","⚙️ Technical support"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=settings_keyboard_uz
        )
    elif databs.get_user(message.from_user.id)['lang'] == "en":
        await message.answer(
            text="⚙️ Settings!!!",
            reply_markup=settings_keyboard_en
        )
    else:
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=settings_keyboard_ru
        )

@dp.message_handler(text=["⚙️ tillni almashtirish", "⚙️ изменение языка","⚙️ change language"], state=None)
async def update_lang(message: types.Message):
    await message.answer(
            text="O'zgartirishni xohlagan tilizni tanlang!!!",
            reply_markup=keyboard
        )
    await LanguagesUpdate.up_lang.set()

@dp.callback_query_handler(lambda c: c.data in ['uz', 'ru','en'], state=LanguagesUpdate.up_lang)
async def update_lang_callback(call: types.CallbackQuery, state: FSMContext):
    lang = call.data
    databs.update_user(call.from_user.id, lang)
    lang=databs.get_user(call.from_user.id)['lang']
    if lang == 'uz':
        await call.message.answer("Bo‘limni tanlang:", reply_markup=keyboard_uz)
    elif lang == 'en':
        await call.message.answer("Bo‘limni tanlang:", reply_markup=keyboard_en)
    else:
        await call.message.answer("Выберите раздел:", reply_markup=keyboard_ru)
    await call.answer(cache_time=60)
    # await call.message.delete()
    await state.finish()

@dp.message_handler(text=["⬅️ Orqaga", "⬅️ Назад","⬅️ Back"])
async def back_menu(message: types.Message):
    user_info = databs.get_user(message.from_user.id)['lang']
    if user_info=='uz':
        await message.answer("Siz bosh  sahifaga qaytdingiz.", reply_markup=keyboard_uz)
    elif user_info=='en':
        await message.answer("You have returned to the home page.", reply_markup=keyboard_en)
    else:
        await message.answer("Вы вернулись на домашнюю страницу.", reply_markup=keyboard_ru)
