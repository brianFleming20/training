import unittest
import os
import json
import AccessDataBase
import Login
import User
import DataStore
import pandas as pd

AD = AccessDataBase.GetExternalData()
LOG = Login
US = User
DS = DataStore.data_store()


ENTRY = "ByH1KHdo7y30I6aN"

class remoteDataTests(unittest.TestCase):

    def setUp(self):
        self.path = os.path.join("C:\\Users", os.getenv('username'),
                                 "Desktop\\Training\\Docs", "")
        self.path_doc = os.path.join("C:\\Users", os.getenv('username'),
                                     "Deltex Medical\Training - Documents\Training Database\Files", "")
        raw_path = os.path.join(self.path_doc, "TrainingDocs.csv")
        self.path_doc_json = os.path.join("C:\\Users", os.getenv('username'),
                                          "Deltex Medical\Shared No Security - Documents\Brian Fleming\Training Database\DataFiles",
                                          "")
        AD.doc_names = pd.read_csv(raw_path)


    def test_get_info_from_file(self):
        print("Test getting data from file")

        user = "Brian Fleming"
        password = "password"
        LOG.Login(user,password)
        expected = type(pd.DataFrame())
        expected2 = str


        for file in os.listdir(self.path):
            data, doc_ref = AD.get_data(file)
            result = type(data)
            result2 = type(doc_ref)
            self.assertEqual(result,expected)
            self.assertEqual(result2,expected2)

    def test_one_dataframe(self):
        print("Test the dataframe save method")

        ref_number = '9070-1203.csv'
        raw_path = os.path.join(self.path, ref_number)
        header10 = ["Issue", "Trainee", "Level", "Trainer", "Date_Trained", "Review_date", "Logged_by",
                    "date_logged", "Status"]
        expected = 'Grant'
        df = pd.read_csv(raw_path, header=None)

        df.set_axis(header10, axis='columns', inplace=True)
        result = AD.search_data(df,ref_number)

        self.assertEqual(True, result)

        if not os.path.abspath(self.path_doc_json + '\.file.user'):
            json_path = False
        else:
            json_path = os.path.abspath(self.path_doc_json + '\.file.user')
        print(json_path)

        with open(json_path, 'r') as user_file:
            users = json.load(user_file)

        for user,data in users.items():
            if user == 'Grant':
                self.assertEqual(user, expected)

    def test_progress_bar(self):
        print("Test progress bar")

        AD.get_user_info()




if __name__ == '__main__':
    unittest.main()