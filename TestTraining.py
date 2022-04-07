import unittest
import Training
import Documents
import User


TR = Training.Training()
DOC = Documents.Document()
USER = User.User()

class TrainingTests(unittest.TestCase):

    def setUp(self):
        self.document = None
        self.trainer = "Lee"
        self.notes = []
        self.expires_on = None
        self.review_date = None
        self.user = None
        USER.set_name("Lynn")
        USER.set_is_trainer(False)
        USER.set_trainer("Lee")
        USER.set_training_level(3)
        USER.save_user()
       
        USER.set_name("Lee")
        USER.set_is_trainer(True)
        USER.set_trainer("Alex")
        USER.set_training_level(1)
        USER.save_user()
     
        USER.set_name("Jon")
        USER.set_is_trainer(False)
        USER.set_trainer("Lee")
        USER.set_training_level(3)
        USER.save_user()
     

    def test_time_now(self):
        print("Show time now")

        TR.get_now_time()


    def test_get_all_users(self):
        print("Get all users")
        names = []
   
        expected = ["Jon","Lynn","Lee","Brian"]

        users = TR.get_all_users()

        for user in filter(None, users):
            names.append(user)

        self.assertEqual(expected,names)



    def test_get_all_trainers(self):
        print("Get all trainers")

        expected = ["Lee"]

        result = TR.get_all_trainers()

        self.assertEqual(expected,result)


    def test_get_all_trained_at_level(self):
        print("get all that are trained at a level")

        expected = ["Brian","Lynn","Jon"]

        result = TR.get_all_at_level(3)

        self.assertEqual(expected,result)


    def test_who_is_trainer(self):
        print("Get all trainers")

        expected = ["Lee","Alex"]

        result = TR.who_is_trainer()

        self.assertTrue(expected, result)


    def test_get_all_documents(self):
        print("Get all documents")



    def test_get_user_info(self):
        print("Test get user info")

        users = TR.get_all_users()
        for user,values in users.items():  
            expected = values
           
            user_info = TR.get_user(user)
         

            for (k,v),(k1,v1) in zip(expected.items(), user_info.items()):

                self.assertEqual(v,v1)
               


if __name__ == '__main__':
    unittest.main()