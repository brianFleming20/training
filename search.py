'''
Search the datbase and return the selected items

'''
import DataStore
import User
import Training

DS = DataStore.data_store()
USER = User.User()
TR = Training.Training()



class search():

    def __init__(self):
        self.username = ""
        self.password = ""
        self.level = 0
        self.trainer = ""
        self.is_trainer = False
        self.documents = []
        self.doc_name = ""
        self.issue_number = 0.0
        self.reference_number = ""


    def get_user_documents(self,name):
        selected = None
        users = DS.read_user()
        for user in users:
            if user.name == name:
                selected = user.documents
        return selected




    def get_document(self,doc_name):
        selected = None
        for doc in self.get_user_documents():
            if doc.name == doc_name:
                selected = doc
            else:
                selected = False
        return selected



    def add_user_to_store(self, user):
        DS.write_user(user)