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
        self.path_doc_names = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\Training", "")
        self.is_trainer = False
        self.doc_names = None

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

        return data, file[:-4]

        # search via logger for full list of users and documents

    def search_data(self, data, doc_ref):
        all_names = data["Trainee"].to_list()
        for name in all_names:
            user_data = data[data.Trainee == name]
            for index, row in user_data.iterrows():
                try:
                    status = row.Status
                except:
                    status = None
                if row.Trainer:
                    self.is_trainer = True

                doc_name_data = self.doc_names.loc[self.doc_names['Document No.'] == doc_ref]
                # print(doc_name_data['Document Description'].to_string(index=False))
                doc_name = doc_name_data['Document Description'].to_string(index=False)
                user = US.User(row.Trainee, row.Trainer, self.is_trainer, "No email yet")
                DS.write_user(user)
                document = MD.MakeDoc(doc_name, row.Issue, doc_ref)
                DS.write_document(document)
                training = CT.CreateTraining(username=row.Trainee, doc_name=doc_name, doc_ref=doc_ref,
                                             train_date=row.Date_Trained, review=row.Review_date,
                                             logger=row.Logged_by, level=row.Level, note=status)
                DS.add_training_record(training)

    def get_user_info(self):
        raw_path = os.path.join(self.path_doc_names, "TrainingDocs.csv")
        self.doc_names = pd.read_csv(raw_path)

        for files in os.listdir(self.path):
            data, file = self.get_data(files)
            if files[:5] == "Login":
                pass
            else:
                self.search_data(data, file)
