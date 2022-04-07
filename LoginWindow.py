'''
Created on 9 March 2022


@Author by Brian F



'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from time import gmtime, strftime
import Login
import Screen
import User

UL = Login
SC = Screen
US = User.User()


class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller
        self.canvas_name = Canvas()
        self.canvas_pass = Canvas()
        self.username = StringVar()
        self.password = StringVar()
        self.logged_in = False
        self.x = 350
        self.y1 = 225
        self.y2 = 300
        self.base = Canvas(self,bg="#FBF8F1",width=980, height=680)
        self.base.place(x=10, y=10)


    def refresh_window(self):
        self.canvas_name = Canvas(self,bg="#E9DAC1",width=400, height=55)
        self.canvas_name.place(x=self.x, y=self.y1)

        self.canvas_pass = Canvas(self,bg="#E9DAC1",width=400, height=55)
        self.canvas_pass.place(x=self.x, y=self.y2)

        Label(self.canvas_name, text="Username").place(x=20,y=16,width=80)
        Label(self.canvas_pass, text="Password").place(x=20,y=16,width=80)
      
        name = Entry(self.canvas_name, textvariable=self.username,width=30)
        name.place(x=150, y=16)
        password = Entry(self.canvas_pass, textvariable=self.password,width=30)
        password.place(x=150, y=16)
        
        Button(self,text="Log in", width=30, command=self.user_login,bg='#54BAB9').place(x=600,y=500)



        

    def user_login(self):
        
        username = "Lee"
        password = "password"
        # username = self.username.get()
        # password = self.password.get()
        login = UL.Login(username,password)
        user,admin = login.login_user()
        print(f"user {user} : logged user {login.password}")
        if user:
            print("User loggin in")
            US.set_is_trainer(admin)
            
            self.control.show_frame(SC.main_screen)
        else:
            print("user not logged in")
            mb.showerror(title="User Error",message="User not logged in.")