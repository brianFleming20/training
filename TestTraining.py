import unittest
import Training
import Documents
import User
import Login
import DataStore
import datetime as DT

TR = Training.Training()
TE = Training
DOC = Documents
USER = User
DS = DataStore.data_store()
LG = Login


class TrainingTests(unittest.TestCase):

    def setUp(self):
        self.a_user = USER.User(name="Brian", trainer="Lee", is_trainer=False)
        self.b_user = USER.User(name="Hendryk", trainer="Lee", is_trainer=True)

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

    def test_get_users(self):
        print("Get all users")

        users = TR.get_all_users()
        result = len(users)

        self.assertGreater(result, 0)


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
        expected = "Lee"

        user = TR.get_user(name)
        result = user['trainer']

        self.assertEqual(result, expected)

    def test_save_login(self):
        print("Save a user login data")

        name = "Lee"
        password = "your password"
        admin = 1
        user = USER.User(name="Lee", trainer=True)

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

        expected = True
        document = "9070-1203"
        user = "Brian Fleming"
        level = 3
        password = "password"
        LG.Login(user, password)

        result = TR.register_trained(document, user, level, "Note")

        self.assertEqual(result, expected)

    def test_get_training(self):
        print("Get a training record")
        name = "Brian Fleming"
        doc_ref = "9070-1203"

        expected = 3

        data = TR.get_training_record(name, doc_ref)
        result = data['level']

        self.assertEqual(result, expected)

    def test_get_email_date(self):
        print("Test getting email date")
        date = "14-06-2022"

        result1 = TR.get_email_date(date)

        expected_now = True

        self.assertEqual(expected_now,result1)

        review_date = "01-09-2022"

        expected_review = False

        result2 = TR.get_email_date(review_date)

        self.assertEqual(expected_review,result2)



if __name__ == '__main__':
    unittest.main()
