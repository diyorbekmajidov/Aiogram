from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.inline.callback_data import course_callback
from keyboards.default.startMenuKeyboard import keyboard_ru, keyboard_uz,keyboard_en

@dp.message_handler(text=['📢 Siznig kurslaringiz','📢 Ваши курсы:','📢 Your courses'])
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
    elif  databs.get_user(message.from_user.id)['lang']=="en":
        data=databs.get_user_course(message.from_user.id)
        text=''
        if data is not None:
            for i in data:
                text +=f"\n {data.index(i)+1}.{i['course']}"
            await message.answer(
            text=f"List of your courses:\n{text}\n\n"
            f"If the administrator has not contacted you, please re-register for the course!!!"
            ,
            )
        else:
            await message.answer('<b>You are not yet registered for our courses!!!</b>')
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


