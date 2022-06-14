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
        print(f"{file} : {data}")
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
        # extract all the names that are referred to a trainee
        all_names = data["Trainee"].to_list()
        # search all the names in the file for a document reference number
        for name in all_names:
            user_data = data[data.Trainee == name]
            # For each of the names iterated through, collect that data row. The index is the row index
            # The row index is not needed, but has to be referenced to collect the rest of the data.
            #
            # Iterates through the row of the selected name.
            # The status refers to the employee status as whether they and still employed by the company.
            for index, row in user_data.iterrows():
                try:
                    status = row.Status
                except:
                    status = " "

                if row.Trainer:
                    self.is_trainer = True

                doc_name_data = self.doc_names.loc[self.doc_names['Document No.'] == doc_ref]
                # print(doc_name_data['Document Description'].to_string(index=False))
                doc_name = doc_name_data['Document Description'].to_string(index=False)

                # Generate a user object and save user to local file for display on main screen
                user = US.User(row.Trainee, row.Trainer, self.is_trainer, "No email yet")
                DS.write_user(user)
                # Generate a document object saved to the local file and displayed on the main screen
                document = MD.MakeDoc(doc_name, row.Issue, doc_ref)
                DS.write_document(document)
                # Generate a training object and save to local file and displayed on main screen
                training = CT.CreateTraining(username=row.Trainee, doc_name=doc_name, doc_ref=doc_ref,
                                             train_date=row.Date_Trained, review=row.Review_date,
                                             logger=row.Logged_by, level=row.Level, note=status)
                DS.add_training_record(training)
                # Reset is trainer flag
                self.is_trainer = False

    def get_user_info(self):
        raw_path = os.path.join(self.path_doc_names, "TrainingDocs.csv")
        self.doc_names = pd.read_csv(raw_path)
        for files in os.listdir(self.path):
            data, file = self.get_data(files)
            if files[:5] == "Login":
                pass
            else:
                self.search_data(data, file)
