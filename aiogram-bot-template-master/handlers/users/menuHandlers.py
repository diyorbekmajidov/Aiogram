from aiogram import types
from loader import dp, bot
from keyboards.default.startMenuKeyboard import settings_keyboard_uz, settings_keyboard_ru, keyboard_ru, keyboard_uz
from aiogram.dispatcher import FSMContext
from states.userlang_update import LanguagesUpdate
from keyboards.inline.langkeyboard import keyboard
import tracemalloc
tracemalloc.start()

from .start import databs

@dp.message_handler(text=["⚙️ Texnik yordam", "⚙️ Техническая поддержка"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=settings_keyboard_uz
        )
    else:
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=settings_keyboard_ru
        )

@dp.message_handler(text=["📍Manzil", "📍Адрес"])
async def send_location(message: types.Message):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="Najot talim uquv markazi\n📍 76 Narpayskaya ko'chasi\n🕓 10:00 - 21:50\n✅ Wi-Fi\n✅ Kaworking zone",
            reply_markup=settings_keyboard_uz
        )
        await bot.send_location(message.chat.id, latitude=41.3136, longitude=69.2823)

    else:
        await message.answer(
            text="Образовательный центр Наджот Талим\n📍ул. Нарпайская, 76\n🕓 10:00 - 21:50\n ✅ Wi-Fi\n ✅ Зона Kaworking",
            reply_markup=settings_keyboard_ru
        )
        await bot.send_location(message.chat.id, latitude=41.3136, longitude=69.2823)

@dp.message_handler(text=["⚙️ tillni almashtirish", "⚙️ изменение языка"], state=None)
async def update_lang(message: types.Message):
    await message.answer(
            text="O'zgartirishni xohlagan tilizni tanlang!!!",
            reply_markup=keyboard
        )
    await LanguagesUpdate.up_lang.set()

@dp.callback_query_handler(lambda c: c.data in ['uz', 'ru'], state=LanguagesUpdate.up_lang)
async def update_lang_callback(call: types.CallbackQuery, state: FSMContext):
    lang = call.data
    if databs.get_user(call.from_user.id):
        databs.update_user(call.from_user.id, lang)
        await call.answer("Til muvaqqaiy sozlandi o'zgartirildi")
        await call.answer(cache_time=60)
        await call.message.delete()

@dp.message_handler(text=["⬅️ Orqaga", "⬅️ Назад"])
async def back_menu(message: types.Message):
    user_info = databs.get_user(message.from_user.id)['lang']
    if user_info=='uz':
        await message.answer("Siz avvalgi sahifaga qaytdingiz.", reply_markup=keyboard_uz)
    else:
        message.answer("Choose the section:\n\n", reply_markup=keyboard_ru)
