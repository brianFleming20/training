'''
Created on 9 March 2022


@Author by Brian F



'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import AdminUser as AU
import interface
import Screen as SC
import Training
import Email

TR = Training.Training()
TE = Training
INT = interface.interface()
EM = Email.send_emails()


class show_user_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=self.ws / 8, height=self.hs - (self.hs / 5))
        self.canvas_btndis.place(x=self.ws - (self.ws / 4.5), y=110)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=self.ws - (self.ws / 8.5), height=self.hs / 10)
        self.canvas_srdis.place(x=10, y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=self.ws / 1.3, height=self.hs / 1.25)
        self.canvas_back.place(x=10, y=110)
        self.serach_item = StringVar()
        self.time = StringVar()
        self.doc_id = StringVar()
        self.data = []

    def refresh_window(self):
        self.time.set(TR.get_date_now())
        self.data.clear()
        self.data.extend(INT.extend_interface())
        self.canvas_back.delete('all')
        Button(self.canvas_btndis, text="Main", width=12,
               command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="Selected User").place(x=10, y=15)
        Label(self.canvas_srdis, text="Date ", bg="#E9DAC1").place(x=630, y=18)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_back, text="Name", bg="#E9DAC1").place(x=50, y=150)
        Label(self.canvas_back, text="Email address",
              bg="#E9DAC1").place(x=50, y=220)
        self.usr = self.canvas_back.create_text(
            330, 150, text=" ", font=('Helvetica 12 bold'))
        self.email = self.canvas_back.create_text(
            330, 220, text=" ", font=('Helvetica 12 bold'))
        # self.text_area = tk.Text(self, height=8, width=50)
        # self.text_area.place(x=50, y=480)
        self.doc_name = Listbox(self.canvas_back, height=20, width=100)
        self.doc_name.place(x=480, y=220)
        ref_len = 9
        training = TR.get_all_training()
        Label(self.canvas_back, text="Document Name", bg="#E9DAC1").place(relx=0.43, rely=0.25)
        Label(self.canvas_back, text="Document Ref", bg="#E9DAC1").place(relx=0.65, rely=0.25)
        Label(self.canvas_back, text="Competence Level", bg="#E9DAC1").place(relx=0.75, rely=0.25)
        Label(self.canvas_back, text="Notes", bg="#E9DAC1").place(relx=0.9, rely=0.25)
        self.canvas_back.itemconfigure(self.usr, text=self.data[3])
        for user, data in training.items():
            for ref, values in data.items():
                if user == self.data[3]:
                    user_info = TR.get_user(user)

                    if len(ref) < 10:
                        ref_len = 10 - len(ref)
                    self.doc_name.insert(END, "{:<65s}{:<40s}{}{:<40}{:^}".format(values['name'][:35], ref[:22], ' ' * ref_len, values['level'], self.data[8]))
                    self.canvas_back.itemconfigure(self.email, text=user_info['email'])
        self.doc_name.select_set(0)
        self.doc_name.focus_set()

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


class show_document_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.training = None
        self.index = -1
        self.doc_selected = None
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.canvas_back = Canvas(self, bg="#F7ECDE", width=self.ws / 1.3, height=self.hs - (self.hs / 5))
        self.canvas_back.place(x=10, y=110)
        self.control = controller
        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=self.hs / 8, height=self.hs - (self.hs / 5))
        self.canvas_btndis.place(x=self.ws - (self.ws / 4.5), y=110)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=self.ws - (self.ws / 8.5), height=self.hs / 10)
        self.canvas_srdis.place(x=10, y=15)

        self.search_item = StringVar()
        self.user = StringVar()
        self.time = StringVar()
        self.doc_no = StringVar()
        self.doc_name = StringVar()
        self.doc_issue = StringVar()
        self.user_trained_on_doc = ""
        self.form_data = []
        self.data = []
        self.doc_location = ""

    def refresh_window(self):
        self.time.set(TR.get_date_now())
        self.data.extend(INT.extend_interface())
        self.doc_no.set(self.data[0])
        self.doc_name.set(self.data[1])
        self.doc_issue.set(self.data[2])
        self.training = TR.get_all_training()
        self.index = -1
        self.canvas_back.delete('all')

        self.user.set(TR.get_logged_in_user())

        Button(self.canvas_btndis, text="Main", width=12,
               command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_back, text="Document Details", bg="#F7ECDE", font=("Courier", 18)).place(relx=0.3, rely=0.05)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=40)
        Label(self.canvas_srdis, text="Logged In User", bg="#E9DAC1").place(x=60, y=40)
        Label(self.canvas_srdis, textvariable=self.user).place(x=180, y=40)

        Label(self.canvas_back, text="Document Reference Number", bg="#F7ECDE").place(relx=0.1, rely=0.1)
        Label(self.canvas_back, text="Document Name", bg="#F7ECDE").place(relx=0.3, rely=0.1)
        Label(self.canvas_back, text="Document Issue Number", bg="#F7ECDE").place(relx=0.5, rely=0.1)
        Label(self.canvas_back, textvariable=self.doc_no).place(relx=0.14, rely=0.12)
        Label(self.canvas_back, textvariable=self.doc_name).place(relx=0.3, rely=0.12)
        Label(self.canvas_back, textvariable=self.doc_issue).place(relx=0.52, rely=0.12)
        Label(self.canvas_back, text="Associated Users", bg="#F7ECDE").place(relx=0.25, rely=0.2)
        self.name = Listbox(self.canvas_back, height=20, width=25)
        self.name.place(relx=0.2, rely=0.25)

        self.name.insert(END, "  User")
        self.name.insert(END, "----------------------")

        for ref, body in self.training.items():
            for key, data in body.items():
                if key == self.data[0]:
                    self.name.insert(END, ref)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


#########################################################################
#                                                                       #
#########################################################################

class show_event_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=self.ws / 1.3, height=self.hs - (self.hs / 5))
        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=self.hs / 6, height=self.hs - (self.hs / 5))
        self.canvas_btndis.place(x=self.ws - (self.ws / 4.5), y=110)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=self.ws - (self.ws / 8.5), height=self.hs / 10)
        self.canvas_srdis.place(x=10, y=15)
        self.canvas_back.place(x=10, y=110)
        self.serach_item = StringVar()
        self.time = StringVar()

    def refresh_window(self):
        self.time.set(TR.get_date_now())
        Button(self.canvas_btndis, text="Show Users", width=12,
               command=self.add_event, bg='#54BAB9').place(x=20, y=80)

        Button(self.canvas_btndis, text="Main", width=12,
               command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="Events").place(x=10, y=15)

        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)

        Label(self.canvas_back, text="Upcoming training events").place(x=50, y=50)
        admin = TR.get_user_admin()
        if admin:
            Button(self.canvas_back, text="Send Emails", width=30, bg='#54BAB9', command=self.generate_email).place(
                x=580, y=530)
        self.check_for_email()

    def check_for_email(self):
        text_area = tk.Text(self.canvas_back, height=25, width=85)
        text_area.place(x=50, y=100)
        complete = False
        dash = '-' * 80
        name = " Name"
        doc = "Document Name"
        review = "Review Date"
        text_area.insert(INSERT, f"{dash}\n")
        text_area.insert(INSERT, "{:<10s}{:>35s}{:>33s}\n".format(name, doc, review))
        text_area.insert(INSERT, f"{dash}\n")
        for user, event in TR.get_all_training().items():
            for ref, items in event.items():
                email_date = TR.get_email_date(items['review_date'])
                if not items['note'] or type(items['note']) == str and "longer" in items['note'] or "company" in items['note']:
                    pass
                else:
                    if ref != "Login" and email_date:
                        text_area.insert(INSERT,
                                         f"{user :<18s}{items['name']:^55s}{items['review_date']:^8}\n")
                        complete = True

        text_area.config(state=DISABLED)
        return complete

    def generate_email(self):
        for user, event in TR.get_all_training().items():
            for ref, items in event.items():
                if not items['note'] or type(items['note']) == str and "No longer an employee" in items['note']:
                    pass
                else:
                    if ref != "Login" and TR.get_email_date(items['review_date']):
                        EM.notify_training(user, ref)
                        EM.send_copy_to_trainer(user, ref)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def add_event(self):
        self.control.show_frame(AU.ShowUsers)
