from aiogram.dispatcher.filters.state import State, StatesGroup

class PostStates(StatesGroup):
    post= State()
    save_post= State()