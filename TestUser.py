import unittest
from tkinter import StringVar
import cryptocode

import User
import Training
import DataStore
import AdminUser

UR = User
TR = Training.Training()
DS = DataStore.data_store()
AU = AdminUser

ENTRY = "ByH1KHdo7y30I6aN"

class UserTests(unittest.TestCase):


    def setUp(self):
        user = UR.User("Brian","the other",3,"Lee",True)
        self.this_user = user
        self.edit_user = UR.EditUser(self.this_user)
        self.added_user = UR.User("Jack","password",2)
        self.delete_user = UR.DeleteUser(self.added_user)
        self.passw = StringVar()
        self.conf_pass = StringVar()

    def test_update_password(self):
        print("Test change password")
        
        expected = "password"

        TR.save_user(self.this_user)

        AU.EditUser.set_for_test(self,"password",3,"Lee")

        AU.EditUser.change_password(self)

        user = TR.get_user('Brian')

        result = cryptocode.decrypt(user.password, ENTRY)

        self.assertEqual(result,expected)


    def test_update_level(self):
        print("Test update level")

        expected = 4

        user = self.this_user

        self.edit_user.change_level(4)

        result = user.level

        self.assertEqual(expected, result)

       


    def test_change_trainer(self):
        print("Test change trainer")

        expected = "Jon"

        user = self.this_user

        self.edit_user.change_trainer("Jon")

        result = user.trainer

        self.assertEqual(expected, result)


    def test_delete_user(self):
        print("Test delete user")

        expected = None

        user = self.added_user
   

        deleted = self.delete_user.delete_user("Jack")

        result = user.name

        self.assertEqual(expected, result)
        self.assertEqual(deleted,True)









   

if __name__ == '__main__':
    unittest.main()