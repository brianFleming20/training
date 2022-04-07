import json
import os
import pickle
from tkinter import messagebox as mb



class data_store():

    def __init__(self):
        self.data = []
        self.path = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\Training", "")
        self.check_directories()

    # Write or add user to pickle

    def write_user(self, user):
        fullPath = os.path.abspath(self.path + '.file.user')
        user_json = self.create_dict(user)
        try:
            with open(fullPath, 'r') as user_file:
                data = json.load(user_file)
        except FileNotFoundError:
            with open(fullPath,'w') as user_file:
                json.dump(user_json, user_file, indent=4)
        else:
            data.update(user_json)
            with open(fullPath,'w') as user_file:
                json.dump(data, user_file, indent=4)



    # Read user from pickle
    def read_users_data(self):
        fullPath = os.path.abspath(self.path + '.file.user')
        try:
            with open(fullPath, 'r') as load_user_file:
                load_data = json.load(load_user_file)
        except FileNotFoundError:
           
            mb.showinfo(title="File Error",message="File not found\nTry again.")
            
        else:
            return load_data


    def get_user_obj(self, usr_obj):
        users = self.read_users_data()
        if users == None:
            self.write_user(usr_obj)
        else:
            for usr,value in users.items():
                if usr == usr_obj.name:      
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
        loaded_users.insert(0,self.read_users_data())
        loaded_users.append(user)
        self.write_user(loaded_users)


    def delete_user(self,name):
        current_users = self.get_user_obj()
        print(current_users)
        for user in current_users:
            if user.name == name:
                print(f"found {user.name}")



    def write_documents(self, documents):
        docPath = os.path.abspath(self.path + '.file.doc')
        with open(docPath, 'w') as docs_file:
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


    def create_doc_file(self, doc):
        new_doc = {
            
        }
    
    def check_directories(self):
        '''
        Check that the directories exist, if not create them        
        '''
        if not os.path.isdir(self.path):
            try:
                os.makedirs(self.path, 0o777)
            except OSError:
                print (" %s already exists." % self.path)
            else:
                print ("Successfully created the directory %s" % self.path)

        if not os.path.isdir(self.path):
            try:
                os.makedirs(self.path, 0o777)
            except OSError:
                print (" %s failed" % self.path)
            else:
                print ("Successfully created the directory %s" % self.path)