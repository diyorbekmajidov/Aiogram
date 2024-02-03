from aiogram.dispatcher.filters.state import State, StatesGroup

class FreeLesson_State(StatesGroup):
    name_uz=State()
    name_ru=State()
    link = State()