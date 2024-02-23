from tinydb import TinyDB, Query, where
from tinydb.database import Document
import uuid

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()
        self.user = self.db.table('user_lang')
        self.user_cource = self.db.table('user_cources') 
        self.free_lesson = self.db.table('free_lesson')
        self.teacher = self.db.table('teacher')

    def add_teacher(self, username, science):
        teacher={
            'username':username,
            "science":science
        }
        doc_id=self.teacher.insert(teacher)
        return doc_id
    
    def fillter_teacher(self, science):
        return self.teacher.search(where('science') == science)

    def add_user(self, chat_id, lang=None, admin=None):
        self.user.insert(Document({
            'chat_id': chat_id,
            'lang': lang,
            'admin':admin
            }, doc_id=chat_id))
        
    def add_free_lesson(self, name_uz, name_ru,name_en, link):
        new_lesson = {
            'name_uz': name_uz,
            'name_en': name_en,
            'name_ru': name_ru,
            'link': link
        }

        # insert metodidan foydalanib, yangi hujjatni qo'shish
        doc_id = self.free_lesson.insert(new_lesson)
        return doc_id
    
    def get_free_lesson(self):  
        return self.free_lesson.all()

    def get_user(self, chat_id):
        return self.user.get(doc_id=chat_id)
    
    def get_alluser(self):
        return self.user.all()

    def update_user(self, chat_id, lang=None, admin=None):
        if lang:
            self.user.update({'lang': lang}, doc_ids=[chat_id])
        if admin:
            self.user.update({'admin':admin}, doc_ids=[chat_id])
            
    def add_course_user(self, chat_id, username, courses, phonenumber,teacher):    
        doc_id = f"{chat_id}_{courses}"

        # Check if doc_id already exists in the table
        if not self.user_cource.contains(self.query.doc_id == doc_id):
            self.user_cource.insert({
                'doc_id': doc_id,
                'chat_id': chat_id,
                'username': username,
                'course': courses,
                'phonenumber': phonenumber,
                'teacher':teacher
            })

    def update_user_course(self, chat_id, new_courses, username,teacher):
        doc_id = f"{chat_id}_{new_courses}"

        # Check if doc_id already exists in the table
        if self.user_cource.contains(self.query.doc_id == doc_id):
            # Update the existing document
            self.user_cource.update({'course': new_courses,'username':username,'teacher':teacher}, self.query.doc_id == doc_id)
        else:
            # Handle the case when the document does not exist
            print(f"Document with doc_id {doc_id} does not exist.")

    def get_user_course(self, chat_id):
        user_courses = self.user_cource.search(self.query.chat_id == chat_id)
        return user_courses
    
    def get_user_coursename(self,doc_id):
        user_coursename= self.user_cource.search(self.query.doc_id == doc_id)
        return user_coursename
    
    def get_user_all(self):
        all_users = self.user_cource.all()
        return all_users
    


db = DB('db.json')