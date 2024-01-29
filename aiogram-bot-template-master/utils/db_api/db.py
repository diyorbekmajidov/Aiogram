from tinydb import TinyDB, Query
from tinydb.database import Document
import uuid

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()
        self.user = self.db.table('user_lang')
        self.user_cource = self.db.table('user_cources') 

    def add_user(self, chat_id, lang=None, admin=None):
        self.user.insert(Document({
            'chat_id': chat_id,
            'lang': lang,
            'admin':admin
            }, doc_id=chat_id))

    def get_user(self, chat_id):
        return self.user.get(doc_id=chat_id)
    
    def get_alluser(self):
        return self.user.all()

    def update_user(self, chat_id, lang=None, admin=None):
        if lang:
            self.user.update({'lang': lang,'admin':admin}, doc_ids=[chat_id])
            
    def add_course_user(self, chat_id, username, courses, phonenumber):    
        doc_id = f"{chat_id}_{courses}"

        # Check if doc_id already exists in the table
        if not self.user_cource.contains(self.query.doc_id == doc_id):
            self.user_cource.insert({
                'doc_id': doc_id,
                'chat_id': chat_id,
                'username': username,
                'course': courses,
                'phonenumber': phonenumber
            })

    def update_user_course(self, chat_id, new_courses, username):
        doc_id = f"{chat_id}_{new_courses}"

        # Check if doc_id already exists in the table
        if self.user_cource.contains(self.query.doc_id == doc_id):
            # Update the existing document
            self.user_cource.update({'course': new_courses,'username':username}, self.query.doc_id == doc_id)
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