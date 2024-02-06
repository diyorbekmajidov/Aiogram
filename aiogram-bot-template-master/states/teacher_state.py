from aiogram.dispatcher.filters.state import State, StatesGroup

class TeacherState(StatesGroup):
    name_teacher = State()
    subject_teacher = State()