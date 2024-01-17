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
        
    def add_cource_user(self, chat_id, username,course_name):
        self.user_cource.insertDocument({
            'chat_id': chat_id,
            'username': username,
            'course_name':course_name
            }, doc_id=chat_id)
        
    def get_cource_user(self, chat_id):
        return self.user_cource.get(doc_id=chat_id)


db = DB('db.json')