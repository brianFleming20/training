'''
Creates a user object for the system to use.
'''

import DataStore

DS = DataStore.data_store()


class User():

    def __init__(self, name,password,level=0.0,train="",trainer=False, email="", employee=""):
        self.name = name
        self.password = password
        self.level = level
        self.trainer = train
        self.is_trainer = trainer
        self.email = email
        self.employee = employee



class EditUser(User):

    def __init__(self, User):
        self.user = User

    def get_user(self):
        return self.user


    def change_name(self, new_name):
        self.user.name = new_name


    def change_password(self, new_password):
        self.user.password = new_password


    def change_level(self, new_level):
        self.user.level = new_level


    def change_is_trainer(self, state):
        self.user.is_trainer = state


    def change_trainer(self, trainer):
        self.user.trainer = trainer

    def change_email(self, email):
        self.email = email

    def save_user(self,user):
        DS.write_user(user)
   

class DeleteUser(User):

    def __init__(self, User):
        self.user = User


    def delete_user(self, name):
        if self.user.name == name:
            self.user.name = None
            self.user.password = None
            self.user.email = None
            self.user.level = 0
            self.user.trainer = None
            self.user.employee = None
            return True
        else:
            return False     


