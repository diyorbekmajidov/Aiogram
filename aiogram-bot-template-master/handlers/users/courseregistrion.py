from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.inline.callback_data import course_callback
from keyboards.inline.kurslarkeybord import coursesMenu, coursesMenu_ru,coursesMenu_en, keyboard
from keyboards.default.startMenuKeyboard import keyboard_ru, keyboard_uz,keyboard_en, back_botton_uz, back_botton_ru,back_botton_en
from states.user_course import Userdata
from data.config import ADMINS
from aiogram.dispatcher import FSMContext
async def send_course_list(message: types.Message, lang):
    if lang == "uz":
        await message.answer("Kursga yozilish uchun kurslardan birini tanlang va ma’lumotlarni botga kiriting.", reply_markup=types.ReplyKeyboardRemove())
        await message.answer(text="Kurslar ruyhati", reply_markup=coursesMenu)
    elif lang == "en":
        await message.answer("To enroll in a course, select one of the courses and enter the information in the bot.", reply_markup=types.ReplyKeyboardRemove())
        await message.answer(text="List of courses", reply_markup=coursesMenu_en)
    else:
        await message.answer("Чтобы записаться на курс, выберите один из курсов и введите информацию в бота.", reply_markup=types.ReplyKeyboardRemove())
        await message.answer(text="Список курсов", reply_markup=coursesMenu_ru)

@dp.message_handler(text=["Kurslarimiz", "Наши курсы", "Our courses"])
async def settings_bot(message: types.Message, state=None):
    lang = databs.get_user(message.from_user.id)['lang']
    await send_course_list(message, lang)
    await Userdata.courseName.set()

@dp.callback_query_handler(course_callback.filter(item_name=['cancel']),state='*')
async def cansel_menu(call: types.CallbackQuery, state: FSMContext):
    if databs.get_user(call.from_user.id)['lang'] == "uz":
        await call.message.answer(
            text="Kurslar ruyhati",
            reply_markup=keyboard_uz)
        await state.finish()
        await call.answer(cache_time=20)
    elif databs.get_user(call.from_user.id)['lang'] == "en":
        await call.message.answer(
            text="List of courses",
            reply_markup=keyboard_en)
        await call.answer(cache_time=20)
        await state.finish()
    else:
        await call.message.answer(
            text="Список курсов",
            reply_markup=keyboard_ru
        )
        await state.finish()
        await call.answer(cache_time=20)

@dp.callback_query_handler(course_callback.filter(item_name=['SAT', 'Umumiy matematika','Bolalar uchun matematika','Ingliz tili', 'DTM']), state=Userdata.courseName)
async def buying_course(call: types.CallbackQuery, state: FSMContext):
    if databs.get_user(call.from_user.id)['lang'] == 'uz':
        course = call.data
        await state.update_data(
            {"coursename": course}
        )
        await call.message.answer(
            f"Siz <b>{course.split(':')[1]}</b>  Kursini tanladingiz.\nRuyhatda utishni istasangiz \n<b>To'liq ismingizni kiriting </b>...", 
            reply_markup=back_botton_uz
            )
        await call.answer(cache_time=20)
        await Userdata.next()

    elif  databs.get_user(call.from_user.id)['lang'] == 'en':
        course = call.data
        await state.update_data(
            {"coursename": course}
        )
        await call.message.answer(
            f"You <b>{course.split(':')[1]}</b>  You have selected a course.\nIf you want to win on the list, \n<b>Enter your full name </b>...", 
            reply_markup=back_botton_en
            )
        await call.answer(cache_time=20)
        await Userdata.next()

    else:
        course = call.data
        lang={'SAT':'СИДЕЛ', 'Umumiy matematika':'Общая математика',
              'Bolalar uchun matematika':'Математика для детей',
              'Ingliz tili':'английский язык', 'DTM':'ДТМ'}
        await state.update_data(
            {"coursename": course}
        )
        course=course.split(':')[1]
        await call.message.answer(
            f"Ты <b>{lang[course]}</b> выбрали курс.\n Если хотите выиграть в списке\n <b>Введите свое полное имя</b>...")
        await call.answer(cache_time=20)
        await Userdata.next()


