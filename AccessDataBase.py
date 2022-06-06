import os
import pandas as pd
import Training
import DataStore
import User
import Documents

DS = DataStore.data_store()
CT = Training
TR = Training.Training()
US = User
MD = Documents


class GetExternalData:

    def __init__(self):
        # self.path = os.path.join("C:\\Users", os.getenv('username'),
        #                          "Deltex Medical\Training - Documents\Training Database\Files\Docs", "")
        self.path = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\Training\\Docs", "")
        self.is_trainer = False

    def get_data(self, file):
        raw_path = os.path.join(self.path, file)
        header10 = ["Issue", "Trainee", "Level", "Trainer", "Date_Trained", "Review_date", "Logged_by",
                    "date_logged", "Status", "second_date"]
        header9 = ["Issue", "Trainee", "Level", "Trainer", "Date_Trained", "Review_date", "Logged_by",
                   "date_logged", "Status"]
        header8 = ["Issue", "Trainee", "Level", "Trainer", "Date_Trained", "Review_date", "Logged_by",
                   "date_logged"]
        data = pd.read_csv(raw_path, header=None)
        length = len(data.columns)
        if length == 10:
            data.set_axis(header10, axis='columns', inplace=True)
        if length == 9:
            data.set_axis(header9, axis='columns', inplace=True)
        if length == 8:
            data.set_axis(header8, axis='columns', inplace=True)
        data = data.fillna(0)

        return data, file[:9]

        # search via logger for full list of users and documents

    def search_data(self, data, doc_ref, admin):
        name_idx = 0
        all_names = data["Trainee"].to_list()
        all_names = list(dict.fromkeys(all_names))
        name_len = len(all_names)
        user_login = TR.get_logged_in_user()
        while name_idx < name_len:
            user_data = data[data.Trainee == all_names[name_idx]]
            for index, row in user_data.iterrows():
                try:
                    status = row.Status
                except:
                    status = None
                if row.Trainer:
                    self.is_trainer = True
                user = US.User(row.Trainee, row.Level, row.Trainer, self.is_trainer, "No notes yet", status)
                training = CT.CreateTraining(row.Trainee, "", doc_ref, row.Date_Trained, row.Review_date, row.Logged_by)
                document = MD.MakeDoc("none", row.Issue, doc_ref)
                if admin:
                    print(f"user = {user.name} : ")
                    DS.write_user(user)
                    DS.add_training_record(training)
                    DS.write_document(document)
                if user_login == row.Trainee or user_login == row.Trainer:
                    print(f"user = {user} : training = {training} : doc = {document}")
                    DS.write_user(user)
                    DS.add_training_record(training)
                    DS.write_document(document)
                # else:
                #     print(f"user = {user} : training = {training} : doc = {document}")
                #     DS.write_user(user)
                #     DS.add_training_record(training)
                #     DS.write_document(document)
            name_idx += 1

    # def user_left(self, name):
    #     if name in DS.read_users_data():
    #         data = self.get_data()
    #         print(f" data {data}")
    #
    #         return True
    #     else:
    #         return False

    def get_user_info(self):
        admin = TR.get_user_admin()
        for files in os.listdir(self.path):
            data, file = self.get_data(files)
            if files[:5] == "Login":
                pass
            else:
                self.search_data(data, file, admin)
