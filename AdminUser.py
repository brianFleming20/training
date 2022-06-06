'''
Creates a new user for the training records system
'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import Training
import interface
import Screen as SC
import User
import Documents
import AccessDataBase
import onetimepad

TR = Training.Training()
INT = interface.interface()
UR = User
DOC = Documents
AS = AccessDataBase.GetExternalData()
ENTRY = "ByH1KHdo7y30I6aN"

class AddNewUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
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
        self.time.set(TR.get_date_now())
        self.data.clear()
        self.canvas_back.delete('all')
        self.logged_in = TR.get_user(TR.get_logged_in_user())

        Button(self.canvas_btndis, text="Show Users", command=self.show_users, width=12, bg='#54BAB9').place(x=20,
                                                                                                             y=160)
        Button(self.canvas_btndis, text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="New User").place(x=10, y=15)
        Label(self.canvas_srdis, text="Search").place(x=250, y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item, width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_back, text="Name ", bg="#E9DAC1").place(x=50, y=100)
        Label(self.canvas_back, text="New Password ", bg="#E9DAC1").place(x=50, y=140)
        Label(self.canvas_back, text="Confirm Password ", bg="#E9DAC1").place(x=50, y=180)
        Label(self.canvas_back, text="Competency level ", bg="#E9DAC1").place(x=50, y=220)
        Label(self.canvas_back, text="Email address", bg="#E9DAC1").place(x=50, y=260)

        name = Entry(self.canvas_back, textvariable=self.name, width=25)
        name.place(x=210, y=100)
        password = Entry(self.canvas_back, textvariable=self.passw, width=25)
        password.place(x=210, y=140)
        conf_password = Entry(self.canvas_back, textvariable=self.conf_pass, width=25)
        conf_password.place(x=210, y=180)
        competency = Entry(self.canvas_back, textvariable=self.comp, width=15)
        competency.place(x=210, y=220)
        email = Entry(self.canvas_back, textvariable=self.email, width=30)
        email.place(x=210, y=260)

        self.checkbutton = Checkbutton(self.canvas_back, text="   Trainer    ",
                                       variable=self.admin_state, command=self.update_overwrite, font=("Courier", 10))
        self.admin_state.get()
        self.checkbutton.place(x=80, y=520)
        btn5 = Button(self.canvas_back, text="Add User", command=self.add_user, width=12, bg='#54BAB9')
        btn5.place(x=680, y=500)

        if self.logged_in['is_trainer'] == True:
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

    def update_admin(self):
        if not self.administrator:
            self.administrator = 1
        else:
            self.administrator = 0

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def show_users(self):
        self.control.show_frame(ShowUsers)

    # def add_document(self):
    #     filename = filedialog.askopenfilename(initialdir="./Downloads", 
    #     title="Select Document",filetypes = (("pdf files","*.pdf"),("word files","*.docx"))) 
    #     print(filename)
    #     self.document.set(filename)

    def add_user(self):
        password = self.passw.get()
        create_password = onetimepad.encrypt(password, ENTRY)
        if self.name.get() == "" or self.passw.get() == "" or self.comp.get() == 0 or self.email.get() == "":
            mb.showerror(title="Entry Error", message="Some of the fields are empty, \ntry again.")
        else:
            if self.create_user(self.name.get(), self.passw.get(),self.conf_pass.get(), self.comp.get(),
                                self.email.get(),self.administrator,create_password):
                self.control.show_frame(ShowUsers)
            else:
                mb.showerror(title="User Error", message="User not created.")
                return False

    def create_user(self, name, password, conf_pass, comp, email,admin,create_password):
        if password == conf_pass:
            user = UR.User(name=name, level=comp, trainer=self.admin, email=email)
            TR.save_user(user)
            TR.save_user_login(user,create_password,admin)
            return True
        else:
            mb.showerror(title="User Error", message="Your passwords don't match.")
            return False


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
        Button(self.canvas_btndis, text="New User", command=self.add_new_user, width=12, bg='#54BAB9').place(x=20, y=80)
        Button(self.canvas_btndis, text="Edit User", command=self.edit_user, width=12, bg='#54BAB9').place(x=20, y=160)
        Button(self.canvas_btndis, text="Remove User", command=self.delete_user, width=12, bg='#54BAB9').place(x=20,
                                                                                                               y=240)
        Button(self.canvas_btndis, text="Add Document", command=self.add_document, width=12, bg='#54BAB9').place(x=20,
                                                                                                                 y=320)
        Button(self.canvas_btndis, text="Edit Document", command=self.edit_doc, width=12, bg='#54BAB9').place(x=20,
                                                                                                              y=400)
        Button(self.canvas_btndis, text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="New User").place(x=10, y=15)
        Label(self.canvas_srdis, text="Search").place(x=250, y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item, width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_lists, text="Trained Users").place(x=20, y=18)
        Label(self.canvas_lists, text="Documents").place(x=280, y=18)
        self.users = Listbox(self.canvas_lists, exportselection=False)
        self.users.place(x=20, y=45)
        self.users.config(height=20, width=20, bg="#E9DAC1")
        self.documents = Listbox(self.canvas_lists, exportselection=False)
        self.documents.place(x=250, y=45)
        self.documents.config(height=20, width=45, bg="#E9DAC1")

        for no in TR.get_all_users():
            self.users.insert(END, no)

        for ref, doc in TR.get_documents().items():
            self.documents.insert(END, f"{ref} - {doc['name']} - {doc['issue']}")
            self.documents.bind('<<ListboxSelect>>', self.edit_doc)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def add_new_user(self):
        self.control.show_frame(AddNewUser)

    def add_document(self):
        self.control.show_frame(addNewDocument)

    def edit_doc(self, event):
        # show doc details for edit
        idx = int(self.documents.curselection()[0])
        num = self.documents.get(idx)
        INT.provide_interface([num])
        self.control.show_frame(editDocument)

    def edit_user(self):
        try:
            self.index = int(self.users.curselection()[0])
        except IndexError:
            mb.showerror(title="Selection Error", message="Please select a row.")
            self.refresh_window()
        else:
            data_user = self.users.get(self.index)

            INT.provide_interface([data_user])
            self.control.show_frame(EditUser)

    def delete_user(self):
        self.index = int(self.users.curselection()[0])
        user = self.users.get(self.index)
        AS.user_left(user)
        result = TR.delete_user(user)
        if result:
            self.control.show_frame(ShowUsers)
        else:
            mb.showerror(title="Selection Error", message="Please select a row.")

class EditUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
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
        Button(self.canvas_btndis, text="Add User", command=self.add_user, width=12, bg='#54BAB9').place(x=20, y=160)
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
        Label(self.canvas_back, text="Change trainer", bg="#E9DAC1").place(x=50, y=300)
        self.name.set(self.data[0])
        Label(self.canvas_back, text=self.name.get(), width=14, font='Helvetica 12 bold').place(x=210, y=100)
        password = Entry(self.canvas_back, textvariable=self.passw, width=25)
        password.place(x=210, y=140)
        conf = Entry(self.canvas_back, textvariable=self.conf_pass, width=25)
        conf.place(x=210, y=180)
        comp = Entry(self.canvas_back, textvariable=self.comp, width=15)
        comp.place(x=210, y=220)
        email = Entry(self.canvas_back, textvariable=self.email, width=20)
        email.place(x=210, y=260)
        trainer = Entry(self.canvas_back, textvariable=self.trainer, width=20)
        trainer.place(x=210, y=300)
        self.checkbutton = Checkbutton(self.canvas_back, text="   Trainer    ",
                                       variable=self.admin_state, command=self.update_trainer, font=("Courier", 10))
        self.admin_state.get()
        self.checkbutton.place(x=80, y=520)
        user = TR.get_user(self.name.get())
        self.admin_state.set(user['is_trainer'])

        user_password = TR.get_user_password(self.name.get())
        if user_password:
            try:
                self.comp.set(user['level'])
                self.trainer.set(user['trainer'])
                self.email.set(user['email'])
            except:
               pass
        else:
            mb.showerror(title="User Error", message="User cannot be displayed fully,\nmissing entries,"
                                                     "\nPlease complete..")
        # btn2 = Button(self.canvas_back, text="Update Password", command=self.change_password, width=14)
        # btn2.place(x=400, y=180)
        # btn3 = Button(self.canvas_back, text="Change Level", command=self.change_level, width=14)
        # btn3.place(x=400, y=220)
        # btn4 = Button(self.canvas_back, text="Change Email", command=self.change_email, width=14)
        # btn4.place(x=400, y=260)
        # btn5 = Button(self.canvas_back, text="Change trainer", command=self.change_trainer, width=14)
        # btn5.place(x=400, y=300)
        btn6 = Button(self.canvas_back, text="Update user", command=self.update, width=14)
        btn6.place(x=400, y=520)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def show_users(self):
        self.control.show_frame(ShowUsers)

    def add_user(self):
        self.control.show_frame(AddNewUser)

    def update_trainer(self):
        if not self.admin:
            self.admin = True
        else:
            self.admin = False

    def get_admin(self):
        return self.admin

    def update_user(self):
        password = self.passw.get()
        confirm_pass = self.conf_pass.get()

        if password == confirm_pass:
            create_password = onetimepad.encrypt(password, ENTRY)
            update_user = TR.get_blank_user()
            update_user.name = self.name.get()
            update_user.level = self.comp.get()
            update_user.trainer = self.trainer.get()
            update_user.is_trainer = self.admin
            update_user.password = create_password
            update_user.email = self.email.get()
            TR.update_password(update_user.name,create_password)
            return update_user
        else:
            mb.showerror(title="Password Error", message="Your passwords are not the same, \ntry again.")

    # def change_password(self):
    #     password = self.passw.get()
    #     confirm_pass = self.conf_pass.get()
    #     if password == confirm_pass:
    #         update_user = self.update_user()
    #         TR.save_user(update_user)
    #     else:
    #         mb.showerror(title="Password Error", message="Your passwords are not the same, \ntry again.")

    def update(self):
        update_user = self.update_user()
        TR.save_user(update_user)
        self.control.show_frame(ShowUsers)


    def set_for_test(self,password,level,trainer):
        self.passw.set(password)
        self.conf_pass.set(password)
        self.comp.set(level)
        self.trainer.set(trainer)


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
        Label(self.canvas_back, text="Document Location Address",
              bg="#E9DAC1").place(x=50, y=220)

        self.doc_name = Entry(self.canvas_back, textvariable=self.name, width=30)
        self.doc_name.place(x=210, y=100)
        self.doc_ref = Entry(
            self.canvas_back, textvariable=self.doc_reference, width=30)
        self.doc_ref.place(x=210, y=140)
        self.doc_iss = Entry(
            self.canvas_back, textvariable=self.doc_issue, width=30)
        self.doc_iss.place(x=210, y=180)
        self.doc_location = Entry(
            self.canvas_back, textvariable=self.doc_location, width=40)
        self.doc_location.place(x=210, y=220)

        Button(self.canvas_back, text="Add Document", width=12,
               command=self.add_new_document,
               bg='#54BAB9', ).place(x=680, y=500)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def documents(self):
        self.refresh_window()

    def add_new_document(self):
        if self.name.get() == "" or self.doc_issue.get() == "" or self.doc_reference.get() == "" or self.doc_location.get() == "":
            mb.showerror(title="Entry Error", message="Some of your inputs are empty, \ntry again.")
        else:
            document = DOC.MakeDoc(name=self.name.get(), issue=self.doc_issue.get(),
                               ref=self.doc_reference.get(), location=self.doc_location.get())
            TR.add_document(document)
            self.name.set("")
            self.doc_reference.set("")
            self.doc_issue.set("")
            self.doc_location.set("")
            self.refresh_window()


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
        self.location = StringVar()
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
        Button(self.canvas_btndis, text="Show Documents", command=self.show_documents, width=12, bg='#54BAB9').place(
            x=20, y=80)
        Button(self.canvas_btndis, text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="Edit Document").place(x=10, y=15)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_back, text="Document Name ", bg="#E9DAC1").place(x=50, y=100)
        Label(self.canvas_back, text="Document reference ", bg="#E9DAC1").place(x=50, y=140)
        Label(self.canvas_back, text="Issue number ", bg="#E9DAC1").place(x=50, y=180)
        Label(self.canvas_back, text="Document Location", bg="#E9DAC1").place(x=50, y=220)

        Entry(self.canvas_back, textvariable=self.name, width=25).place(x=210, y=100)
        Entry(self.canvas_back, textvariable=self.ref, width=25).place(x=210, y=140)
        Entry(self.canvas_back, textvariable=self.issue, width=25).place(x=210, y=180)
        Entry(self.canvas_back, textvariable=self.location, width=35).place(x=210, y=220)

        self.name.set(ref["name"])
        self.ref.set(ref_num)
        self.issue.set(ref["issue"])
        self.location.set(ref["location"])

        Button(self.canvas_back, text="Save Changes", command=self.save, width=12, bg='#54BAB9').place(x=550, y=450)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def show_documents(self):
        self.control.show_frame(ShowUsers)

    def save(self):
        doc = DOC.MakeDoc(name=self.name.get(), ref=self.ref.get(), issue=self.issue.get(), location=self.location.get())
        TR.update_document(doc)
        self.control.show_frame(ShowUsers)
