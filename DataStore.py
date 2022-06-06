import json
import os
from tkinter import messagebox as mb
import pandas as pd


class data_store():

    def __init__(self):
        self.data = []
        self.path = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\Training\\Docs", "")
        # self.data_path = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\Training\\", "")
        self.json_path = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\Training", "")
        self.check_directories()

    def write_user(self, user):

        fullPath = os.path.abspath(self.json_path + '.file.user')
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

    def write_user_admin(self, user, password, admin):
        self.save_data(user, password, admin)

    def dump_users(self, users):
        fullPath = os.path.abspath(self.json_path + '.file.user')
        with open(fullPath, 'w') as user_file:
            json.dump(users, user_file, indent=4)

    def read_users_data(self):
        fullPath = os.path.abspath(self.path + '.file.user')
        try:
            with open(fullPath, 'r') as load_user_file:
                load_data = json.load(load_user_file)
        except FileNotFoundError:
            pass
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
        loaded_users = self.read_users_data()
        loaded_users.append(user)
        self.write_user(loaded_users)

    def user_left(self, name):
        if name in self.read_users_data():
            pass
        else:
            return False


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
            self.add_training_to_file(training_obj)


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
            pass
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
                            train_data[the_user][key] = val
                            self.dump_training_data(train_data)
                            self.add_training_to_file(training_obj)


    def create_user_dict(self, user):
        new_data = {
            user.name: {
                'level': user.level,
                'trainer': user.trainer,
                'is_trainer': user.is_trainer,
                'email': user.email,
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
                    "entered_by": record.logger,
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

    def add_training_to_file(self, training_obj):
        comp = None
        empty = ""
        issue = ""
        trainer = ""
        doc_data = self.get_all_documents()
        file_loc = f"{training_obj.document_ref}.csv"
        for doc, item in doc_data.items():
            if file_loc == doc:
                issue = item['issue']
        for user, data in self.read_users_data().items():
            if user == training_obj.username:
                comp = data['level']
                trainer = data['trainer']
        training_data = [issue,training_obj.username, comp, trainer, training_obj.trained_on, empty,
                         training_obj.logger,training_obj.review_date,empty,empty]
        raw_path = os.path.join(self.data_path, file_loc)
        fake_path = "data.csv"
        data = pd.read_csv(raw_path)
        data_lists = data.values.tolist()
        if data_lists is None:
            mb.showinfo(title="    Saving document Error ", message="Document empty.")
        else:
            data_lists.append(training_data)
            df = pd.DataFrame(data_lists)
            # df.to_csv(fake_path, index=False)


    def get_login_data(self):
        raw_path = os.path.join(self.path, "Login.csv")
        try:
            data = pd.read_csv(raw_path)
        except FileNotFoundError:
            title_names = ["Name", "Password","Admin"]
            create = pd.DataFrame(columns=title_names)
            create.to_csv(raw_path, index=False)
        else:
            output_data = data.to_dict(orient="records")
            return output_data

    def save_data(self, name, password, admin):
        raw_path = os.path.join(self.data_path, "Login.csv")
        data = pd.read_csv(raw_path)
        output_data = data.to_dict(orient="records")
        for user in output_data:
            if user["Name"] == name:
                return False
            else:
                new_data = {
                            "Name": name,
                            "Password": password,
                            "admin": admin,
                        }
                output_data.insert(0, new_data)
                df = pd.DataFrame(output_data)
                df.to_csv(raw_path, index=False)
                return True

    def login_delete_user(self, name):
        raw_path = os.path.join(self.data_path, "Login.csv")
        data = pd.read_csv(raw_path)
        data.drop_duplicates(inplace=True)
        output_data = data.to_dict(orient="records")
        for user in output_data:
            if user["Name"] == name:
                output_data.remove(user)
                df = pd.DataFrame(output_data)
                df.to_csv(raw_path, index=False)
                return True
            else:
                return False


    def update_user(self, name, password, admin):
        raw_path = os.path.join(self.data_path, "Login.csv")
        data = pd.read_csv(raw_path)
        output_data = data.to_dict(orient="records")
        self.login_delete_user(name)
        self.save_data(name,password,admin)
        for user in output_data:
            if user['Name'] == name:
                if user['Password'] == password:
                    return False
                else:
                    return True

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

    def reset_files(self):
        train_path = os.path.abspath(self.path + '.train.json')
        doc_path = os.path.abspath(self.path + '.doc.json')
        # if os.path.exists(doc_path):
        #     os.remove(doc_path)
        # if os.path.exists(train_path):
        #     os.remove(train_path)

    def get_user_admin_status(self, name):
        raw_path = os.path.join(self.data_path, "Login.csv")
        data = pd.read_csv(raw_path)
        output_data = data.to_dict(orient="records")
        for item in output_data:
            if item['Name'] == name:
                print(f"admin = {type(item['admin'])}")
                return item['admin']
