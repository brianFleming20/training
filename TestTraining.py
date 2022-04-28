import unittest
import Training
import Documents
import User
import DataStore

TR = Training.Training()
TE = Training
DOC = Documents.Document()
USER = User
DS = DataStore.data_store()


class TrainingTests(unittest.TestCase):

    def setUp(self):
        self.document_ref = None
        self.trainer = "Lee"
        self.notes = []
        self.expires_on = None
        self.review_date = None
        self.username = None
        self.a_user = USER.User(name="Brian", password="password", level=3, train="Lee", trainer=False)
        self.b_user = USER.User(name="Hendryk", password="Haha", level=2, train="Lee", trainer=True)

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

    def test_get_all_trainers(self):
        print("Get all trainers")

        expected = ["Linn", "Alan"]

        result = TR.get_all_trainers()

        self.assertEqual(expected, result)

    def test_get_all_trained_at_level(self):
        print("get all that are trained at a level")

        expected = 3
        users = TR.get_all_at_level(3)

        result = len(users)

        self.assertEqual(result, expected)

    def test_who_is_trainer(self):
        print("Get all trainers")

        expected = ["Lee", "Alex"]

        result = TR.who_is_trainer()

        self.assertTrue(expected, result)

    def test_get_all_documents(self):
        print("Get all documents")

    def test_get_user_info(self):
        print("Test get user info")

        users = TR.get_all_users()
        for user, values in users.items():
            expected = values

            user_info = TR.get_user(user)

            for (k, v), (k1, v1) in zip(expected.items(), user_info.items()):
                self.assertEqual(v, v1)

    def test_save_user(self):
        print("Test save user to file")

        expected = "Lin"

        TR.save_user(self.a_user)

        users = DS.read_users_data()

        if expected in users:
            result = True

        self.assertEqual(result, True)

    def test_doc_trained_on_user(self):
        print("Test adding a training record")
        doc_ref = []
        # create user
        user = self.a_user

        note = "Training note for the user"

        username = user.name

        # create document use doc already in the system file
        docs = TR.get_documents()
        for ref, doc in docs.items():
            print(ref)
            doc_ref.append(ref)

        train_date = TR.get_date_now()
        review_date = TR.get_review_date()
        name = "Stores"

        print(user.trainer)

        # create training event
        training_record1 = TE.CreateTraining(username, name, doc_ref[4], train_date, review_date, note)

        # record training event
        TR.add_training_record(training_record1)

        # check training event
        training = TR.get_all_training()


        for a_user, event in training.items():

            for doc, item in event.items():

                for a, b in item.items():
                    print(a)
                    print(b)

    # add a new training document a user
    def test_zadd_new_training_doc_to_user(self):
        print("Test adding a new document to a user for training")

        doc_ref = []
        # create user
        user = self.b_user

        note = "This is a good room"

        username = user.name

        # create document use doc already in the system file
        docs = TR.get_documents()
        for ref, doc in docs.items():
            doc_ref.append(ref)

        train_date = TR.get_date_now()
        review_date = TR.get_review_date()
        name = "Monitor"

        print(user.trainer)

        # create training event
        training_record2 = TE.CreateTraining(username, name, doc_ref[1], train_date, review_date, note)

        # record training event
        TR.add_to_user_training(training_record2)

        # check training event
        training = TR.get_all_training()

        # for a_user, event in training.items():
        #     for doc, item in event.items():
        #         for a, b in item.items():
        #             print(a)
        #             print(b)


    def test_check_expire_dates(self):
        print("Test all document expire dates for user")

        user = "Lin"


if __name__ == '__main__':
    unittest.main()
