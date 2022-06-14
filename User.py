'''
Creates a user object for the system to use.
'''

import DataStore

DS = DataStore.data_store()


class User:

    def __init__(self, name,trainer="",is_trainer=True, email=""):
        self.name = name
        self.trainer = trainer
        self.is_trainer = is_trainer
        self.email = email





class EditUser(User):

    def __init__(self, User, name, password):
        super().__init__(name, password)
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

    def __init__(self, User, name, password):
        super().__init__(name, password)
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



