'''
Creats a training event
'''
from datetime import datetime
import Documents
import DataStore


DOC = Documents
DS = DataStore


class Training():

   

    def init(self):
        self.document = DOC.Document()
        self.trainer = ""
        self.notes = []
        self.expires_on = None
        self.review_date = None
        self.training_event = []



    def get_now_time(self):
        presentime = datetime.now()
        date = presentime.strftime('%Y-%m-%d')
        print(f"Date now is {date}")
        return date


    def get_expire_date(self):
        pass



    def add_training_note(self,user):
        pass



    def get_document(self):

        return DS.data_store.get_all_documents(self)


    def write_documents(self, documents):
        DS.data_store.write_documents(documents)


    def get_all_users(self):
        users = DS.data_store.read_users(self)
       
        return users


    def get_user(self, username):
        for user,data in self.get_all_users().items():
            if user == username:
                return data



    def add_training_record(self,doc_obj,user_obj,train_date,exp_date,note):
        pass


    def trained_on(self, doc, user):
        pass


    def docs_trained_on(self,user):
        pass



    def who_is_trainer(self):
        result = []
        for usr,value in self.get_all_users().items():
            for item,i_val in value.items():
                if item == "trainer":
                    result.insert(0,i_val)
        return list(dict.fromkeys(result))


    def user_expire_date(self, date):
        pass



    def document_expire_date(self, date):
        pass



    def search_users(self, search):
        result = []
        for usr,value in self.get_all_users().items():
            for item,i_val in value.items():
                if i_val == search:
                    result.insert(0,usr)
        return list(dict.fromkeys(result))



    def get_all_trainers(self):
        return self.search_users(True) 
            



    def get_all_at_level(self, level):
        return self.search_users(level)