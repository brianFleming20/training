import unittest
import DataStore
import Training
import Login
import Documents
import User
import cryptocode

DS = DataStore.data_store()
TR = Training.Training()
LG = Login
MD = Documents
U = User


KEY = "ByH1KHdo7y30I6aN"
class DatastoreTests(unittest.TestCase):

    def test_get_user_admin(self):
        print("Test user admin status")
        name = "Brian Fleming"
        expected = 1

        result = DS.get_user_admin_status(name)

        self.assertEqual(expected,result)

    def test_save_data(self):
        print("Test save user login data")

        name = "Lee Lindfield"
        password = "password"
        admin = 1

        expected = False

        result = DS.save_data(name,password,admin)

        self.assertEqual(result,expected)

    def test_get_user_login(self):
        print("Test user login data")

        name = "Brian Fleming"
        password = "password"

        LG.Login(name,password)

        result = DS.get_login_data()


        for item in result:
            if item['Name'] == name:
                pw = item['Password']
                plain_text = cryptocode.decrypt(pw,KEY)
                self.assertEqual(plain_text,password)


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
        password = "my password"
        admin = 1
        pw = DS.update_user(name, password, admin)
        result = cryptocode.decrypt(pw,KEY)

        self.assertEqual(result, password)

    def test_send_data_to_file(self):
        print("Send data to csv file")

        document = MD.MakeDoc("Compressor Operation",1,"9070-2004")
        user = U.User("Brian Fleming",False,"my-email@gmail.com")
        #
        # TR.register_trained(document,user)

        training_to_file = [document.issue_number, user.name, 3, "Hendryk", TR.get_date_now(),
                            TR.get_review_date(), "System", TR.get_date_now(), "no status"]

        # result1 = DS.update_training_file(training_to_file, document.reference_number)




if __name__ == '__main__':
    unittest.main()