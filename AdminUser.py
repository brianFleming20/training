'''
Add users to the system
'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from time import gmtime, strftime
import Training
import User
import Screen as SC

TR = Training.Training()
USER = User.User()


class admin_user_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller
        self.canvas_btndis = Canvas(self,bg="#E9DAC1",width=120,height=630)
        self.canvas_btndis.place(x=840,y=10)
        self.canvas_srdis = Canvas(self,bg="#E9DAC1", width=810,height=50)
        self.canvas_srdis.place(x=10,y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810,height=560)
        self.canvas_back.place(x=10,y=80)
        self.name = StringVar()
        self.document = StringVar()
        self.time = StringVar()


    def refresh_window(self):
        self.time.set(TR.get_now_time())
        self.is_trainer()


    def show_screen(self,name):
        Button(self.canvas_btndis,text="New", width=12 ,bg='#54BAB9').place(x=20,y=80)
        Button(self.canvas_btndis,text="Delete", width=12, bg='#54BAB9').place(x=20,y=160)
        Button(self.canvas_btndis,text="Edit", width=12, bg='#54BAB9').place(x=20,y=240)
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="Admin User").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)
        Label(self.canvas_srdis, text="Trainer Name ").place(x=10,y=15)
      

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


    def is_trainer(self):
        user = USER.get_user()
        trainer = user.trainer
        print(user)
        if trainer:
            self.show_screen(user.name)
        else:
            self.return_to_home()