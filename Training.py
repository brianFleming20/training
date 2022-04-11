'''
Creats a training event
'''
from datetime import datetime
import Documents
import DataStore
import User

DOC = Documents
DS = DataStore.data_store()
UR = User


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
        return date



    def change_name(self,old_name,new_name):
        USER = UR.User
        for user,data in self.get_all_users().items():
            if user == old_name:
                print(f"found user {user}")
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
            print(user_set)
            DS.dump_users(user_set)
        else:
            return False
