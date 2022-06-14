import unittest
import Screen
from tkinter import *

SC = Screen

class ScreenTests(unittest.TestCase):

    def setUp(self):
        self.main = Tk()
        self.main.search_item = StringVar()
        self.finish = False

    def test_get_user(self):
        print("Test getting user")

        SC.main_screen.get_user(self.main)


if __name__ == '__main__':
        unittest.main()