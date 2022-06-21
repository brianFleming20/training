'''
Created on 9 March 2022


@Author by Brian F



'''

import tkinter as tk
from tkinter import *
import Login
import Screen
import User
import interface

UL = Login
SC = Screen
US = User
INT = interface.interface()


class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        ##############################
        # Setup attributes of class  #
        ##############################
        tk.Frame.__init__(self, parent, bg='#8D8DAA')
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
        ################################################################
        # Set up of the canvas screen locations for the login          #
        ################################################################
        self.canvas_name = Canvas(self,bg="#E9DAC1",width=400, height=55)
        self.canvas_name.place(x=self.x, y=self.y1)
        self.canvas_pass = Canvas(self,bg="#E9DAC1",width=400, height=55)
        self.canvas_pass.place(x=self.x, y=self.y2)
        Label(self,text="Training Database",font=("Courier", 22, 'bold')).place(x=330,y=80)
        Label(self,text="Please Log in",font=("Courier", 16)).place(x=380,y=180)
        Label(self.canvas_name, text="Username").place(x=20,y=16,width=80)
        Label(self.canvas_pass, text="Password").place(x=20,y=16,width=80)

        ##############################################################################
        # Get the username and the password from the user                            #
        ##############################################################################
        name = Entry(self.canvas_name, textvariable=self.username,width=30)
        name.place(x=150, y=16)
        password = Entry(self.canvas_pass, textvariable=self.password, show="*",width=30)
        password.place(x=150, y=16)
        Button(self,text="Log in", width=30, command=self.user_login,bg='#54BAB9').place(x=600,y=500)

    def user_login(self):
        ##############################################################################
        # When the working version is released, the username and password will be    #
        # replaced with the user input fields.                                       #
        ##############################################################################
        username = "Brian Fleming"
        password = "password"
        # username = self.username.get()
        # password = self.password.get()
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
