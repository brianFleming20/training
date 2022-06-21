import unittest
import AdminUser
import Training
from tkinter import *
import interface

IN = interface.interface()
AU = AdminUser
AUT = AdminUser
TR = Training.Training()


class AdminTests(unittest.TestCase):

    def setUp(self):
        self.parent = Tk()
        self.controller = Tk()
        self.adduser = AU.AddNewUser(self.parent, self.controller)
        self.show = AU.ShowUsers(self.parent, self.controller)
        self.edit = AU.EditUser(self.parent, self.controller)
        self.add_doc = AU.addNewDocument(self.parent, self.controller)
        self.show.documents = Listbox(self.parent ,exportselection=False)
        self.show.users = Listbox(self.parent ,exportselection=False)
        self.show.control.show_frame = Tk()

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

        result = self.adduser.create_user(name,password,conf_pass,email, admin,encrypt, trainer, administrator)

        self.assertEqual(result, True)


    def test_set_admin_state(self):
        print("Test set admin state")

        expected = True
        self.adduser.set_admin_state(True)
        result = self.adduser.get_admin_state()

        self.assertEqual(expected, result)

    def test_update_overwrite(self):
        print("Test update over write")

        self.adduser.update_overwrite()
        result1 = self.adduser.get_admin()

        self.assertEqual(True, result1)
        self.adduser.update_overwrite()
        result2 = self.adduser.get_admin()

        self.assertEqual(False, result2)

    def test_administrator(self):
        print("Test administrator settings")

        self.adduser.update_admin()
        result1 = self.adduser.get_administrator()
        self.assertEqual(1,result1)

        self.adduser.update_admin()
        result2 = self.adduser.get_administrator()
        self.assertEqual(0, result2)

    def test_edit_doc(self):
        print("Test edit doc")
        doc = "9070-1209"
        self.show.documents.insert(END,doc)
        self.show.documents.select_set(0)
        self.show.edit_doc("event")
        result = IN.extend_interface()[0]
        self.assertEqual(doc,result)


    def test_edit_user(self):
        print("Test edit user")
        user = "Jack"
        self.show.users.insert(END, user)
        self.show.users.select_set(0)
        self.show.edit_user("event")
        result = IN.extend_interface()[0]

        self.assertEqual(user,result)

    def test_update_trainer(self):
        print("Test update is trainer")

        expected = True
        self.edit.update_trainer()
        result1 = self.edit.get_admin()
        self.assertEqual(expected, result1)

        self.edit.update_trainer()
        result2 = self.edit.get_admin()
        self.assertEqual(False, result2)

    def test_update_user(self):
        print("Test update user")
        user = TR.get_blank_user()
        user.name = "Fred"
        user.email = "non yet"
        user.is_trainer = False
        user.trainer = "Lee"
        expected = user.name
        self.edit.set_for_test("password",2,"Lee",user.name)
        result_user = self.edit.update_user()
        result = result_user.name
        self.assertEqual(expected, result)


    def test_add_new_document(self):
        print("Test add new document")
        self.add_doc.name.set("Da document")
        self.add_doc.doc_issue.set(5)
        self.add_doc.doc_reference.set("1234-5678")

        self.add_doc.add_new_document()


    def test_register_training(self):
        print("test register training")

    def test_check_data(self):
        print("test check data")




if __name__ == '__main__':
    unittest.main()