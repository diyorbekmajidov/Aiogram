from aiogram import types
from keyboards.default.adminKeyboard import admin_kurs,post_true_or_false,back_admin_keyboard
from aiogram.dispatcher import FSMContext
from states.post_state import PostStates
from states.free_lesson import FreeLesson_State
from states.add_to_admin_state import Add_AdminStates
from .start import databs
import logging
import os

# Add this at the beginning of your code
logging.basicConfig(level=logging.DEBUG)

from loader import dp, bot
from .start import databs
from data.config import ADMINS

@dp.message_handler(commands="admin")
async def admin_page(message: types.Message):
    chat_id=message.from_user.id
    if str(chat_id) in ADMINS or str(databs.get_user(chat_id)['admin'])==str(chat_id):
        await message.answer('admin page', reply_markup=admin_kurs)
    else:
        await message.answer('Siz xato buyruq yubordingiz')


@dp.message_handler(text='Bepul darslar qushish', state=None)
async def handler1(message: types.Message):
    await message.answer("Qushmoqchi bulgan kursingi nomini yozib yuboring <b>uzbek tilida</b>",
                         reply_markup=back_admin_keyboard)
    await FreeLesson_State.name_uz.set()

@dp.message_handler(text='◀️ Orqaga',state='*')
async def back_admin(message:types.Message,state:FSMContext):
    chat_id=message.from_user.id
    await message.answer('admin page', reply_markup=admin_kurs)
    await state.finish()

@dp.message_handler(state=FreeLesson_State.name_uz)
async def handler2(message:types.Message, state:FSMContext):
    name_uz = message.text
    await state.update_data({'name_uz':name_uz})
    await message.answer("Qushmoqchi bulgan kursingi nomini yozib yuboring <b>rus </b>tilida")
    await FreeLesson_State.name_ru.set()

@dp.message_handler(state=FreeLesson_State.name_ru)
async def check_name_ru(message: types.Message, state: FSMContext):
    name_ru = message.text
    await state.update_data({'name_ru':name_ru})
    await message.answer("Qushmoqchi bulgan kursingi <b>link</b> yuboring")
    await FreeLesson_State.link.set()

@dp.message_handler(state=FreeLesson_State.link)
async def check_link(message: types.Message, state:FSMContext):
    link = message.text
    await state.update_data({'link':link})
    data = await state.get_data()
    name_uz=data['name_uz']
    name_ru=data['name_ru']
    databs.add_free_lesson(name_ru=name_ru,name_uz=name_ru,link=link)
    await message.answer('Kurs mufaqatli qushildi')
    await state.finish()


@dp.message_handler(text='Kurslar Statistika')
async def Kurs_Statistika(message:types.Message):
    data = databs.get_user_all()
    user = len(databs.get_alluser())
    course_data={
        'SAT':0, 
        'Umumiy matematika':0,
        'Bolalar uchun matematika':0,
        'Ingliz tili':0, 
        'DTM':0
    }
    for i in data:
        course_data[i['course']]+=1
    text = course_data.items()
    t=''
    k=1
    for j in text:
        t+=f'{k}. {j[0]} : {j[1]}\n'
        k+= 1
    await message.answer(f'Umumiy foydalanuvchilar soni: {user}\n{t}')

@dp.message_handler(text='Post yaratish')
async def Kurs_Statistika(message:types.Message,state:None):
    await message.answer('Botda 4 turdagi habar yubora olasiz bular:\n'
                         '<b>1.Text\n2.Rasim  (jpg)\n3.Video (mp4)\n4.Poll</b>\n'
                         'Agar siz ushbu turdagi xabarni yuborsangiz, bot barcha foydalanuvchilarga yuboriladi'
                         ,parse_mode=types.ParseMode.HTML,
                         reply_markup=back_admin_keyboard)
    await PostStates.post.set()

@dp.message_handler(text="🛠 Admin qushish")
async def Addto_admin(message:types.Message):
    await message.answer('Admin qushish uchun uning chat_id raqamini yuboring'
                         f"chat_id raqamini @MissRose_bot kirib\n star bosib /id buyruq orqali olishingiz mumkun va chat_id botga yuboring",
                         reply_markup=back_admin_keyboard
                         )
    await Add_AdminStates.admin.set()

@dp.message_handler(state=Add_AdminStates.admin)
async def add_admin(message: types.Message, state:FSMContext):
    try:
        admin = message.text
        user = databs.get_user(int(message.text))
        print(user)
        if user is not None:
            databs.update_user(int(user['chat_id']),admin=admin)
            print(databs.get_user(int(message.text)))
            await message.answer("Admin mufaqliy qushildi!")
            await state.finish()
    except:
        await message.answer('Bunday  foydalanuvchi topilmadi!')
        await state.finish()


@dp.message_handler(content_types=types.ContentType.ANY, state=PostStates.post)
async def get_file_id_p(message: types.Message, state: FSMContext):
    if message.photo:
        await state.update_data({"post": message.photo[-1].file_id, "caption":message.caption, "type":"photo"})

        await message.reply("post qabul qilindi\n uni yuborish holasangiz <b>ha</b> tugmasini bosing akis holda <b>yuq<b>") 
        await message.answer("sd", reply_markup=post_true_or_false)

        await PostStates.save_post.set()

    elif message.video:
        await state.update_data({"post": message.video.file_id,"caption":message.caption, "type":"video"})
        await message.reply("post qabul qilindi\n uni yuborish holasangiz ha tugmasini bosing akis holda yuq", reply_markup=post_true_or_false)
        await PostStates.save_post.set()

    elif message.poll:
        question = message.poll.question
        options = [x.text for x in message.poll.options]
        await state.update_data({"post":question ,"options":options, "type":"poll"})
        await message.reply("post qabul qilindi\n uni yuborish holasangiz ha tugmasini bosing akis holda yuq", reply_markup=post_true_or_false)
        await PostStates.save_post.set()
    else:
        await state.update_data({"post": message.text, "type":"text"})
        await message.reply("post qabul qilindi\n uni yuborish holasangiz ha tugmasini bosing akis holda yuq", reply_markup=post_true_or_false)
        await PostStates.save_post.set()

@dp.message_handler(text=['Ha','Yuq'], state=PostStates.save_post)
async def get_file_id_save_post(message:types.Message,state: FSMContext):
    if message.text=='Ha':
        data = await state.get_data()
        type = data['type']
        post = data['post']
        get_userdata= databs.get_alluser()
        if type=='photo':
            caption=data['caption']
            for user in get_userdata:
                await bot.send_photo(user['chat_id'], post, caption=caption)
            await state.finish()
            await message.answer('admin page', reply_markup=admin_kurs)
        elif type=='video':
            caption=data['caption']
            for user in get_userdata:
                await bot.send_video(user['chat_id'], post, caption=caption)
            await state.finish()
            await message.answer('admin page', reply_markup=admin_kurs)
        elif type=='poll':
            options = data['options']
            for user in get_userdata:
                await bot.send_poll(message.from_user.id, post, options)
            await state.finish()
            await message.answer('admin page', reply_markup=admin_kurs)
        elif type == 'text':
            for user in get_userdata:
                await bot.send_message(user['chat_id'], post)
            await state.finish()
            await message.answer('admin page', reply_markup=admin_kurs)  
    else:
        await message.answer('Post bekor qilindi.')
        await message.answer('admin page', reply_markup=admin_kurs)
        await state.finish()


        