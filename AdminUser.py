'''
Creates a new user for the training records system
'''

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import Training
import interface
import Screen as SC
import User

TR = Training.Training()
INT = interface.interface()
UR = User

class AddNewUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller

        self.canvas_btndis = Canvas(self,bg="#E9DAC1",width=120,height=630)
        self.canvas_btndis.place(x=840,y=10)
        self.canvas_srdis = Canvas(self,bg="#E9DAC1", width=810,height=50)
        self.canvas_srdis.place(x=10,y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810,height=560)
        self.canvas_back.place(x=10,y=80)
        self.serach_item = StringVar()
        self.time = StringVar()
        self.doc_id = StringVar()
        self.name = StringVar()
        self.passw = StringVar()
        self.conf_pass = StringVar()
        self.comp = IntVar()
        self.document = StringVar()
        self.data = []
        self.admin = False
        self.admin_state = IntVar()


    def refresh_window(self):
        self.time.set(TR.get_now_time())
        self.data.clear()
        self.canvas_back.delete('all')
        Button(self.canvas_btndis,text="Edit User", command=self.edit_user, width=12 ,bg='#54BAB9').place(x=20,y=80)
        Button(self.canvas_btndis,text="Show Users", command=self.show_users, width=12, bg='#54BAB9').place(x=20,y=160)
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="New User").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)
        Label(self.canvas_back, text="Name " ,bg="#E9DAC1").place(x=50,y=100)
        Label(self.canvas_back, text="New Password ", bg="#E9DAC1").place(x=50,y=140)
        Label(self.canvas_back, text="Confirm Password ", bg="#E9DAC1").place(x=50,y=180)
        Label(self.canvas_back, text="Competency level ", bg="#E9DAC1").place(x=50,y=220)
       
        name = Entry(self.canvas_back, textvariable=self.name,width=25).place(x=210, y=100)
        password = Entry(self.canvas_back, textvariable=self.passw,width=25).place(x=210, y=140)
        conf_password = Entry(self.canvas_back, textvariable=self.conf_pass,width=25).place(x=210, y=180)
        compency = Entry(self.canvas_back, textvariable=self.comp,width=15).place(x=210, y=220)
       
        Button(self.canvas_back, text="Add User", command=self.add_user(name,password,conf_password,compency),width=12 ,bg='#54BAB9',).place(x=680,y=500)


        self.checkbutton = Checkbutton(text="   Trainer    ", 
                                  variable=self.admin_state,command=self.update_overwrite, font=("Courier",10))
                                  
        self.admin_state.get()
        self.checkbutton.place(x=80, y=520)

        

    def set_admin_state(self, state):
        self.admin_state.set(state)


    def update_overwrite(self):
        if self.admin == False:
            self.admin = True
        else:
            self.admin = False
      

            
    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


    def show_users(self):
        self.control.show_frame(ShowUsers)


    def edit_user(self):
        self.control.show_frame(EditUser)


    # def add_document(self):
    #     filename = filedialog.askopenfilename(initialdir="./Downloads", 
    #     title="Select Document",filetypes = (("pdf files","*.pdf"),("word files","*.docx"))) 
    #     print(filename)
    #     self.document.set(filename)

        

    def add_user(self,name,password,conf_pass,comp):
        USER = UR.User
        if password == conf_pass:
            user = UR.User(name,password,level=comp,trainer=self.admin)
            USER.save_user(user)
            return True
            
        else:
            mb.showerror(title="User Error",message="Your passwords don't match.")
            return False
        

