'''
Creats a training event
'''
from datetime import datetime
from tkinter import messagebox as mb
import DataStore
import User


DS = DataStore.data_store()
UR = User

documents = []
users = []
training_event = []

class Training():


    def refresh_window(self):
        self.get_all_data()

    def get_now_time(self):
        presentime = datetime.now()
        date = presentime.strftime('%Y-%m-%d')
        return date



    def change_name(self,old_name,new_name):
        for user,data in self.get_all_users().items():
            if user == old_name:
                for item,item_data in data.items():
                    if item == "passwd":
                        passwd = item_data
                    if item == "level":
                        level = item_data
                    if  item == "trainer":
                        train = item_data
                    if item == "is_trainer":
                        trainer = item_data
                update = UR.User(new_name,passwd,level,train,trainer)
                DS.write_user(update)
                self.delete_user(user)


    def get_expire_date(self,name):
        pass



    def add_training_note(self,user):
        pass



    def get_documents(self):
        docs = DS.get_all_documents()
        if docs != None:
            return docs
        else:
            return False


    def write_document(self, document):
        DS.write_document(document)


    def get_all_users(self):
        users = DS.read_users_data()
        return users


    def get_user(self, username):
        for user,data in self.get_all_users().items():
            if user == username:
                return data
        

    def save_user(self,user):
        users.insert(0,user)
        DS.write_user(user)


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


    def expire_date_all_users(self, date):
        pass



    def document_expire_date(self, date):
        pass


    def get_all_training(self):
        pass


    def add_document(self,doc):
        documents.insert(0,doc)


    def get_local_docs(self):
        return documents


    def remove_document(self, doc_obj):
        for document in documents:
            print(document.reference_number)
            if doc_obj.reference_number == document.reference_number:
                documents.remove(document)
                self.overwrite_docs(documents)
                return True
            else:
                mb.showerror(title="Reference Error",message="The old reference number not found.")
                return False



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


    def delete_user(self,name):
        user_set = None
        users = self.get_all_users()
        if name in users.keys():
            user_set = users
            user_set.pop(name)
          
            DS.dump_users(user_set)
        else:
            return False

    def overwrite_docs(self,docs):
        DS.dump_documents(docs)


    def get_all_local_data(self):
        users = DS.read_users_data()
        docs = self.get_documents()
        training = self.get_all_training()





class CreateTraining():

    def init(self):
        self.notes = []
        self.expires_on = None
        self.review_date = None
