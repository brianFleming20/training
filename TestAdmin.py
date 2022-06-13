import unittest
import AdminUser
import Training


AU = AdminUser
AUT = AdminUser
TR = Training.Training()


class AdminTests(unittest.TestCase):

    def test_add_user(self):
        print("Test add new user")

        name = "Alan"
        password = "letmein"
        conf_pass = "letmein"
        email = "my new email"
        encrypt = "testtesttest"
        admin = True
        trainer = "Lee"
        administrator = 1

        result = AU.AddNewUser.create_user(AU,name,password,conf_pass,email, admin,encrypt, trainer, administrator)

        self.assertEqual(result, True)

    def test_record_training(self):
        print("Record new training")
        root = AUT.RecordTraining()
        AU.RecordTraining.set_up_for_test(AU, 3)

        AU.RecordTraining.register_training(AU)




if __name__ == '__main__':
    unittest.main()