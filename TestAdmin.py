import unittest
import AdminUser
import Training
from tkinter import *
import tkinter as tk


AU = AdminUser
AUT = AdminUser
TR = Training.Training()


class AdminTests(unittest.TestCase):

    def setUp(self):
        self.parent = Tk()
        self.cb = StringVar()
        self.doc_reference = StringVar()
        self.name = StringVar()
        self.canvas = Canvas(self.parent,  height=8, width=35)
        self.note = tk.Text(self.parent, height=8, width=35)


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

        result = AU.AddNewUser.create_user(self.parent,name,password,conf_pass,email, admin,encrypt, trainer, administrator)

        self.assertEqual(result, True)

    def test_record_training(self):
        print("Record new training")
        self.cb.set("Jon")
        self.doc_reference.set("9070-1203")
        self.name.set("Jon")

        AU.RecordTraining.register_training(self)




if __name__ == '__main__':
    unittest.main()