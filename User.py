'''
Creates a user object for the system to use.
'''

import DataStore
import Training

TR = Training
DS = DataStore.data_store()


class User():

    def __init__(self):
        self.name = ""
        self.password = ""
        self.level = 0
        self.trainer = ""
        self.is_trainer = False
     


    def get_user(self):
        return self


    def set_user_obj(self,obj):
        self = obj


    def set_name(self, name):
        self.name = name


    def get_name(self):
        return self.name


    def set_password(self, password):
        self.password = password
    

    def get_password(self):
        return self.password


    def set_training_level(self, level):
        self.level = level


    def get_training_level(self):
        return self.level


    def set_trainer(self, trainer):
        self.trainer = trainer


    def get_trainer(self):
        return self.trainer


    def set_is_trainer(self, state=False):
        self.is_trainer = state


    def get_is_trainer(self):
        return self.is_trainer


    def save_user(self):
        new_user = self.get_user()
        DS.write_user(new_user)


    def show_user_details(self):
        print(f"User name {self.name} : is a trainer {self.is_trainer} : User Level {self.level} : Is trainer on {self.documents} : by {self.trainer}")


class EditUser(User):

    def __init__(self, User):
        self.user = User


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


   

class DeleteUser(User):

    def __init__(self, User):
        self.user = User


    def delete_user(self, name):
        if self.user.name == name:
            self.user.name = None
            self.user.password = None
            self.user.documents = None
        
        return self.user




    

