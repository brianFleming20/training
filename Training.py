'''
Creats a training event
'''
from datetime import datetime
from tkinter import messagebox as mb
import DataStore
import User
import Login
import AccessDataBase

DS = DataStore.data_store()
UR = User
LGI = Login



class Training:

    def get_date_now(self):
        presentime = datetime.now()
        date = presentime.strftime('%d-%m-%y')
        return date

    def get_review_date(self):
        dt = datetime.now()
        dt = dt.replace(year=dt.year + 1)
        return dt.strftime('%d-%m-%y')

    # def check_expire_dates(self, name):
    #     for event in training_events:
    #         print(event)

    def get_documents(self):
        docs = DS.get_all_documents()
        return docs

    def get_a_document(self, doc_ref):
        documents = self.get_documents()
        doc_items = None
        for doc, item in documents.items():
            if doc_ref == doc:
                doc_items = item
        return doc_items

    def get_all_users(self):
        users = DS.read_users_data()
        return users

    def get_user(self, username):
        for user, data in self.get_all_users().items():
            if user == username:
                return data

    def get_logged_in_user(self):
        return LGI.LI_user

    def save_user(self, user):
        DS.write_user(user)

    def add_training_record(self, training_obj):
        DS.add_training_record(training_obj)

    def register_trained(self, document, user):
        training = None
        all_docs = self.get_documents()
        training_records = self.get_all_training()
        for doc, item in all_docs.items():
            if doc == document:
                training = CreateTraining(username=user, doc_ref=doc, doc_name=item['name'],
                                          train_date=self.get_date_now(), review=self.get_review_date(),
                                          logger="System")
            else:
                print("record failed")
        if user in training_records:
            self.add_to_user_training(training)
        else:
            self.add_training_record(training)

    def add_to_user_training(self, training_obj):
        DS.add_training_to_user(training_obj)

    def who_is_trainer(self):
        result = []
        for usr, value in self.get_all_users().items():
            for item, i_val in value.items():
                if item == "trainer":
                    result.insert(0, i_val)
        return list(dict.fromkeys(result))

    def get_all_training(self):
        return DS.get_all_training()

    def add_document(self, doc):
        DS.write_document(doc)

    def remove_document(self, ref):
        documents = self.get_documents()

        if ref in documents.keys():
            documents.pop(ref)
            DS.dump_documents(documents)
            return True
        else:
            mb.showerror(title="Reference Error", message="The old reference number not found.")
            return False

    def search_users(self, search):
        result = []
        for usr, value in self.get_all_users().items():
            for item, i_val in value.items():
                if i_val == search:
                    result.insert(0, usr)
        return list(dict.fromkeys(result))

    def get_all_trainers(self):
        return self.search_users(True)

    def get_all_at_level(self, level):
        return self.search_users(level)

    def delete_user(self, name):
        users = self.get_all_users()
        if name in users.keys():
            user_set = self.get_all_users()
            user_set.pop(name)

            DS.dump_users(user_set)
        else:
            return False

    def overwrite_docs(self, docs):
        DS.dump_documents(docs)

    def update_document(self, doc):
        self.add_document(doc)

    def get_blank_user(self):
        return UR.User(name="", password="")

    def update_password(self,name,password):
        LGI.Login.save_data(name,password)

class CreateTraining():

    def __init__(self, username="", doc_name="", doc_ref="", train_date="", review="", logger="", note=""):
        self.notes = note
        self.trained_on = train_date
        self.review_date = review
        self.username = username
        self.document_ref = doc_ref
        self.document_name = doc_name
        self.logger = logger
