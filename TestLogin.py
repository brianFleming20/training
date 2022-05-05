import unittest
import Training
import Login
import User
import LoginWindow
import tkinter as tk


UL = Login
UR = User
LW = LoginWindow
TR = Training.Training()



class LoginTests(unittest.TestCase):

   
    def setUp(self):

        self.user1 = UR.User("Brian","something",3,"Lee",False)

        self.user2 = UR.User("Lee","password",1,"Alex",True)
    
        self.user3 =UR.User("Jon","else",3,"Lee",False)
        
        self.user = UL.Login("Lee","password") 
        self.newuser = UL.Login("Brian","something")
        self.unknown = UL.Login("Carey","batman")
        self.wrong = UL.Login("Jon","wrong one")

        self.parent = tk.Tk()
      
        

    def test_auser_obj(self):
        print("\nTest user object")

        expected1 = "Lee"
        expected2 = "Brian"
        ##########################################
        # Does this user object get retrived from
        # the training class
        ##########################################

        
        user = TR.get_user("Brian")
        admin = user['is_trainer']

        self.assertEqual(admin, True)

        #########################################

        self.newuser.write_user(user)

        user2 = self.newuser.get_user()
        
        result2 = user2.name

        self.assertEqual(expected2,result2)
        ##########################################


    def test_buser_login(self):
        print("\nTest user login")

        expected = True

        result,admin = self.user.login_user()

        self.assertTrue(expected,result)



    def test_wrong_password(self):
        print("\nTest wrong password")

        expected = False
        result,admin = self.wrong.login_user()

        self.assertEqual(expected,result)


    def test_login_unknown_user(self):
        print("\nLoggin in unknown user")

        expected = False

        result,admin = self.unknown.login_user()

        self.assertEqual(expected,result)


    def test_login_is_trainer(self):
        print("\nLog in name and is trainer")

        expected = False

        user,result = self.user.login_user()

        print(f"user {user} : result {result}")

        self.assertEqual(result, expected)


    def test_login_window(self):
        print("\nTest user login from window")

        self.control = tk
        LW.LoginWindow.user_login(self)


    

        



if __name__ == '__main__':
    unittest.main()