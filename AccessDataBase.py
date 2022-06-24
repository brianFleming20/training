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
        self.path = os.path.join("C:\\Users", os.getenv('username'),
                                 "Deltex Medical\Training - Documents\Training Database\Files\Docs", "")
        self.path_doc = os.path.join("C:\\Users", os.getenv('username'),
                                    "Deltex Medical\Training - Documents\Training Database\Files", "")
        self.path_doc_json = os.path.join("C:\\Users", os.getenv('username'),
                                           "Deltex Medical\Shared No Security - Documents\Brian Fleming\Training Database", "")
        self.is_trainer = False
        self.doc_names = None

    def get_data(self, file):
        raw_path = os.path.join(self.path, file)
        ###################################################################
        # As each of the training files are of different lengths, the     #
        # titles for the dataframe have to be altered too.                #
        ###################################################################
        header10 = ["Issue", "Trainee", "Level", "Trainer", "Date_Trained", "Review_date", "Logged_by",
                    "date_logged", "Status", "second_date"]
        header9 = ["Issue", "Trainee", "Level", "Trainer", "Date_Trained", "Review_date", "Logged_by",
                   "date_logged", "Status"]
        header8 = ["Issue", "Trainee", "Level", "Trainer", "Date_Trained", "Review_date", "Logged_by",
                   "date_logged"]
        ######################################################
        # Convert each document reference training file to a #
        # dataframe to be searched through.                  #
        ######################################################
        data = pd.read_csv(raw_path, header=None)
        length = len(data.columns)
        if length == 10:
            data.set_axis(header10, axis='columns', inplace=True)
        if length == 9:
            data.set_axis(header9, axis='columns', inplace=True)
        if length == 8:
            data.set_axis(header8, axis='columns', inplace=True)
        ######################################################
        # Removes all of the 'NaN' entries and replaces them #
        # with zeros.                                        #
        ######################################################
        data = data.fillna(0)
        #########################################
        # Returns the filtered data.            #
        #########################################
        return data, file[:-4]
        ##########################################################
        # search via logger for full list of users and documents #
        ##########################################################

    def search_data(self, data, doc_ref):
        ########################################################
        # extract all the names that are referred to a trainee #
        ########################################################
        all_names = data["Trainee"].to_list()

        ####################################################################
        # search all the names in the file for a document reference number #
        ####################################################################
        for name in all_names:
            user_data = data[data.Trainee == name]
            ##############################################################################################
            # For each of the names iterated through, collect that data row. The index is the row index  #
            # The row index is not needed, but has to be referenced to collect the rest of the data.     #
            #                                                                                            #
            # Iterates through the row of the selected name.                                             #
            # The status refers to the employee status as whether they and still employed by the company.#
            ##############################################################################################
            for index, row in user_data.iterrows():
                try:
                    status = row.Status
                except:
                    status = " "

                if row.Trainer:
                    self.is_trainer = True
                ######################################################################
                # Collects the document data taken from the document reference .csv  #
                # that matches to current training record being processed.           #
                ######################################################################
                doc_name_data = self.doc_names.loc[self.doc_names['Document No.'] == doc_ref]
                ######################################################################
                # Collects the document name from the relevant document              #
                # reference number.                                                  #
                ######################################################################
                doc_name = doc_name_data['Document Description'].to_string(index=False)
                #################################################################################
                # Generate a user object and save user to local file for display on main screen #
                #################################################################################
                user = US.User(row.Trainee, row.Trainer, "No email yet")
                result1 = DS.write_user(user)
                if not result1:
                    print("User not created")
                #######################################################################################
                # Generate a document object saved to the local file and displayed on the main screen #
                #######################################################################################
                document = MD.MakeDoc(doc_name, row.Issue, doc_ref)
                DS.write_document(document)
                ##################################################################################
                # Generate a training object and save to local file and displayed on main screen #
                ##################################################################################
                training = CT.CreateTraining(username=row.Trainee, doc_name=doc_name, doc_ref=doc_ref,
                                             train_date=row.Date_Trained, trainer=row.Trainer, review=row.Review_date,
                                             logger=row.Logged_by, level=row.Level, note=status)
                DS.add_training_record(training)
                #########################
                # Reset is trainer flag #
                #########################
                self.is_trainer = False
        return True

    def get_user_info(self):
        DS.reset_training_file()
        path = os.path.join(self.path_doc_json, "train.json")
        if os.path.exists(path):
            os.remove(path)
        ##################################################
        # Collect the training .csv file and convert it  #
        # to a pandas dataframe.                         #
        ##################################################
        raw_path = os.path.join(self.path_doc, "TrainingDocs.csv")
        self.doc_names = pd.read_csv(raw_path)
        ##################################################
        # Sort through all of the training files data    #
        ##################################################
        for files in os.listdir(self.path):
            data, file = self.get_data(files)
            if files[:5] == "Login":
                pass
            else:
                self.search_data(data, file)
