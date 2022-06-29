import unittest
import Screen
from tkinter import *
import Training

SC = Screen
TR = Training.Training()

class ScreenTests(unittest.TestCase):

    def setUp(self):
        self.parent = Tk()
        self.controller = Tk()
        self.parent.search_item = StringVar()

        self.finish = False

    def test_get_user(self):
        print("Test getting user")
        expected = "Carey Grey"
        SCR = SC.main_screen(self.parent, self.controller)
        SCR.search_item.set(expected)
        SCR.finish = False
        result = SCR.get_selected_name()
        self.assertEqual(result,expected)


    def test_get_document_name_from_id(self):
        print("Show the document name from its document reference number")
        SCR = SC.main_screen(self.parent,self.controller)
        document_ref = "9070-1203"
        expected = "Doppler Probe Assembly Procedure"

        SCR.search_doc.set(document_ref)

        data = SCR.get_document_requested()
        SCR.check_data()
        result = SCR.search_document.get()
        self.assertEqual(result, expected)


if __name__ == '__main__':
        unittest.main()