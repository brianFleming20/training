import unittest
import DisplayScreens
import tkinter as tk

DS = DisplayScreens

class DisplayScreenTest(unittest.TestCase):

    def generate_email(self,user,ref):
        print(f"send email {user} : {ref}")

    def generate_email_reminder(self, user, ref):
        print(f"overdue email {user} : {ref}")

    def setUp(self):

        self.parent = tk.Tk()
        self.canvas_back = tk.Canvas(self.parent, width=120, height=630)

    def test_sent_email(self):
        print("Test send email to user and trainer")

        expected = True

        result = DS.show_event_window.check_for_email(self)

        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()