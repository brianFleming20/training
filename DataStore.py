import json
import pickle
from tkinter import messagebox as mb



class data_store():

    def __init__(self):
        self.data = []

    # Write or add user to pickle

    def write_user(self, user):
        user_json = self.create_dict(user)
        try:
            with open('file.user', 'r') as user_file:
                data = json.load(user_file)
        except FileNotFoundError:
            with open('file.user','w') as user_file:
                json.dump(data, user_file, indent=4)
        else:
            data.update(user_json)
            with open('file.user','w') as user_file:
                json.dump(data, user_file, indent=4)



    # Read user from pickle
    def read_users(self):
        try:
            with open('file.user', 'r') as load_user_file:
                load_data = json.load(load_user_file)
        except FileNotFoundError:
           
            mb.showinfo(title="File Error",message="File not found\nTry again.")
        else:
     
            return load_data


    def get_user_obj(self, name):
    
        for usr,value in self.read_users().items():
            if usr == name:      
                return value
        else:
            return False


    def check_user_in_system(self,user,loaded_file):
        if type(loaded_file) is list:
            for a_user in loaded_file:
                print(a_user.name)
                if a_user.name == user.name:
                    mb.showinfo(title="     User ",message="User found.")
                    return False
                else:
                    return True
               
                    
    def update_user_file(self, user):
        loaded_users = []
        loaded_users.insert(0,self.read_users())
        loaded_users.append(user)
        self.write_user(loaded_users)


    def delete_user(self,name):
        current_users = self.read_user()
        print(current_users)
        for user in current_users:
            if user.name == name:
                print(f"found {user.name}")



    def write_documents(self, documents):
        with open('file.docs', 'wb') as docs_file:
            pickle.dump(documents, docs_file)



    def get_all_documents(self):
        try:
            with open('file.docs', 'wb') as docs_file:
                docs_data = pickle.load(docs_file)
        except FileNotFoundError:
            mb.showinfo(title="     Document Error ",message="Document not found.")
        else:
            return docs_data


    def create_dict(self,user):
        new_data = {
            user.name:{
                'pass': user.password,
                'level':user.level,
                'trainer':user.trainer,
                'is_trainer':user.is_trainer,
                
            }
        }
   
        return new_data
    
