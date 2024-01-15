from  aiogram.dispatcher.filters.state import State, StatesGroup


class LanguagesUpdate(StatesGroup):
    up_lang = State()