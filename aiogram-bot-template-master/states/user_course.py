from aiogram.dispatcher.filters.state import State, StatesGroup

class Userdata(StatesGroup):
    courseName = State()
    phonenumber=State()
    fullname=State()