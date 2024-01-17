from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.default.startMenuKeyboard import location_keyboard_uz, location_keyboard_ru

@dp.message_handler(text=["📍Filialni tanlang:", "📍Выберите филиал:"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.delete()
        await message.answer(
            text="Filialni tanlang:",
            reply_markup=location_keyboard_uz
        )
        await message.answer(cache_time=60)
    else:
        await message.delete()
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=location_keyboard_ru
        )
        await message.answer(cache_time=60)


@dp.message_handler(text=["Yagona daricha", "Единое окно"])
async def send_location(message: types.Message):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.delete()
        await message.answer(
            text="Najot talim uquv markazi\n📍 76 Narpayskaya ko'chasi\n🕓 10:00 - 21:50\n✅ Wi-Fi\n✅ Kaworking zone",
            # reply_markup=settings_keyboard_uz
        )
        await message.answer(cache_time=60)
        await bot.send_location(message.chat.id, latitude=41.3136, longitude=69.2823)
    else:
        await message.delete()
        await message.answer(
            text="Образовательный центр Наджот Талим\n📍ул. Нарпайская, 76\n🕓 10:00 - 21:50\n ✅ Wi-Fi\n ✅ Зона Kaworking",
            # reply_markup=settings_keyboard_ru
        )
        await bot.send_location(message.chat.id, latitude=41.3136, longitude=69.2823)
        await message.answer(cache_time=60)

    
@dp.message_handler(text=["37 перед школой", "37-maktab oldida"])
async def send_location(message: types.Message):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="Najot talim uquv markazi\n📍 76 Narpayskaya ko'chasi\n🕓 10:00 - 21:50\n✅ Wi-Fi\n✅ Kaworking zone",
            # reply_markup=settings_keyboard_uz
        )
        await bot.send_location(message.chat.id, latitude=41.3136, longitude=69.2823)
    else:
        await message.answer(
            text="Образовательный центр Наджот Талим\n📍ул. Нарпайская, 76\n🕓 10:00 - 21:50\n ✅ Wi-Fi\n ✅ Зона Kaworking",
            # reply_markup=settings_keyboard_ru
        )
        await bot.send_location(message.chat.id, latitude=41.3136, longitude=69.2823)