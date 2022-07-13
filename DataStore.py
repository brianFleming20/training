import json
import os
from tkinter import messagebox as mb
import pandas as pd
import cryptocode
import csv
from tkinter import *
from tkinter import ttk

KEY = "ByH1KHdo7y30I6aN"
USERNAME = "brian.fleming@dtxmedical.onmicrosoft.com"
PASSWORD = "Manakin88%G"


class data_store():

    def __init__(self):
        self.total = 0.1
        self.data = []
        self.base_path = os.path.abspath("C:\\Users")
        self.file_data = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.data_path = ""
        self.json_path = ""
        self.read_data_file_locations()
        # self.check_directories()


    def write_user(self, user):
        fullPath = os.path.abspath(self.json_path + '\.file.user')
        if user.name == None:
            mb.showerror(title="Save User Error", message="User cannot be none.")
            return False
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
            return True

    def write_data_file_locations(self):
        raw_path = os.path.join(self.file_data, "DataLocation.json")
        self.show_prgress_screen("Getting file locations... ")
        data = self.search_data_path()
        data_file = self.search_path()
        file_obj = {
            "location1": data,
            "location2": data_file
        }
        with open(raw_path, 'w') as user_file:
            json.dump(file_obj, user_file, indent=4)
        self.destroy_window()

    def read_data_file_locations(self):
        raw_path = os.path.join(self.file_data, "DataLocation.json")
        flag = os.path.exists(raw_path)
        if flag:
            with open(raw_path, 'r') as load_user_file:
                load_data = json.load(load_user_file)
            self.json_path = load_data['location1']
            self.data_path = load_data['location2']
        else:
            self.write_data_file_locations()


    def write_user_admin(self, user, password, admin):
        self.save_data(user, password, admin)

    def dump_users(self, users):
        fullPath = os.path.abspath(self.json_path + '\.file.user')
        with open(fullPath, 'w') as user_file:
            json.dump(users, user_file, indent=4)

    def read_users_data(self):
        fullPath = os.path.abspath(self.json_path + '\.file.user')
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
            for usr, value in users.items():

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
        docPath = os.path.abspath(self.json_path + '\.doc.json')
        doc_json = self.create_doc_file(document)
        try:
            with open(docPath, 'r') as doc_file:
                data = json.load(doc_file)
        except FileNotFoundError:
            with open(docPath, 'w') as doc_file:
                json.dump(doc_json, doc_file, indent=4)
        else:
            data.update(doc_json)
            print(data)
            with open(docPath, 'w') as doc_file:
                json.dump(data, doc_file, indent=4)
            return True

    def dump_documents(self, docs):
        fullPath = os.path.abspath(self.json_path + '\.doc.json')
        with open(fullPath, 'w') as user_file:
            json.dump(docs, user_file, indent=4)

    def get_all_documents(self):
        docPath = os.path.abspath(self.json_path + '\.doc.json')
        result = False
        try:
            with open(docPath, 'r') as docs_file:
                docs_data = json.load(docs_file)
        except FileNotFoundError:
            mb.showinfo(title="     Document Error ", message="Document not found.")
        else:
            result = docs_data
        return result

    def add_training_record(self, training_obj):
        trainPath = os.path.abspath(self.json_path + '\.train.json')
        train_json = self.create_training_file(training_obj)
        try:
            with open(trainPath, 'r') as doc_file:
                data = json.load(doc_file)
                if training_obj.username in data:
                    self.add_training_to_user(training_obj)
                    return True
        except FileNotFoundError:
            with open(trainPath, 'w') as doc_file:
                json.dump(train_json, doc_file, indent=4)
        else:
            data.update(train_json)
            with open(trainPath, 'w') as doc_file:
                json.dump(data, doc_file, indent=4)
            self.add_training_to_user(training_obj)

    def dump_training_data(self, data):
        trainPath = os.path.abspath(self.find_json_files() + '\.train.json')
        with open(trainPath, 'w') as train_file:
            json.dump(data, train_file, indent=4)

    def get_all_training(self):

        trainPath = os.path.abspath(self.find_json_files() + '\.train.json')
        try:
            with open(trainPath, 'r') as train_file:
                train_data = json.load(train_file)
        except FileNotFoundError:
            mb.showinfo(title="     Training Error ", message="Training not found.")
        else:
            return train_data

    def add_training_to_user(self, training_obj):
        train_path = os.path.abspath(self.find_json_files() + '\.train.json')
        the_values = self.create_new_train_items(training_obj)
        with open(train_path, 'r') as train_file:
            train_data = json.load(train_file)
        for the_user in train_data:
            if training_obj.username == the_user:
                for key, val in the_values.items():
                    train_data[the_user][key] = val
                    self.dump_training_data(train_data)
                    return True




    # def update_training_file(self, training_file, doc_ref):
    #     result = self.add_training_to_file(training_file, doc_ref)
    #     return result

    def create_user_dict(self, user):
        new_data = {
            user.name: {
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
            }
        }
        return new_doc

    def create_training_file(self, record):
        new_record = {
            record.username: {
                record.document_ref: {
                    "name": record.document_name,
                    "trained_on": record.trained_on,
                    "trainer": record.trainer,
                    "review_date": record.review_date,
                    "entered_by": record.logger,
                    "entered_on": record.trained_on,
                    "level": record.level,
                    "note": record.notes,
                },
            }
        }
        print(new_record)
        return new_record

    def create_new_train_items(self, record):
        new_doc = {
            record.document_ref: {
                "name": record.document_name,
                "trained_on": record.trained_on,
                "trainer": record.trainer,
                "review_date": record.review_date,
                "entered_by": record.logger,
                "entered_on": record.trained_on,
                "level": record.level,
                "note": record.notes,
            },
        }
        return new_doc

    # def add_training_to_file(self, training_data, ref):
    #     file_loc = f"{ref}.csv"
    #     data_path = os.path.join("C:\\Users", os.getenv('username'),
    #                              "Desktop\\Training\\Docs", "")
    #     raw_path = os.path.join(data_path, file_loc)
    #     data_path = os.listdir(data_path)
    #     if file_loc in data_path:
    #         with open(raw_path, 'a', newline='') as file:
    #             writer = csv.writer(file, delimiter=',')
    #             writer.writerow(training_data)
    #         return True
    #     else:
    #         return False

    # def remove_training_line(self, location,ref):
    #     file_loc = f"{ref}.csv"
    #     data_path = location
    #     raw_path = os.path.join(data_path, file_loc)
    #     data_path = os.listdir(data_path)
    #     if file_loc in data_path:
    #         with open(raw_path, 'r') as file:
    #             lines = file.readlines()
    #     lines = lines[:-1]
    #     with open(raw_path, 'w', newline='') as file:
    #         for line in lines:
    #             file.write(line)

    def get_login_data(self):
        raw_path = os.path.join(self.data_path, "Login.csv")
        try:
            data = pd.read_csv(raw_path)
        except FileNotFoundError:
            title_names = ["Name", "Password", "admin"]
            create = pd.DataFrame(columns=title_names)
            create.to_csv(raw_path, index=False)
            return False
        else:
            output_data = data.to_dict(orient="records")
            return output_data

    def save_data(self, name, password, admin):
        raw_path = os.path.join(self.data_path, "Login.csv")
        data = pd.read_csv(raw_path)
        output_data = data.to_dict(orient="records")
        encrypt2 = cryptocode.encrypt(password, KEY)
        for user in output_data:
            if user["Name"] == name:
                return False
        new_data = {
            "Name": name,
            "Password": encrypt2,
            "admin": admin,
        }
        output_data.insert(0, new_data)
        df = pd.DataFrame(output_data)
        df.to_csv(raw_path, index=False)
        return True

    def login_delete_user(self, name):
        raw_path = os.path.join(self.data_path, "Login.csv")
        data = pd.read_csv(raw_path)
        indexNames = data[data['Name'] == name].index
        data.drop(indexNames, inplace=True)
        data.to_csv(raw_path, index=False)
        return True

    def update_user(self, name, password, admin):
        raw_path = os.path.join(self.data_path, "Login.csv")
        data = pd.read_csv(raw_path)
        result = False
        output_data = data.to_dict(orient="records")
        for user in output_data:
            if user['Name'] == name:
                data.loc[data['Name'] == name, 'Password'] = password
                data.loc[data['Name'] == name, 'admin'] = admin
                result = password
            else:
                result = False
        data.to_csv(raw_path, mode='w', index=False)
        return result


    def check_directories(self):
        '''
        Check that the directories exist, if not create them        
        '''

        if not os.path.isdir(self.json_path):

            os.makedirs(self.json_path, 0o777)



                # path = "https://dtxmedical.sharepoint.com/:u:/s/SharedNoSecurity/Ef_r7mG-GqtJrIVHHvImXBkBqJKvKQwgvnc-ru3kjdphlQ?e=Mhy3Cy&download=1"
                # webbrowser.open(path)
                # path1 = "https://dtxmedical.sharepoint.com/:u:/s/SharedNoSecurity/ERwEjASwsM5IpkwZYb8tdXMBe48uCXrACsyOoxnuceCaHQ?e=BeCWN5&download=1"
                # webbrowser.open(path1)
                # path2 = "https://dtxmedical.sharepoint.com/:u:/s/SharedNoSecurity/EXx2VMohW-dJp1hrAuctxsMBy4JMvZMLWfYyTQihM4VFKA?e=gQz0Sw&download=1"
                # webbrowser.open(path2)
                # time.sleep(5)
                #
                # locations = ['doc.json','file.user','train.json']
                # for loc in locations:
                #     originalPath = os.path.abspath(self.download + loc)
                #     destinationPath = os.path.abspath(self.json_fake + loc)
                #     os.renames(originalPath, destinationPath)
                # time.sleep(3)
                # try:
                #     os.system("taskkill / IMmsedge.exe / F")
                # except:
                #     pass
                # try:
                #     os.system("taskkill /im firefox.exe /f")
                # except:
                #     pass
                # try:
                #     os.system("taskkill /im chrome.exe /f")
                # except:
                #     pass

    def get_data_file_location(self):
        return self.json_path

    def reset_training_file(self):
        train_path = os.path.abspath(self.json_path + '\.train.json')
        doc_path = os.path.abspath(self.json_path + '\.doc.json')
        if os.path.exists(train_path):
            os.remove(train_path)
        if os.path.exists(doc_path):
            os.remove(doc_path)

    def get_user_admin_status(self, name):
        raw_path = os.path.join(self.data_path, "Login.csv")
        data = pd.read_csv(raw_path)
        result = None
        output_data = data.to_dict(orient="records")
        for item in output_data:
            if item['Name'] == name:
                result = item['admin']
            else:
                result = False
        return result

    def find_data_files(self):
        if self.data_path == "":
            self.data_path = self.search_path()
        else:
            return self.data_path

    def find_json_files(self):
        if self.json_path == "":
            self.json_path = self.search_data_path()
        else:
            return self.json_path
        self.check_directories()

    def search_path(self):
        name = "Deltex Medical"
        file = "Training - Documents"
        location = "Training Database"
        training_files = "Files"
        endpoint = "Docs"
        for root, dirs, files in os.walk(self.base_path):
            self.increase_total(0.01)
            if name in root:
                if file in root:
                    if location in root:
                        if training_files in root:
                            if endpoint in root:
                                return root


    def search_data_path(self):
        name = "Deltex Medical"
        file = "Shared No Security - Documents"
        location = "Brian Fleming"
        data_files = "Training Database"
        endpoint = "DataFiles"
        for root, dirs, files in os.walk(self.base_path):
            self.increase_total(0.01)
            if name in root:
                if file in root:
                    if location in root:
                        if data_files in root:
                            if endpoint in root:
                                return root


    def show_prgress_screen(self, title):
        self.window = Tk()
        self.window.title("Please wait")
        w = 330  # width for the Tk root
        h = 150  # height for the Tk root

        # calculate x and y coordinates for the Tk root window
        x = (1400 / 2) - (w / 2)
        y = (1100 / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.attributes('-topmost', True)
        Label(self.window, text=title).place(x=90, y=35)
        # progressbar
        self.pb = ttk.Progressbar(
            self.window,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        self.pb.place(x=20, y=100)
        Tk.update(self.window)

    def destroy_window(self):
        self.pb['value'] = 100
        self.window.destroy()

    def increase_total(self,num):
        self.total += num
        if self.pb['value'] < 100:
            self.pb['value'] = self.total
            self.window.update_idletasks()