@dp.message_handler(text=['⬅Orqaga',"⬅Назад",'⬅Back'],state='*')
async def back_to_menu(msg:types.Message,state:FSMContext):
    if databs.get_user(msg.from_user.id)['lang'] == "uz":
        await msg.answer(
            text="Kurslar ruyhati",
            reply_markup=keyboard_uz)
        await state.finish()
    if  databs.get_user(msg.from_user.id)['lang'] == "en":
        await msg.answer(
            text="Kurslar ruyhati",
            reply_markup=keyboard_en)
        await state.finish()
    else:
        await msg.answer(
            text="Список курсов",
            reply_markup=keyboard_ru
        )
        await state.finish()


@dp.message_handler(state=Userdata.fullname)
async def answer_email(message:types.Message, state: FSMContext):
    user_data = await state.get_data()
    name = message.text
    await state.update_data(
            {"name": name}
        )
    course = user_data.get("coursename").split(':')[1]
    data = databs.fillter_teacher(course)
    t=''
    teacher_keyboard = types.InlineKeyboardMarkup(row_width=5)
    for i in data:
        t+=f"{data.index(i)+1}. {i['username']}\n"
        teacher_keyboard.insert(types.InlineKeyboardButton(
                text=f"{data.index(i)+1}",callback_data=i['username']))
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await  message.answer(f"O'qituvchini tanlang\n{t}",reply_markup=teacher_keyboard)
        await Userdata.next()
    elif  databs.get_user(message.from_user.id)['lang'] == 'en':
        await  message.answer(f"Choose a teacher\n{t}",reply_markup=teacher_keyboard)
        await Userdata.next()
    else:
        await  message.answer(f'Выбрать преподавателя\n{t}',reply_markup=teacher_keyboard)
        await Userdata.next()
@dp.callback_query_handler(state=Userdata.teacher)
async def teacher_info(call: types.CallbackQuery, state:FSMContext):
    subject = call.data
    await state.update_data(
            {"teacher": subject}
        )
    user = databs.get_user(call.from_user.id)
    if user['lang']=='uz':
        await call.message.answer("Telefon raqamini kiritish uchun tugmani bosing", reply_markup=keyboard)
        await Userdata.next()
    elif  user['lang']=='en':
        await call.message.answer("Click the button to enter the phone number", reply_markup=keyboard)
        await Userdata.next()
    else:
        await call.message.answer("Нажмите кнопку, чтобы ввести номер телефона", reply_markup=keyboard)
        await Userdata.next()
    

@dp.message_handler(content_types='contact', state=Userdata.phonenumber)
async def get_contact(message: types.Message,state: FSMContext):
    data = await state.get_data()
    username = data.get("name")
    courses = data.get("coursename")
    course = courses.split(':')[1]
    teacher = data.get('teacher')
    phonenumber = message.contact.phone_number
    chat_id = message.from_user.id
    if databs.get_user_coursename(f"{chat_id}_{course}") is not None:
        for admin in ADMINS:
            await dp.bot.send_message(admin, f"1.Ismi:{username}\n2.Kurs:{course}\n3.O'qtuvchi:{teacher}\n4.Telfon raqami:{phonenumber}")
        databs.update_user_course(chat_id, course,username,teacher)
    # else add to user on data base
    else:
        for admin in ADMINS:
            await dp.bot.send_message(admin, f"1.Ismi:{username}\n2.Kurs:{course}\n3.O'qtuvchi:{teacher}\n4.Telfon raqami:{phonenumber}")
        databs.add_course_user(chat_id,username,course,phonenumber,teacher)
    if databs.get_user(chat_id)['lang'] == "uz":
        await message.answer(
            f"Rahmat, <b>{username}</b>.\n"
            f"O'qtuvchi: {teacher}.\n"
            f"Sizning {phonenumber} raqamingizni qabul qildik.\nAdminmiz siz bilan bog'lanadi.",
            reply_markup=keyboard_uz)
        await state.finish()
    elif databs.get_user(chat_id)['lang'] == "en":
        await message.answer(
            f"Thank you, <b>{username}</b>.\n"
            f"Teacher: {teacher}.\n"
            f"We have received your {phonenumber}.\nOur admin will contact you.",
            reply_markup=keyboard_en)
        await state.finish()
    else :
        await message.answer(
            f"Спасибо, <b>{username}</b>.\n"
            f"Учитель: {teacher}.\n"
            f"Мы получили ваш {phonenumber}.\n Наш администратор свяжется c вами.",
            reply_markup=keyboard_ru
        )
        await state.finish()