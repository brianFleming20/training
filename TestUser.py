import unittest
import User


UR = User


class UserTests(unittest.TestCase):

    def setUp(self):
        user = UR.User("Brian","mogo",3,"Lee",True)
        self.this_user = user
        self.edit_user = UR.EditUser(self.this_user)
        self.added_user = UR.User("Jack","password",2)
        self.delete_user = UR.DeleteUser(self.added_user)



    def test_update_username(self):
        print("Test change username")
    
        expected = "Clare"

        user = self.edit_user

        user.change_name("Clare")

        result = self.this_user.name

        self.assertEqual(expected, result)


    def test_update_password(self):
        print("Test change password")

        expected = "the other"

        user = self.this_user

        self.edit_user.change_password("the other")

        result = user.password

        self.assertEqual(expected, result)


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