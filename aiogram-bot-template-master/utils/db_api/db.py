from tinydb import TinyDB, Query
from tinydb.database import Document

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()
        self.user = self.db.table('user_lang')
        self.user_cource = self.db.table('user_cources') 

    def add_user(self, chat_id, lang=None):
        self.user.insert(Document({
            'chat_id': chat_id,
            'lang': lang
            }, doc_id=chat_id))

    def get_user(self, chat_id):
        return self.user.get(doc_id=chat_id)

    def update_user(self, chat_id, lang=None,):
        if lang:
            self.user.update({'lang': lang}, doc_ids=[chat_id])
        
    def add_course_user(self, chat_id, username, courses, phonenumber):
        self.user_cource.insert(Document({
            'chat_id': chat_id,
            'username': username,
            'courses': courses,  # Store courses as a list
            'phonenumber': phonenumber
        }, doc_id=chat_id))

    def get_user_courses(self, chat_id):
        user_info = self.user_cource.get(doc_id=chat_id)
        return user_info.get('courses', []) if user_info else []
    
    def add_course_to_user(self, chat_id, course_name):
        user_info = self.user_cource.get(doc_id=chat_id)

        if user_info:
            courses = user_info.get('courses', [])
            if course_name not in courses:
                courses.append(course_name)
                self.user_cource.update({'courses': courses}, doc_ids=[chat_id])
        else:
            pass


db = DB('db.json')