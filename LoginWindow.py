'''
Created on 9 March 2022


@Author by Brian F



'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import Login
import Screen
import User
import interface
import Training
import AdminUser

UL = Login
SC = Screen
US = User
INT = interface.interface()
TR = Training.Training()
AU = AdminUser


class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        ##############################
        # Setup attributes of class  #
        ##############################
        # ws = self.winfo_screenwidth()
        # hs = self.winfo_screenheight()
        tk.Frame.__init__(self, parent, bg='#8D8DAA')
        self.control = controller
        self.canvas_name = Canvas()
        self.canvas_pass = Canvas()
        self.username = StringVar()
        self.password = StringVar()
        self.logged_in = False
        self.x = 350
        self.y1 = 225
        self.y2 = 320
        self.base = Canvas(self,bg="#FBF8F1",width=1280, height=830)
        self.base.place(x=10, y=10)


    def refresh_window(self):
        ################################################################
        # Set up of the canvas screen locations for the login          #
        ################################################################
        self.username.set("")
        self.canvas_name = Canvas(self,bg="#E9DAC1",width=500, height=85)
        self.canvas_name.place(x=self.x, y=self.y1)
        self.canvas_pass = Canvas(self,bg="#E9DAC1",width=500, height=85)
        self.canvas_pass.place(x=self.x, y=self.y2)
        Label(self,text="Training Database",font=("Courier", 24, 'bold')).place(x=330,y=80)
        Label(self,text="Please Log in",font=("Courier", 20)).place(x=380,y=180)
        Label(self.canvas_name, text="Username", font=('Courier',18)).place(x=20,y=16)
        Label(self.canvas_pass, text="Password", font=('Courier', 18)).place(x=20,y=16)
        Button(self.base, text="Forgot password", command=self.forgot, bg="#FBF8F1").place(x=380, y=420)

        ##############################################################################
        # Get the username and the password from the user                            #
        ##############################################################################
        name = Entry(self.canvas_name, textvariable=self.username,width=25, font=('Courier', 16))
        name.place(x=150, y=20)
        password = Entry(self.canvas_pass, textvariable=self.password, show="*",width=25, font=('Courier', 16))
        password.place(x=150, y=20)
        login_btn = Button(self,text="Log in", width=20, command=self.user_login, bg='#54BAB9', font=('Courier', 20))
        login_btn.place(x=600,y=500)
        password.bind('<Return>', self.user_login)
        name.focus_set()

    def user_login(self):
        ##############################################################################
        # When the working version is released, the username and password will be    #
        # replaced with the user input fields.                                       #
        ##############################################################################
        # username = "Brian"
        # password = "my-password"
        username = self.username.get().title()
        password = self.password.get()
        for user in TR.get_all_users():
            if username in user:
                username = user

        ##################################################
        # Send the user information to the login checker #
        # If it succeeds, the main screen will be shown  #
        ##################################################
        login = UL.Login(username,password)
        user = login.get_logged_in_user()
        ##################################################
        # Resets the user input areas for the next user  #
        ##################################################
        if user:
            INT.provide_interface([username])
            self.username.set("")
            self.password.set("")
            self.control.show_frame(SC.main_screen)

    def forgot(self):
        # Label(self.base, text="Coming Soon").place(relx=0.4, rely=0.8)
        found = False
        if not self.username.get():
            mb.showinfo(title="Username", message="Please enter your username to reset.")
        else:
            username = self.username.get().title()
            for user in TR.get_all_users():
                if username in user:
                    username = user
                    INT.provide_interface([username, True])
                    user_data = UL.Login.get_user_data(self)
                    for name in user_data:
                        if name["Name"] == username:
                            UL.Login.write_user(self, name['Name'], name['admin'])
                    found = True
            if not found:
                self.username.set("")
            else:
                AU.EditUser.reset_password(self)
                self.control.show_frame(AU.EditUser)

            self.refresh_window()

