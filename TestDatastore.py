import unittest
import DataStore
import onetimepad
import Training

DS = DataStore.data_store()
TR = Training

KEY = "ByH1KHdo7y30I6aN"
class DatastoreTests(unittest.TestCase):

    def test_get_user_admin(self):
        print("Test user admin status")
        name = "Brian Fleming"
        expected = "1"

        result = DS.get_user_admin_status(name)

        self.assertEqual(expected,result)

    def test_save_data(self):
        print("Test save user login data")

        name = "Brian Fleming"
        password = "password"
        admin = 1

        cipher = onetimepad.encrypt(password, KEY)

        expected = True

        result = DS.save_data(name,cipher,admin)

        self.assertEqual(result,expected)

    def test_get_user_login(self):
        print("Test user login data")

        name = "Brian Fleming"
        password = "password"

        result = DS.get_login_data()


        for item in result:
            if item['Name'] == name:
                pw = item['Password']
                plain_text = onetimepad.decrypt(pw,KEY)
                self.assertEqual((plain_text,password))


    def test_1_insert_user(self):
        print("Test insert user to login database csv")
        name = "Lin"
        password = "password2"
        admin = 0
        result = DS.save_data(name,password, admin)

        self.assertEqual(result, True)

    def test_2_insert_user_already_in_system(self):
        print("Test add user already in system")

        name = "Lin"
        password = "password2"
        admin = 0
        result = DS.save_data(name, password, admin)

        self.assertEqual(result, False)

    def test_3_delete_user(self):
        print("Test delete a user from the login database csv")
        name = "Lin"
        result = DS.login_delete_user(name)

        self.assertEqual(result, True)

    def test_4_update_user(self):
        print("Test update password")
        name = "Brian Fleming"
        admin = 1
        sec_password = onetimepad.encrypt("password", ENTRY)

        result = DS.update_user(name, sec_password, admin)

        self.assertEqual(result, True)

    def test_send_data_to_file(self):
        print("Send data to csv file")

        training = TR.CreateTraining(username="Brian Fleming", doc_ref="3000-0002", doc_name="Printing",
                                  train_date="18/5/2022", review="18/5/2023",
                                  logger="System")

        DS.add_training_to_file(training)





if __name__ == '__main__':
    unittest.main()