import unittest
import User
import Login




UR = User




class UserTests(unittest.TestCase):

    def setUp(self):
        self.user = UR.User()
        this_user = self.user.get_user()
        self.change_user = UR.EditUser(this_user)
        self.delete_user = UR.DeleteUser(this_user)
 
    

    # Test no username  
    def test_get_user(self):
        print("Test get username")

        expected = "Brian"

        self.user.set_name("Brian")

        result = self.user.get_name()

        self.assertEqual(expected, result)


    def test_get_password(self):
        print("Test get password")

        expected = "mogo"

        self.user.set_password("mogo")

        result = self.user.get_password()

        self.assertEqual(expected, result)


    def test_get_level(self):
        print("Test get level")

        expected = 3

        self.user.set_training_level(3)

        result = self.user.get_training_level()

        self.assertEqual(expected, result)

    
    def test_get_trainer(self):
        print("Test get trainer")

        expected = "Lee"

        self.user.set_trainer("Lee")

        result = self.user.get_trainer()

        self.assertEqual(expected, result)



   



    def test_is_trainer(self):
        print("Test is trainer")

        expected = True

        self.user.set_is_trainer(True)

        result = self.user.get_is_trainer()

        self.assertEqual(expected, result)


    def test_update_username(self):
        print("Test change username")
    
        expected = "Clare"

        self.user.set_name("Brian")

        self.change_user.change_name("Clare")

        result = self.user.get_name()

        self.assertEqual(expected, result)


    def test_update_password(self):
        print("Test change password")

        expected = "the other"

        self.user.set_password("password")

        self.change_user.change_password("the other")

        result = self.user.get_password()

        self.assertEqual(expected, result)


    def test_update_level(self):
        print("Test update level")

        expected = 4

        self.user.set_training_level(2)

        self.change_user.change_level(4)

        result = self.user.get_training_level()

        self.assertEqual(expected, result)


    def test_add_new_doc(self):
        print("Test adding new document to user")

       


    def test_change_trainer(self):
        print("Test change trainer")

        expected = "Jon"

        self.user.set_trainer("Lee")

        self.change_user.change_trainer("Jon")

        result = self.user.get_trainer()

        self.assertEqual(expected, result)


    def test_delete_user(self):
        print("Test delete user")

        expected = None

        self.user.set_name("Jon")
        self.user.set_password("password")
        self.user.set_is_trainer(True)
        self.user.set_trainer("None")
   

        self.delete_user.delete_user("Jon")

        result = self.user.get_name()

        self.assertEqual(expected, result)



   

if __name__ == '__main__':
    unittest.main()