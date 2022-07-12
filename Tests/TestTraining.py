import unittest
import Training
import Documents
import User
import Login
import DataStore
import datetime as DT
import csv
import os

TR = Training.Training()
TE = Training
DOC = Documents
USER = User
DS = DataStore.data_store()
LG = Login


class TrainingTests(unittest.TestCase):

    def setUp(self):
        self.a_user = USER.User(name="Brian", is_trainer=False, email="no email yet")
        self.b_user = USER.User(name="Hendryk", is_trainer=True, email="no email yet")

    def test_time_now(self):
        print("Show time now")

        time = TR.get_date_now()
        print(time)

    def test_get_all_users(self):
        print("Get all users")
        names = []

        users = TR.get_all_users()

        for user in filter(None, users):
            names.append(user)

        result = len(names)

        self.assertGreater(result, 0)

    def test_get_review_data(self):
        print("Get a review date")

        review = TR.get_review_date()

        print(review)

    def test_get_documents(self):
        print("Get all documents")

        docs = TR.get_documents()
        result = len(docs)

        self.assertGreater(result, 0)

    def test_get_a_document(self):
        print("Get a document")

        document_ref = "9070-1203"
        expected = 27

        doc = TR.get_a_document(document_ref)
        result = doc['issue']

        self.assertEqual(result, expected)



    def test_logged_in_user(self):
        print("Get logged in user")

        name = "Brian Fleming"
        password = "password"
        admin = 1
        LG.Login(name,password)

        result = TR.get_logged_in_user()

        self.assertEqual(result, name)

        result1 = TR.get_user_admin()

        self.assertEqual(result1, admin)

    def test_save_user(self):
        print("Save a user to file")

        TR.save_user(self.b_user)

        name = "Hendryk"
        expected = "no email yet"

        user = TR.get_user(name)
        result = user['email']

        self.assertEqual(result, expected)

    def test_save_login(self):
        print("Save a user login data")

        name = "Lee"
        password = "your password"
        admin = 1
        user = USER.User(name="Lee", is_trainer=True)

        TR.save_user_login(user,password,admin)

        LG.Login(name,password)
        result = TR.get_logged_in_user()

        self.assertEqual(result, name)

    def test_all_training(self):
        print("Get all training")

        expected = 0

        training = TR.get_all_training()
        result = len(training)

        self.assertGreater(result, expected)

    def test_add_training(self):
        print("Resister a training record")
        file_location = os.path.join("C:\\Users", os.getenv('username'),
                                 "Desktop\\Training\\Docs", "")
        expected = True
        document = "9070-1203"
        user = "Brian Fleming"
        level = 3
        trainer = "Lee"
        password = "password"
        issue = 1
        note = "a note"
        LG.Login(user, password)
        training_to_file = [issue, user, level, trainer, TR.get_date_now(),
                            TR.get_review_date(), TR.get_logged_in_user(), TR.get_date_now(), note]

        # result = DS.add_training_to_file(training_to_file,document)

        # self.assertEqual(result, expected)
        # DS.remove_training_line(file_location,document)



    def test_get_user_training(self):
        print("Get a training record")
        name = "Brian Fleming"
        doc_ref = "9070-1203"

        expected = 3

        data = TR.get_training_record(name, doc_ref)
        result = data['level']

        self.assertEqual(result, expected)

    def test_get_email_date(self):
        print("Test getting email date")

        review_date = "10-07-2022"

        expected_review = True

        result2 = TR.get_email_date(review_date)

        self.assertEqual(expected_review,result2)

    def test_training_overdue_date(self):
        print("Test overdue training date")

        date = "01-05-2021"
        expected = True

        result = TR.get_overdue_train(date)

        self.assertEqual(expected,result)

    def test_review_date_formats(self):
        print("Test review different date formats")
        date1 = "15-06-2022"
        date2 = "15-06-22"
        date3 = "15/06/2022"
        date4 = "15/06/22"
        date5 = DT.datetime.now()
        date6 = 0.0
        date7 = ""

        expected = False
        expected_today = True

        check1 = TR.check_date_format(date1)
        result1 = TR.get_email_date(check1)
        self.assertEqual(expected, result1)

        check2 = TR.check_date_format(date2)
        result2 = TR.get_email_date(check2)
        self.assertEqual(expected,result2)

        check3 = TR.check_date_format(date3)
        result3 = TR.get_email_date(check3)
        self.assertEqual(expected, result3)

        check4 = TR.check_date_format(date4)
        result4 = TR.get_email_date(check4)
        self.assertEqual(expected,result4)

        check5 = TR.check_date_format(date5)
        result5 = TR.get_email_date(check5)
        self.assertEqual(expected_today,result5)

        check6 = TR.check_date_format(date6)
        result6 = TR.get_email_date(check6)
        self.assertEqual(expected_today,result6)

        check7 = TR.check_date_format(date7)
        print(check7)
        result7 = TR.get_email_date(check7)
        self.assertEqual(expected_today,result7)


if __name__ == '__main__':
    unittest.main()
