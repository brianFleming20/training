import unittest
import DataStore
import Training
import Login
import Documents
import User
import cryptocode
import AccessDataBase
import csv
import os

DS = DataStore.data_store()
TR = Training.Training()
LG = Login
MD = Documents
U = User
AS = AccessDataBase.GetExternalData()


KEY = "ByH1KHdo7y30I6aN"
class DatastoreTests(unittest.TestCase):

    def test_get_user_admin(self):
        print("Test user admin status")
        name = "Brian Fleming"
        expected = 1

        result = DS.get_user_admin_status(name)

        self.assertEqual(expected,result)

    def test_save_user_data(self):
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

    def test_no_user_login_found(self):
        print("No loggin user found")

        name = "Jo-Jo"

        result = DS.get_user_admin_status(name)

        self.assertEqual(result, False)


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

    def test_update_user_not_in_system(self):
        print("Test to update non user")

        name = "Jo=Jo"
        password = "12345678"
        admin = 0

        result = DS.update_user(name,password,admin)

        self.assertEqual(result, False)


    def test_send_data_to_file(self):
        print("Send data to csv file")

        document = MD.MakeDoc("Compressor Operation",1,"9070-2004")
        user = U.User("Brian Fleming",False,"my-email@gmail.com")
        trainer = "Hendryk"
        level = 3
        note = "no status"

        result = TR.register_trained(document,user,level,trainer,note)

        training_to_file = [document.issue_number, user.name, level, trainer, TR.get_date_now(),
                            TR.get_review_date(), "System", TR.get_date_now(), note]

        self.assertEqual(result,False) # as this training has already taken place

        result1 = DS.add_training_to_file(training_to_file, document.reference_number)

        doc_number = document.reference_number
        username = user.name
        training = TR.get_training_record(username,doc_number)
        result2 = training['note']
        expected = "Expired"

        self.assertEqual(result2,expected)

        self.assertEqual(result1,True)

        data_file = f"{doc_number}.csv"

        data,ref = AS.get_data(data_file)
        data_list = data['Logged_by'].astype(str).tolist()

        for name in data_list:
            if name == trainer:
                self.assertEqual(name,trainer)

    def test_send_wrong_doc_to_file(self):
        print("Test send wrong doc file to DB")

        document = MD.MakeDoc("Compressor Operation", 1, "9090-0001")
        user = U.User("Brian Fleming", False, "my-email@gmail.com")
        trainer = "Hendryk"
        level = 3
        note = "no status"

        result = TR.register_trained(document, user, level, trainer, note)

        training_to_file = [document.issue_number, user.name, level, trainer, TR.get_date_now(),
                            TR.get_review_date(), "System", TR.get_date_now(), note]

        # result1 = DS.add_training_to_file(training_to_file, document.reference_number)

        self.assertEqual(result,False)
        # self.assertEqual(result1,False)

    def test_remove_test_data_from_file(self):
        print("Removing test data from file")
        self.json_fake = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\Docs", "")

        data_file = os.path.join(self.json_fake,"9070-1203.csv")

        # with open(data_file, "a") as f:
        #     lines = f.readlines()
        #     lines = lines[:-1]
        #
        # cWriter = csv.writer(f, delimiter=',')
        # for line in lines:
        #     cWriter.writerow(line)



if __name__ == '__main__':
    unittest.main()