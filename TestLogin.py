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
        self.parent = tk.Tk()

    def test_b_user_login(self):
        print("\nTest user login")

        name = "Brian Fleming"
        password = "your password"
        user = UL.Login(name,password)

        result = user.get_logged_in_user()

        self.assertEqual(user.name, result)




    def test_wrong_password(self):
        print("\nTest wrong password")
        name = "Brian Fleming"
        password = "none"

        user = UL.Login(name, password)

        result = user.get_logged_in_user()

        self.assertEqual(result, False)



    def test_login_unknown_user(self):
        print("\nLoggin in unknown user")

        name = "Jim"
        password = "none"

        user = UL.Login(name, password)

        result = user.get_logged_in_user()

        self.assertEqual(result,False)


if __name__ == '__main__':
    unittest.main()