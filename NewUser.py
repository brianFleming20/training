'''
Creates a new user for the training records system
'''

import tkinter as tk
from tkinter import *
from tkinter import filedialog
import Training
import interface
import Screen as SC
import User

TR = Training.Training()
INT = interface.interface()
US = User.User()

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
        self.depart = StringVar()
        self.comp = IntVar()
        self.document = StringVar()
        self.data = []
        self.value = False


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
        Label(self.canvas_back, text="Password ", bg="#E9DAC1").place(x=50,y=140)
        Label(self.canvas_back, text="Competency level ", bg="#E9DAC1").place(x=50,y=180)
        Label(self.canvas_back, text="Notes ", bg="#E9DAC1").place(x=50,y=220)
        Label(self.canvas_back, text="Document name", bg="#E9DAC1").place(x=50,y=340)
        name = Entry(self.canvas_back, textvariable=self.name,width=25).place(x=210, y=100)
        password = Entry(self.canvas_back, textvariable=self.depart,width=25).place(x=210, y=140)
        compency = Entry(self.canvas_back, textvariable=self.comp,width=15).place(x=210, y=180)
        text_area = tk.Text(self, height=4, width=30).place(x=220, y=310)
        docum = Entry(self.canvas_back, textvariable=self.document,width=30).place(x=210, y=340)
        Button(self.canvas_back, text="Add Document", command=self.add_document, width=14).place(x=350,y=390)
        Button(self.canvas_back, text="Add User", command=self.add_user,width=12 ,bg='#54BAB9',).place(x=680,y=500)
        admin = "On"

        Radiobutton(self.canvas_back, text = "  Trainer  ", variable = admin,
            value = self.value).place(x=120,y=450)

        US.set_name(name)
        US.set_password(password)
        US.set_training_level(compency)
        
        

        Label(self.canvas_back, text="Trained on ").place(x=500,y=50)
        doc_name = Listbox(self, height=20, width=18)
        doc_name.place(x=500, y=180)
        doc_ref = Listbox(self, height=20, width=18)
        doc_ref.place(x=650, y=180)
        doc_name.insert(END, "Document Name")
        doc_name.insert(END,"-----------------")
        doc_ref.insert(END, "Document Ref.")
        doc_ref.insert(END,"-----------------")


    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


    def show_users(self):
        self.control.show_frame(ShowUsers)


    def edit_user(self):
        self.control.show_frame(EditUser)


    def add_document(self):
        filename = filedialog.askopenfilename(initialdir="./Downloads", 
        title="Select Document",filetypes = (("pdf files","*.pdf"),("word files","*.docx"))) 
        print(filename)
        

    def add_user(self):
        print("Add user button pressed")


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
        Button(self.canvas_btndis,text="Show User", command=self.show_users, width=12 ,bg='#54BAB9').place(x=20,y=80)
        Button(self.canvas_btndis,text="Add User", command=self.add_user,width=12, bg='#54BAB9').place(x=20,y=160)
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="Edit User").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)


    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


    def show_users(self):
        self.control.show_frame(ShowUsers)


    def add_user(self):
        self.control.show_frame(AddNewUser)