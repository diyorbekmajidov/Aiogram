from aiogram import types
from keyboards.default.adminKeyboard import admin_kurs,post_true_or_false
from aiogram.dispatcher import FSMContext
from states.post_state import PostStates
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

@dp.message_handler(text='Kurslar Statistika')
async def Kurs_Statistika(message:types.Message):
    data = databs.get_user_all()
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
    await message.answer(f'{t}')

@dp.message_handler(text='Post yaratish')
async def Kurs_Statistika(message:types.Message,state:None):
    await message.answer('Qaysi turdagi xabar yuborishni hohlasangiz Ushani yuboring!!!', )
    await PostStates.post.set()

@dp.message_handler(text="🛠 Admin qushish")
async def Addto_admin(message:types.Message):
    await message.answer('Admin qushish uchun uning chat_id raqamini yuboring')
    await Add_AdminStates.admin.set()

@dp.message_handler(state=Add_AdminStates.admin)
async def add_admin(message: types.Message, state:FSMContext):
    try:
        admin = message.text
        user = databs.get_user(int(message.text))
        print(user)
        if user is not None:
            print(33)
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

        await message.reply("post qabul qilindi\n uni yuborish holasangiz ha tugmasini bosing akis holda yuq") 
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
                await bot.send_photo(user['chat_id'], post, caption)
            await state.finish()
            await message.answer('admin page', reply_markup=admin_kurs)
        elif type=='video':
            caption=data['caption']
            for user in get_userdata:
                await bot.send_video(user['chat_id'], post, caption)
            await state.finish()
            await message.answer('admin page', reply_markup=admin_kurs)
        elif type=='poll':
            options = data['options']
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
