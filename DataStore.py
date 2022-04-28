import json
import os
from tkinter import messagebox as mb


class data_store():

    def __init__(self):
        self.data = []
        self.path = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\Training", "")
        self.check_directories()

    # Write or add user to pickle

    def write_user(self, user):
        fullPath = os.path.abspath(self.path + '.file.user')
        if user.name == None:
            mb.showerror(title="Save User Error", message="User cannot be none.")
        else:
            user_json = self.create_user_dict(user)
            try:
                with open(fullPath, 'r') as user_file:
                    data = json.load(user_file)
            except FileNotFoundError:
                with open(fullPath, 'w') as user_file:
                    json.dump(user_json, user_file, indent=4)
            else:
                data.update(user_json)
                with open(fullPath, 'w') as user_file:
                    json.dump(data, user_file, indent=4)

    def dump_users(self, users):
        fullPath = os.path.abspath(self.path + '.file.user')
        with open(fullPath, 'w') as user_file:
            json.dump(users, user_file, indent=4)

    # Read user from pickle
    def read_users_data(self):
        fullPath = os.path.abspath(self.path + '.file.user')
        try:
            with open(fullPath, 'r') as load_user_file:
                load_data = json.load(load_user_file)
        except FileNotFoundError:

            mb.showinfo(title="File Error", message="File not found\nTry again.")

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

    def check_user_in_system(self, user, loaded_file):
        if type(loaded_file) is list:
            for a_user in loaded_file:
                if a_user.name == user.name:
                    mb.showinfo(title="     User ", message="User found.")
                    return False
                else:
                    return True

    def update_user_file(self, user):
        loaded_users = []
        loaded_users.insert(0, self.read_users_data())
        loaded_users.append(user)
        self.write_user(loaded_users)

    def delete_user(self, name):
        data_set = []
        current_users = self.get_user_obj()
        data_set = self.read_users_data()
        for user in current_users:
            if user.name == name:
                print(f"found {user.name} ")
                print(data_set)

    def write_document(self, document):
        docPath = os.path.abspath(self.path + '.doc.json')
        doc_json = self.create_doc_file(document)

        try:
            with open(docPath, 'r') as doc_file:
                data = json.load(doc_file)
        except FileNotFoundError:
            with open(docPath, 'w') as doc_file:
                json.dump(doc_json, doc_file, indent=4)
        else:
            data.update(doc_json)
            with open(docPath, 'w') as doc_file:
                json.dump(data, doc_file, indent=4)

    def dump_documents(self, docs):
        fullPath = os.path.abspath(self.path + '.doc.json')

        with open(fullPath, 'w') as user_file:
            json.dump(docs, user_file, indent=4)

    def get_all_documents(self):
        docPath = os.path.abspath(self.path + '.doc.json')
        try:
            with open(docPath, 'r') as docs_file:
                docs_data = json.load(docs_file)
        except FileNotFoundError:
            mb.showinfo(title="     Document Error ", message="Document not found.")
        else:
            return docs_data

    def add_training_record(self, training_obj):
        trainPath = os.path.abspath(self.path + '.train.json')
        train_json = self.create_training_file(training_obj)

        try:
            with open(trainPath, 'r') as doc_file:
                data = json.load(doc_file)
        except FileNotFoundError:
            with open(trainPath, 'w') as doc_file:
                json.dump(train_json, doc_file, indent=4)
        else:
            data.update(train_json)
            with open(trainPath, 'w') as doc_file:
                json.dump(data, doc_file, indent=4)


    def dump_training_data(self, data):
        trainPath = os.path.abspath(self.path + '.train.json')
        with open(trainPath, 'w') as train_file:
            json.dump(data, train_file, indent=4)

    def get_all_training(self):
        trainPath = os.path.abspath(self.path + '.train.json')
        try:
            with open(trainPath, 'r') as train_file:
                train_data = json.load(train_file)
        except FileNotFoundError:
            mb.showinfo(title="     Training events Error ", message="Training event not found.")
        else:
            return train_data


    def add_training_to_user(self, training_obj):
        trainPath = os.path.abspath(self.path + '.train.json')
        the_values = self.create_new_doc_items(training_obj)

        if training_obj.username in self.get_all_training():
            with open(trainPath, 'r') as train_file:
                train_data = json.load(train_file)

                for the_user in train_data:
                    if training_obj.username == the_user:
                        for key,val in the_values.items():
                            print(f"a = {key} : b = {val}")
                            train_data[the_user][key] = val
                            print(train_data)
                            self.dump_training_data(train_data)



    def create_user_dict(self, user):
        new_data = {
            user.name: {
                'passwd': user.password,
                'level': user.level,
                'trainer': user.trainer,
                'is_trainer': user.is_trainer,
            }
        }

        return new_data

    def create_doc_file(self, doc):
        new_doc = {
            doc.reference_number: {
                "name": doc.doc_name,
                "issue": doc.issue_number,
                "location": doc.doc_location,
            }
        }
        return new_doc

    def create_training_file(self, record):
        new_record = {
            record.username: {
                record.document_ref: {
                    "name": record.document_name,
                    "trained_on": record.trained_on,
                    "review_date": record.review_date,
                    "note": record.notes,
                },
            }
        }

        return new_record

    def create_new_doc_items(self, record):
        new_doc = {
            record.document_ref: {
                "name": record.document_name,
                "trained_on": record.trained_on,
                "review_date": record.review_date,
                "note": record.notes,
            },
        }
        return new_doc

    def check_directories(self):
        '''
        Check that the directories exist, if not create them        
        '''
        if not os.path.isdir(self.path):
            try:
                os.makedirs(self.path, 0o777)
            except OSError:
                print(" %s already exists." % self.path)
            else:
                print("Successfully created the directory %s" % self.path)

        if not os.path.isdir(self.path):
            try:
                os.makedirs(self.path, 0o777)
            except OSError:
                print(" %s failed" % self.path)
            else:
                print("Successfully created the directory %s" % self.path)
