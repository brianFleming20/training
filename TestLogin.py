import unittest

import Login
import User
import LoginWindow
import tkinter as tk


UL = Login
US = User.User()
LW = LoginWindow




class LoginTests(unittest.TestCase):

   
    def setUp(self):

        US.set_name("Brian")
        US.set_password("something")
        US.set_is_trainer(False)
        US.set_trainer("Lee")
        US.set_training_level(3)
        US.save_user()
       
        US.set_name("Lee")
        US.set_password("password")
        US.set_is_trainer(True)
        US.set_trainer("Alex")
        US.set_training_level(1)
        US.save_user()
     
        US.set_name("Jon")
        US.set_password("else")
        US.set_is_trainer(False)
        US.set_trainer("Lee")
        US.set_training_level(3)
        US.save_user()
        
        self.user = UL.Login("Lee","password") 
        self.newuser = UL.Login("Brian","something")
        self.unknown = UL.Login("Carey","batman")
        self.wrong = UL.Login("Jon","wrong one")

        self.parent = tk.Tk()
      
        

    def test_auser_obj(self):
        print("Test user object")

        expected1 = "Lee"
        expected2 = "Brian"
        ########################################

        user1 = self.user.get_user()
        
        result1 = user1.name
        admin = user1.is_trainer

        self.assertEqual(expected1, result1)
        self.assertEqual(admin, False)

        #########################################

        self.newuser.write_user()

        user2 = self.newuser.get_user()
        
        result2 = user2.name

        self.assertEqual(expected2,result2)
        ##########################################


    def test_buser_login(self):
        print("Test user login")

        expected = True

        result,admin = self.user.login_user()

        self.assertTrue(expected,result)



    def test_wrong_password(self):
        print("Test wrong password")

        expected = False
        result,admin = self.wrong.login_user()

        self.assertEqual(expected,result)


    def test_login_unknown_user(self):
        print("LOggin in unknown user")

        expected = False

        result,admin = self.unknown.login_user()

        self.assertEqual(expected,result)


    def test_login_is_trainer(self):
        print("Log in name and is trainer")

        expected = True

        user,result = self.user.login_user()

        self.assertEqual(result, expected)


    def test_login_window(self):
        print("Test user login from window")

        self.control = tk
        LW.LoginWindow.user_login(self)


    

        



if __name__ == '__main__':
    unittest.main()