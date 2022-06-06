import User
import DataStore
import onetimepad
from tkinter import messagebox as mb

DS = DataStore.data_store()
UR = User


ENTRY = "ByH1KHdo7y30I6aN"
LI_user = []

class Login():

    def __init__(self,username,password):
        self.name = username
        self.password = password
        self.login_user()

    def get_logged_in_user(self):
        if LI_user:
            return LI_user[0]
        else:
            return False

    def login_user(self):
        self.reset_user()
        user_data = DS.get_login_data()
        for name in user_data:
            if name["Name"] == self.name:
                plain_password = onetimepad.decrypt(name['Password'],ENTRY)
                if plain_password == self.password:
                    self.write_user(name['Name'], name['admin'])
                    return True
                else:
                    mb.showerror(title="Log in error",message="Login username or password incorrect.")
                    self.reset_user()
                    return False

    def write_user(self,user,admin):
        LI_user.append(user)
        LI_user.append(admin)

    def reset_user(self):
        LI_user.clear()



