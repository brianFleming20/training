import User
import DataStore
import cryptocode
import AccessDataBase
import pandas as pd
import os
from tkinter import messagebox as mb

DS = DataStore.data_store()
UR = User


ENTRY = "ByH1KHdo7y30I6aN"

LI_user = []
class Login():

    def __init__(self,username,password):
        self.name = username
        self.password = password

        
    def get_user(self):
        user = UR.User(self.name,self.password)
        return user

    def get_logged_in_user(self):
        return LI_user


    def login_user(self):
        # login_data = LOG.get_login_data()
        user_obj = self.get_user()
        user = DS.get_user_obj(user_obj)
        if user != False:
            for item,value in user.items():
                if item == "passwd":
                    password = value
                if item == "is_trainer":
                    admin = value
            plain_password = cryptocode.decrypt(password, ENTRY)
            #plain_password = password
            if plain_password == user_obj.password:
                self.write_user(user_obj)
                return True,admin
            else:
                return False,False
        else:
            return False,False

    def write_user(self,user):
        LI_user.append(user)

    def get_login_data(self):
        path = os.path.join("C:\\Users", os.getenv('username'),
                            "Deltex Medical\Training - Documents\Training Database\Files\Docs", "")
        raw_path = os.path.join(path, "Login.csv")
        try:
            data = pd.read_csv(raw_path)
        except FileNotFoundError:
            title_names = ["Name", "Password"]
            create = pd.DataFrame(columns=title_names)
            create.to_csv(raw_path, index=False)
        else:
            output_data = data.to_dict(orient="records")
            print(output_data)

    def save_data(self, name, password):
        print(f"user {name} : password {password}")
        path = os.path.join("C:\\Users", os.getenv('username'),
                            "Deltex Medical\Training - Documents\Training Database\Files\Docs", "")
        raw_path = os.path.join(path, "Login.csv")
        users = pd.read_csv(raw_path)
        try:
            print(users[name])
            if users[name] == name:
                print("ok")
        except:
            print("no")
        insert_data = { name, password}
        #users = users.concat(insert_data)
        try:
            insert_data.to_csv(raw_path, mode='a', header=False)
        except:
            mb.showerror(title="File error",message="File is open, \nclose file and try again...")
        # if users not None:
        #     for user,item in users.items():
        #         print(user)
        # check for user and append csv file