class ShowUsers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller

        self.canvas_btndis = Canvas(self,bg="#E9DAC1",width=120,height=630)
        self.canvas_btndis.place(x=840,y=10)
        self.canvas_srdis = Canvas(self,bg="#E9DAC1", width=810,height=50)
        self.canvas_srdis.place(x=10,y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810,height=560)
        self.canvas_back.place(x=10,y=80)
        self.canvas_lists = Canvas(self, bg="#F7ECDE", width=810,height=560)
        self.canvas_lists.place(x=10,y=80)
        self.serach_item = StringVar()
        self.time = StringVar()
        self.doc_id = StringVar()
        self.data = []


    def refresh_window(self):
        self.time.set(TR.get_now_time())
        self.data.clear()
        self.data.extend(INT.extend_interface())
        self.canvas_back.delete('all')
        Button(self.canvas_btndis,text="New User", command=self.add_new_user, width=12 ,bg='#54BAB9').place(x=20,y=80)
        Button(self.canvas_btndis,text="Edit User", command=self.edit_user,width=12, bg='#54BAB9').place(x=20,y=160)
        Button(self.canvas_btndis,text="Delete User",command=self.delete_user, width=12, bg='#54BAB9').place(x=20,y=240)
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="New User").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)
        Label(self.canvas_lists, text="Trained Users").place(x=20, y=18)
        self.users = Listbox(self.canvas_lists,exportselection=False)
        self.users.place(x=20, y=45)
        self.users.config(height=20, width=40, bg="#E9DAC1")
        

        for no in TR.get_all_users():
            self.users.insert(END, no)


    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


    def add_new_user(self):
        self.control.show_frame(AddNewUser)


    def edit_user(self):
        self.control.show_frame(EditUser)

    def delete_user(self):
        pass

class EditUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller

        self.canvas_btndis = Canvas(self,bg="#E9DAC1",width=120,height=630)
        self.canvas_btndis.place(x=840,y=10)
        self.canvas_srdis = Canvas(self,bg="#E9DAC1", width=810,height=50)
        self.canvas_srdis.place(x=10,y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810,height=560)
        self.canvas_back.place(x=10,y=80)
        self.canvas_back = Canvas(self, bg="#F7ECDE", width=810,height=560)
        self.canvas_back.place(x=10,y=80)
        self.serach_item = StringVar()
        self.time = StringVar()
        self.doc_id = StringVar()
        self.name = StringVar()
        self.passw = StringVar()
        self.conf_pass = StringVar()
        self.comp = IntVar()
        self.data = []


    def refresh_window(self):
        self.time.set(TR.get_now_time())
        self.data.clear()
        self.data.extend(INT.extend_interface())
        self.canvas_back.delete('all')
        Button(self.canvas_btndis,text="Show User", command=self.show_users, width=12 ,bg='#54BAB9').place(x=20,y=80)
        Button(self.canvas_btndis,text="Add User", command=self.add_user,width=12, bg='#54BAB9').place(x=20,y=160)
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="Edit User").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)

        Label(self.canvas_back, text="New Name " ,bg="#E9DAC1").place(x=50,y=100)
        Label(self.canvas_back, text="New Password ", bg="#E9DAC1").place(x=50,y=140)
        Label(self.canvas_back, text="Confirm Password ", bg="#E9DAC1").place(x=50,y=180)
        Label(self.canvas_back, text="Change Competency level ", bg="#E9DAC1").place(x=50,y=220)

        name = Entry(self.canvas_back, textvariable=self.name,width=25).place(x=210, y=100)
        password = Entry(self.canvas_back, textvariable=self.passw,width=25).place(x=210, y=140)
        conf_password = Entry(self.canvas_back, textvariable=self.conf_pass,width=25).place(x=210, y=180)
        compency = Entry(self.canvas_back, textvariable=self.comp,width=15).place(x=210, y=220)

        Button(self.canvas_back, text="Change Name", command=self.change_name(name), width=14).place(x=400,y=100)
        Button(self.canvas_back, text="Update Password", command=self.change_password(password,conf_password), width=14).place(x=400,y=180)
        Button(self.canvas_back, text="Change Level", command=self.change_level(compency), width=14).place(x=400,y=220)


    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


    def show_users(self):
        self.control.show_frame(ShowUsers)


    def add_user(self):
        self.control.show_frame(AddNewUser)


    def change_name(self,name):
        pass


    def change_password(self,passw,conf):
        pass


    def change_level(self,level):
        pass