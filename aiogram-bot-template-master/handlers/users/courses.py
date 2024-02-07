from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.inline.callback_data import course_callback
from keyboards.default.startMenuKeyboard import keyboard_ru, keyboard_uz

@dp.message_handler(text=['📢 Siznig kurslaringiz','📢 Ваши курсы:'])
async def cansel_course(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        data=databs.get_user_course(message.from_user.id)
        text=''
        if data is not None:
            for i in data:
                text +=f"\n {data.index(i)+1}.{i['course']}"
            await message.answer(
            text=f"<b>Sizning kurslaringiz ruyhati</b>:{text}\n\n"
            f"Agar admin siz bilan bog'lanmagan bo'lsa, kursdan qayta ro'yxatdan o'ting!!!"
            )
        else:
            await message.answer("<b>Siz hali bizning kurslarimizga ro'yxatdan o'tmagansiz!!!</b>")
    else:
        data=databs.get_user_course(message.from_user.id)
        text=''
        if data is not None:
            for i in data:
                text +=f"\n {data.index(i)+1}.{i['course']}"
            await message.answer(
            text=f"Список ваших курсов:\n{text}\n\n"
            f"Если администратор с вами не связался, пожалуйста, перезапишитесь на курс!!!"
            ,
            )
        else:
            await message.answer('<b>Вы еще не зарегистрированы на наши курсы!!!</b>')


@dp.callback_query_handler(course_callback.filter(item_name=['cancel']))
async def cansel_menu(call: types.CallbackQuery):
    if databs.get_user(call.from_user.id)['lang'] == "uz":
        await call.message.answer(
            text="Kurslar ruyhati",
            reply_markup=keyboard_uz)
        await call.answer(cache_time=20)
    else:
        await call.message.answer(
            text="Список курсов",
            reply_markup=keyboard_ru
        )
        await call.answer(cache_time=20)