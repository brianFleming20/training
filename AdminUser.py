'''
Creates a new user for the training records system
'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
import Training
import Screen as SC
import User
import Documents
import AccessDataBase
import cryptocode
import interface


TR = Training.Training()
INT = interface.interface()
UR = User
DOC = Documents
AS = AccessDataBase.GetExternalData()

ENTRY = "ByH1KHdo7y30I6aN"


class AddNewUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.adminbutton = None
        self.checkbutton = None
        self.logged_in = None
        self.control = controller
        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=120, height=630)
        self.canvas_btndis.place(x=840, y=10)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=810, height=50)
        self.canvas_srdis.place(x=10, y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810, height=560)
        self.canvas_back.place(x=10, y=80)
        self.serach_item = StringVar()
        self.time = StringVar()
        self.doc_id = StringVar()
        self.name = StringVar()
        self.passw = StringVar()
        self.conf_pass = StringVar()
        self.comp = IntVar()
        self.document = StringVar()
        self.email = StringVar()
        self.data = []
        self.admin = False
        self.administrator = False
        self.administrator_state = IntVar()
        self.admin_state = IntVar()

    def refresh_window(self):
        ##################################################################
        # Sets the date now                                              #
        ##################################################################
        self.time.set(TR.get_date_now())
        self.data.clear()
        self.canvas_back.delete('all')
        ##################################################################
        # Gets the logged in user                                        #
        ##################################################################
        self.logged_in = TR.get_user(TR.get_logged_in_user())
        ##################################################################
        # Sets up the display for adding a user                          #
        ##################################################################
        Button(self.canvas_btndis, text="Show Users", command=self.show_users, width=12, bg='#54BAB9').place(x=20,
                                                                                                             y=160)
        Button(self.canvas_btndis, text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="New User").place(x=10, y=15)

        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_back, text="Name ", bg="#E9DAC1").place(x=50, y=100)
        Label(self.canvas_back, text="New Password ", bg="#E9DAC1").place(x=50, y=140)
        Label(self.canvas_back, text="Confirm Password ", bg="#E9DAC1").place(x=50, y=180)
        Label(self.canvas_back, text="Email address",bg="#E9DAC1").place(x=50, y=250)
        ####################################################################
        # Gets the user interaction data                                   #
        ####################################################################
        name = Entry(self.canvas_back, textvariable=self.name, width=35)
        name.place(x=210, y=100)
        password = Entry(self.canvas_back, textvariable=self.passw, width=25)
        password.place(x=210, y=140)
        conf_password = Entry(self.canvas_back, textvariable=self.conf_pass, width=25)
        conf_password.place(x=210, y=180)
        email = Entry(self.canvas_back, textvariable=self.email, width=40)
        email.place(x=210, y=260)
        #######################################################################
        # Sets up and checks for the logged in user is a trainer and sets     #
        # the checkbox to the users trainer state                             #
        #######################################################################
        self.checkbutton = Checkbutton(self.canvas_back, text="   Trainer    ",
                                       variable=self.admin_state, command=self.update_overwrite, font=("Courier", 10))
        self.admin_state.get()
        self.checkbutton.place(x=80, y=520)
        btn5 = Button(self.canvas_back, text="Add User", command=self.show_users_screen, width=12, bg='#54BAB9')
        btn5.place(x=680, y=500)
        #######################################################################
        # Sets up and checks for the logged in user is an admin and sets      #
        # the checkbox to the users admin state                               #
        #######################################################################
        if self.logged_in['is_trainer']:
            self.adminbutton = Checkbutton(self.canvas_back, text="   Admin    ",
                                           variable=self.administrator_state, command=self.update_admin,
                                           font=("Courier", 10))
            self.administrator_state.get()
            self.adminbutton.place(x=80, y=480)

    def set_admin_state(self, state):
        self.admin_state.set(state)

    # this represents the user as a trainer
    def update_overwrite(self):
        if not self.admin:
            self.admin = True
        else:
            self.admin = False

    # this represents as an administrator
    def get_admin(self):
        return self.admin

    def get_admin_state(self):
        return self.admin_state.get()

    def update_admin(self):
        if not self.administrator:
            self.administrator = 1
        else:
            self.administrator = 0

    def get_administrator(self):
        return self.administrator

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def show_users(self):
        self.control.show_frame(ShowUsers)

    def add_user(self):
        encrypt_password = cryptocode.encrypt(self.passw.get(), ENTRY)
        if self.name.get() == "" or self.passw.get() == "" or self.email.get() == "":
            mb.showerror(title="Entry Error", message="Some of the fields are empty, \ntry again.")
            return False
        else:
            if self.create_user(self.name.get(), self.passw.get(), self.conf_pass.get(),
                                self.email.get(), self.admin, encrypt_password,
                                self.administrator):
                return True

            else:
                mb.showerror(title="User Error", message="User not created.")
                return False

    def create_user(self, name, password, conf_pass, email, admin,encrypt,administrator):
        if password == conf_pass:
            user = UR.User(name=name,is_trainer=admin, email=email)
            TR.save_user(user)
            TR.save_user_login(user, encrypt, administrator)
            return True
        else:
            mb.showerror(title="User Error", message="Your passwords don't match.")
            return False

    def show_users_screen(self):
        if self.add_user():
            self.control.show_frame(ShowUsers)


class ShowUsers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller

        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=120, height=630)
        self.canvas_btndis.place(x=840, y=10)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=810, height=50)
        self.canvas_srdis.place(x=10, y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810, height=560)
        self.canvas_back.place(x=10, y=80)
        self.canvas_lists = Canvas(self, bg="#F7ECDE", width=810, height=560)
        self.canvas_lists.place(x=10, y=80)
        self.serach_item = StringVar()
        self.time = StringVar()
        self.doc_id = StringVar()
        self.data = []

    def refresh_window(self):
        self.index = -1
        self.time.set(TR.get_date_now())
        self.data.clear()
        self.data.extend(INT.extend_interface())
        self.canvas_back.delete('all')
        btn1 = Button(self.canvas_btndis, text="New User", command=self.add_new_user, width=12, bg='#54BAB9')
        btn1.place(x=20, y=70)
        btn2 = Button(self.canvas_btndis, text="Add Document", command=self.add_document, width=12, bg='#54BAB9')
        btn2.place(x=20, y=150)
        Button(self.canvas_btndis, text="Record Training", command=self.training, width=12, bg='#54BAB9').place(x=20,
                                                                                                                y=220)
        Button(self.canvas_btndis, text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20, y=550)
        Label(self.canvas_srdis, text="New User").place(x=10, y=15)

        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_lists, text="Click on an item to edit",bg='#E9DAC1', font=("Courier", 14)).place(x=150, y=15)
        Label(self.canvas_lists, text="Trained Users").place(x=20, y=48)
        Label(self.canvas_lists, text="Documents").place(x=280, y=48)
        self.users = Listbox(self.canvas_lists, exportselection=False)
        self.users.place(x=20, y=85)
        self.users.config(height=20, width=20, bg="#E9DAC1")
        self.documents = Listbox(self.canvas_lists, exportselection=False)
        self.documents.place(x=250, y=85)
        self.documents.config(height=20, width=45, bg="#E9DAC1")


        for no in TR.get_all_users():
            self.users.insert(END, no)
            self.users.bind('<<ListboxSelect>>', self.edit_user)

        for ref, doc in TR.get_documents().items():
            self.documents.insert(END, f"{ref} - {doc['name']} - {doc['issue']}")
            self.documents.bind('<<ListboxSelect>>', self.edit_doc)

        admin = TR.get_user_admin()
        if admin:
            btn1.config(state=NORMAL)
            btn2.config(state=NORMAL)
            Button(self.canvas_lists, text="Update System", width=12, command=self.display_update,
                   bg='#54BAB9').place(x=650, y=480)
        else:
            btn1.config(state=DISABLED)
            btn2.config(state=DISABLED)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def add_new_user(self):
        self.control.show_frame(AddNewUser)

    def add_document(self):
        self.control.show_frame(addNewDocument)

    def training(self):
        self.control.show_frame(RecordTraining)

    def edit_doc(self, event):
        # show doc details for edit
        self.edit_current_doc(event)
        self.control.show_frame(editDocument)

    def edit_current_doc(self, event):
        idx = int(self.documents.curselection()[0])
        num = self.documents.get(idx)
        INT.provide_interface([num])

    def display_update(self):
        AS.get_user_info()


    def edit_user(self, event):
        self.edit_current_user(event)
        self.control.show_frame(EditUser)

    def edit_current_user(self, event):
        self.index = int(self.users.curselection()[0])
        data_user = self.users.get(self.index)
        INT.provide_interface([data_user])


class EditUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.checkbutton = None
        self.admin_state = BooleanVar()
        self.control = controller

        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=120, height=630)
        self.canvas_btndis.place(x=840, y=10)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=810, height=50)
        self.canvas_srdis.place(x=10, y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810, height=560)
        self.canvas_back.place(x=10, y=80)
        self.canvas_back = Canvas(self, bg="#F7ECDE", width=810, height=560)
        self.canvas_back.place(x=10, y=80)
        self.serach_item = StringVar()
        self.time = StringVar()
        self.doc_id = StringVar()
        self.name = StringVar()
        self.passw = StringVar()
        self.conf_pass = StringVar()
        self.email = StringVar()
        self.trainer = StringVar()
        self.comp = IntVar()
        self.admin = False
        self.data = []

    def refresh_window(self):
        self.time.set(TR.get_date_now())
        self.data.clear()
        self.data.extend(INT.extend_interface())
        self.canvas_back.delete('all')
        Button(self.canvas_btndis, text="Show User", command=self.show_users, width=12, bg='#54BAB9').place(x=20, y=80)
        btn1 = Button(self.canvas_btndis, text="Remove User", command=self.delete_user, width=12, bg='#54BAB9')
        btn1.place(x=20,y=150)
        Button(self.canvas_btndis, text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="Edit User").place(x=10, y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item, width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)

        Label(self.canvas_back, text="Username ", bg="#E9DAC1").place(x=50, y=100)
        Label(self.canvas_back, text="New Password ", bg="#E9DAC1").place(x=50, y=140)
        Label(self.canvas_back, text="Confirm Password ", bg="#E9DAC1").place(x=50, y=180)
        Label(self.canvas_back, text="Change Competency level ", bg="#E9DAC1").place(x=50, y=220)
        Label(self.canvas_back, text="Change Email address ", bg="#E9DAC1").place(x=50, y=260)

        self.name.set(self.data[0])
        Label(self.canvas_back, text=self.name.get(), width=25, font='Helvetica 12 bold').place(x=210, y=100)
        password = Entry(self.canvas_back, textvariable=self.passw, width=30)
        password.place(x=210, y=140)
        conf = Entry(self.canvas_back, textvariable=self.conf_pass, width=30)
        conf.place(x=210, y=180)
        comp = Entry(self.canvas_back, textvariable=self.comp, width=15)
        comp.place(x=210, y=220)
        email = Entry(self.canvas_back, textvariable=self.email, width=40)
        email.place(x=210, y=260)

        self.checkbutton = Checkbutton(self.canvas_back, text="   Trainer    ",
                                       variable=self.admin_state, command=self.update_trainer, font=("Courier", 10))
        self.admin_state.get()
        self.checkbutton.place(x=80, y=520)
        user = TR.get_user(self.name.get())
        self.admin_state.set(user['is_trainer'])
        admin = TR.get_user_admin()
        if admin:
            btn1.config(state=NORMAL)
        else:
            btn1.config(state=DISABLED)

        user_password = TR.get_user_password(self.name.get())
        if user_password:
            try:
                self.comp.set(user['level'])
                self.email.set(user['email'])
            except:
                pass
        else:
            mb.showerror(title="User Error", message="User cannot be displayed fully,\nmissing entries,"
                                                     "\nPlease complete..")
        btn6 = Button(self.canvas_back, text="Update user", command=self.update, width=14,  bg='#54BAB9')
        btn6.place(x=400, y=520)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def show_users(self):
        self.control.show_frame(ShowUsers)

    def add_user(self):
        self.control.show_frame(AddNewUser)

    def delete_user(self):
        if mb.askyesno(title="Delete User",message=f"Are you sure you want to remove \n{self.name.get()} \nfrom the system?"):
            result = TR.delete_user(self.name.get())
            if result:
                self.control.show_frame(ShowUsers)
            else:
                mb.showerror(title="Selection Error", message="Please select a user.")


    def update_trainer(self):
        if not self.admin:
            self.admin = True
        else:
            self.admin = False

    def get_admin(self):
        return self.admin

    def update_user(self):
        password = self.passw.get()
        if password == self.conf_pass.get():
            encrypt_password = cryptocode.encrypt(password, ENTRY)
            update_user = TR.get_blank_user()
            update_user.name = self.name.get()
            update_user.level = self.comp.get()
            update_user.is_trainer = self.admin
            update_user.password = encrypt_password
            update_user.email = self.email.get()
            TR.update_password(update_user.name, encrypt_password)
            return update_user
        else:
            mb.showerror(title="Password Error", message="Your passwords are not the same, \ntry again.")

    def update(self):
        update_user = self.update_user()
        TR.save_user(update_user)
        self.control.show_frame(ShowUsers)

    def set_for_test(self, password, level,name):
        self.passw.set(password)
        self.conf_pass.set(password)
        self.comp.set(level)
        self.name.set(name)


class addNewDocument(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller
        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=120, height=630)
        self.canvas_btndis.place(x=840, y=10)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=810, height=50)
        self.canvas_srdis.place(x=10, y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810, height=560)
        self.canvas_back.place(x=10, y=80)

        self.name = StringVar()
        self.doc_reference = StringVar()
        self.doc_issue = IntVar()
        self.doc_location = StringVar()
        self.time = StringVar()

    def refresh_window(self):
        self.time.set(TR.get_date_now())
        Label(self.canvas_srdis, text="Add a new document").place(x=10, y=15)
        Button(self.canvas_btndis, text="View Documents",
               command=self.documents, width=12, bg='#54BAB9').place(x=20, y=80)
        Button(self.canvas_btndis, text="Main", width=12,
               command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_back, text="Document Name",
              bg="#E9DAC1").place(x=50, y=100)
        Label(self.canvas_back, text="Document Reference No.",
              bg="#E9DAC1").place(x=50, y=140)
        Label(self.canvas_back, text="Document Issue No.",
              bg="#E9DAC1").place(x=50, y=180)

        self.doc_name = Entry(self.canvas_back, textvariable=self.name, width=45)
        self.doc_name.place(x=210, y=100)
        self.doc_ref = Entry(
            self.canvas_back, textvariable=self.doc_reference, width=30)
        self.doc_ref.place(x=210, y=140)
        self.doc_iss = Entry(
            self.canvas_back, textvariable=self.doc_issue, width=30)
        self.doc_iss.place(x=210, y=180)

        Button(self.canvas_back, text="Add Document", width=12,
               command=self.show_user_window,
               bg='#54BAB9', ).place(x=680, y=500)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def documents(self):
        self.control.show_frame(ShowUsers)

    def add_new_document(self):
        if self.name.get() == "" or self.doc_issue.get() == "" or self.doc_reference.get() == "":
            mb.showerror(title="Entry Error", message="Some of your inputs are empty, \ntry again.")
            return False
        else:
            self.add_doc()
            self.name.set("")
            self.doc_reference.set("")
            self.doc_issue.set(0)
            mb.showinfo(title="Document", message="New document has been added.")
            return True

    def add_doc(self):
        document = DOC.MakeDoc(name=self.name.get(), issue=self.doc_issue.get(), ref=self.doc_reference.get())
        TR.add_document(document)


    def show_user_window(self):
        if self.add_new_document():
            self.control.show_frame(ShowUsers)



class editDocument(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller
        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=120, height=630)
        self.canvas_btndis.place(x=840, y=10)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=810, height=50)
        self.canvas_srdis.place(x=10, y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810, height=560)
        self.canvas_back.place(x=10, y=80)
        self.name = StringVar()
        self.ref = StringVar()
        self.issue = StringVar()
        self.time = StringVar()
        self.data = []

    def refresh_window(self):
        self.time.set(TR.get_date_now())
        self.data.clear()
        self.data.extend(INT.extend_interface())
        reference_no = self.data[0]
        ref_num = reference_no[:9]
        ref = TR.get_a_document(ref_num)
        self.canvas_back.delete('all')
        Button(self.canvas_btndis, text="Show Users", command=self.show_documents, width=12, bg='#54BAB9').place(x=20, y=80)
        Button(self.canvas_btndis, text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="Edit Document").place(x=10, y=15)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_back, text="Document Name ", bg="#E9DAC1").place(x=50, y=100)
        Label(self.canvas_back, text="Document reference ", bg="#E9DAC1").place(x=50, y=140)
        Label(self.canvas_back, text="Issue number ", bg="#E9DAC1").place(x=50, y=180)

        Entry(self.canvas_back, textvariable=self.name, width=45).place(x=210, y=100)
        Entry(self.canvas_back, textvariable=self.ref, width=25).place(x=210, y=140)
        Entry(self.canvas_back, textvariable=self.issue, width=25).place(x=210, y=180)

        self.name.set(ref["name"])
        self.ref.set(ref_num)
        self.issue.set(ref["issue"])

        Button(self.canvas_back, text="Save Changes", command=self.save, width=12, bg='#54BAB9').place(x=550, y=450)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def show_documents(self):
        self.control.show_frame(ShowUsers)

    def save(self):
        doc = DOC.MakeDoc(name=self.name.get(), ref=self.ref.get(), issue=self.issue.get())
        TR.update_document(doc)
        self.control.show_frame(ShowUsers)


class RecordTraining(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller
        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=120, height=630)
        self.canvas_btndis.place(x=840, y=10)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=810, height=50)
        self.canvas_srdis.place(x=10, y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810, height=560)
        self.canvas_back.place(x=10, y=80)
        self.time = StringVar()
        self.name = StringVar()
        self.doc_reference = StringVar()
        self.training_date = StringVar()
        self.level = StringVar()
        self.doc_name = StringVar()
        self.doc_issue = IntVar()
        self.trainer = StringVar()
        self.cb = None
        self.finish = False
        self.note = ""
        self.data = ("0", "1", "2", "3", "4")

    def refresh_window(self):
        self.time.set(TR.get_date_now())
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Button(self.canvas_btndis, text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="Record Training").place(x=10, y=15)
        Label(self.canvas_back, text="Trainer", bg="#E9DAC1").place(x=50, y=40)
        Label(self.canvas_back, textvariable=self.trainer, bg="#E9DAC1").place(x=100, y=40)
        Label(self.canvas_back, text="Name", bg="#E9DAC1").place(x=50, y=80)
        Label(self.canvas_back, text="Document Reference No.", bg="#E9DAC1").place(x=350, y=80)
        Label(self.canvas_back, text="Training Level", bg="#E9DAC1").place(x=50, y=150)
        Label(self.canvas_back, text="Date Trained", bg="#E9DAC1").place(x=50, y=230)
        Label(self.canvas_back, text="Trainer", bg="#E9DAC1").place(x=50,y=300)
        Label(self.canvas_back, text="Training Note", bg="#E9DAC1").place(x=50, y=380)
        Label(self.canvas_back, text="Document Name", bg="#E9DAC1").place(x=350, y=150)
        Label(self.canvas_back, text="Issue Number", bg="#E9DAC1").place(x=350, y=230)

        names = TR.get_all_users()
        self.name.set("Choose")
        search_name = OptionMenu(self.canvas_back, self.name, *names)
        search_name.place(x=50, y=100)
        Entry(self.canvas_back, textvariable=self.doc_reference, width=25).place(x=350, y=100)
        Entry(self.canvas_back, textvariable=self.training_date, width=30).place(x=50, y=250)
        Entry(self.canvas_back, textvariable=self.trainer, width=30).place(x=50,y=320)
        Label(self.canvas_back, textvariable=self.doc_name, bg="#E9DAC1").place(x=350, y=170)
        Label(self.canvas_back, textvariable=self.doc_issue, bg="#E9DAC1").place(x=350, y=250)
        self.doc_name.set("Doc name")
        self.doc_issue.set(0)
        self.trainer.set("current user")

        self.cb = Combobox(self.canvas_back, values=self.data)
        self.cb.place(x=50, y=170)
        self.cb.current(0)
        self.trainer.set(TR.get_logged_in_user())
        self.note = tk.Text(self.canvas_back, height=8, width=35)
        self.note.place(x=50, y=400)
        self.training_date.set(TR.get_date_now())
        self.fill_form()

    def show_train_button(self):
        Button(self.canvas_back, text="Register Training", width=20, command=self.register_training,
               bg='#54BAB9').place(x=400, y=500)

    def fill_form(self):
        if not self.finish:
            self.control.after(1000, func=self.check_data)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def register_training(self):
        value = self.cb.get()
        if TR.register_trained(self.doc_reference, self.name.get(), value,self.trainer.get(), self.note.get('1.0', END)):
            mb.showinfo(title="Training Info", message="Training registered to system.")
        else:
            mb.showerror(title="Training Info", message="Something went wrong \n Training not registered to system.")

    def check_data(self):
        doc = TR.get_a_document(self.doc_reference.get())
        training_data = TR.get_training_record(self.name.get(), self.doc_reference.get())
        if not doc:
            pass
        else:
            self.doc_name.set(doc['name'])
            self.doc_issue.set(doc['issue'])

        if not training_data:
            pass
        else:
            self.cb.current(training_data['level'])
            self.finish = True
        if self.name.get() in TR.get_all_users():
            if self.doc_issue.get() > 0:
                self.show_train_button()
        Tk.update(self)
        self.fill_form()


