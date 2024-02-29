from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.default.startMenuKeyboard import location_keyboard_uz, location_keyboard_ru,location_keyboard_en

@dp.message_handler(text=["📍Filialni tanlang:", "📍Выберите филиал:","📍Choose a branch:"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="Filialni tanlang:",
            reply_markup=location_keyboard_uz
        )
    elif  databs.get_user(message.from_user.id)['lang'] == "en":
        await message.answer(
            text="Filialni tanlang:",
            reply_markup=location_keyboard_en
        )
    else:
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=location_keyboard_ru
        )


@dp.message_handler(text=["Yagona daricha", "Единое окно","A single window"])
async def send_location(message: types.Message):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="Premium Education uquv markazi\n📍 Davlat xizmatlar markazi\n🕓 7:30 - 19:30\n✅ Wi-Fi\n✅ Kaworking zone",
        )
        await bot.send_location(message.chat.id, latitude=39.647000, longitude=66.933333)
    elif  databs.get_user(message.from_user.id)['lang'] == 'en':
        await message.answer(
            text="Premium Education training center\n📍 State services center\n🕓 7:30 - 19:30\n✅ Wi-Fi\n✅ Kaworking zone",
        )
        await bot.send_location(message.chat.id, latitude=39.647000, longitude=66.933333)
    else:
        await message.answer(
            text="Учебный центр Премиум Образования\n📍Центр государственных услуг\n🕓 7:30 - 19:30\n ✅ Wi-Fi\n ✅ Зона Kaworking",
        )
        await bot.send_location(message.chat.id, latitude=39.647000, longitude=66.933333)
    

    
@dp.message_handler(text=["Школа 37", "37-maktab",'School 37'])
async def send_location(message: types.Message):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="Premium School uquv markazi\n📍 Amir Temur ko’chasi, 141-uy\n🕓 7:30 - 19:30\n✅ Wi-Fi\n✅ Kaworking zone",
        )
        await bot.send_location(message.chat.id, latitude=39.65369017615916, longitude=66.95189418116307)
    elif databs.get_user(message.from_user.id)['lang'] == "en":
        await message.answer(
            text="Premium School training center\n📍 Amir Temur Street, 141\n🕓 7:30 - 19:30\n✅ Wi-Fi\n✅ Kaworking zone",
        )
        await bot.send_location(message.chat.id, latitude=39.65369017615916, longitude=66.95189418116307)
    else:
        await message.answer(
            text="Образовательный центр Premium School\n📍улица Амира Темура, 141\n🕓 7:30 - 19:30\n ✅ Wi-Fi\n ✅ Зона Kaworking",
        )
        await bot.send_location(message.chat.id, latitude=39.65369017615916, longitude=66.95189418116307)