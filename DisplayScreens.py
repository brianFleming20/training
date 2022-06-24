'''
Created on 9 March 2022


@Author by Brian F



'''

import tkinter as tk
import webbrowser
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
        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=120, height=630)
        self.canvas_btndis.place(x=840, y=10)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=810, height=50)
        self.canvas_srdis.place(x=10, y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810, height=560)
        self.canvas_back.place(x=10, y=80)
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

        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_back, text="Name", bg="#E9DAC1").place(x=50, y=90)

        Label(self.canvas_back, text="Trained By ",
              bg="#E9DAC1").place(x=50, y=170)
        Label(self.canvas_back, text="Trained On Date",
              bg="#E9DAC1").place(x=50, y=200)
        Label(self.canvas_back, text="Training Exrires",
              bg="#E9DAC1").place(x=50, y=240)
        Label(self.canvas_back, text="Competence Level",
              bg="#E9DAC1").place(x=50, y=280)
        Label(self.canvas_back, text="Email address",
              bg="#E9DAC1").place(x=50, y=320)
        Label(self.canvas_back, text="Notes", bg="#E9DAC1").place(x=50, y=370)

        self.usr = self.canvas_back.create_text(
            400, 90, text=" ", font=('Helvetica 12 bold'))
        self.train = self.canvas_back.create_text(
            400, 170, text=" ", font=('Helvetica 12 bold'))
        self.train_date = self.canvas_back.create_text(
            400, 210, text=" ", font=('Helvetica 12 bold'))
        self.exp = self.canvas_back.create_text(
            400, 250, text=" ", font=('Helvetica 12 bold'))
        self.comp = self.canvas_back.create_text(
            400, 290, text=" ", font=('Helvetica 12 bold'))
        self.email = self.canvas_back.create_text(
            330, 330, text=" ", font=('Helvetica 12 bold'))

        self.text_area = tk.Text(self, height=8, width=50)
        self.text_area.place(x=50, y=480)
        Label(self.canvas_back, text="Trained on ").place(x=500, y=50)
        self.doc_name = Listbox(self, height=20, width=20)
        self.doc_name.place(x=480, y=180)
        self.doc_ref = Listbox(self, height=20, width=16)
        self.doc_ref.place(x=615, y=180)
        self.doc_issue = Listbox(self, height=20, width=10)
        self.doc_issue.place(x=730, y=180)
        self.transfer_info()

    def transfer_info(self):
        training = TR.get_all_training()
        self.doc_name.insert(END, "Document Name")
        self.doc_name.insert(END, "-----------------")
        self.doc_ref.insert(END, "Document Ref.")
        self.doc_ref.insert(END, "-----------------")
        self.doc_issue.insert(END, "Issue")
        self.doc_issue.insert(END, "----------------")
        self.canvas_back.itemconfigure(self.usr, text=self.data[3])
        self.canvas_back.itemconfigure(self.comp, text=self.data[5])
        self.canvas_back.itemconfigure(self.train, text=self.data[7])
        for user, data in training.items():
            for ref, values in data.items():
                if user == self.data[3]:
                    user_info = TR.get_user(user)
                    self.doc_ref.insert(END, ref)
                    doc_data = TR.get_a_document(ref)
                    try:
                        self.canvas_back.itemconfigure(self.train_date, text=values['trained_on'])
                        self.canvas_back.itemconfigure(self.exp, text=values['review_date'])
                        self.text_area.insert('1.0', self.data[8])
                        self.doc_name.insert(END, values['name'])
                        self.doc_issue.insert(END, doc_data['issue'])
                        self.canvas_back.itemconfigure(self.email, text=user_info['email'])
                    except:
                        pass
                        # mb.showerror(title="User Error", message="User cannot be displayed fully,\nmissing entries..")

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


class show_document_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.index = -1
        self.doc_selected = None
        self.control = controller
        self.canvas_btndis = Canvas(self, bg="#E9DAC1", width=120, height=630)
        self.canvas_btndis.place(x=840, y=10)
        self.canvas_srdis = Canvas(self, bg="#E9DAC1", width=810, height=50)
        self.canvas_srdis.place(x=10, y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810, height=560)
        self.canvas_back.place(x=10, y=80)
        self.search_item = StringVar()
        self.user = StringVar()
        self.time = StringVar()
        self.user_trained_on_doc = ""
        self.form_data = []
        self.data = []
        self.doc_location = ""


    def refresh_window(self):
        self.time.set(TR.get_date_now())
        self.data.clear()
        self.data = TR.get_documents()
        self.index = -1
        self.canvas_back.delete('all')

        self.user.set(TR.get_logged_in_user())

        Button(self.canvas_btndis, text="Main", width=12,
               command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="Train on a document").place(x=10, y=15)
        Label(self.canvas_srdis, text="Search").place(x=250, y=15)
        search = Entry(self.canvas_srdis, textvariable=self.search_item, width=25)
        search.place(x=300, y=15)
        btn = Button(self.canvas_srdis,text="Search", command=self.search_data,width=10, bg='#54BAB9')
        btn.place(x=400,y=15)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_back, textvariable=self.user).place(x=180, y=40)
        Label(self.canvas_back, text="Training required ").place(x=180, y=70)
        self.doc_name = Listbox(self.canvas_back, height=20, width=20, exportselection=False)
        self.doc_name.place(x=180, y=150)
        self.doc_ref = Listbox(self.canvas_back, height=20, width=20, exportselection=False)
        self.doc_ref.place(x=315, y=150)
        self.doc_issue = Listbox(self.canvas_back, height=20, width=10, exportselection=False)
        self.doc_issue.place(x=450, y=150)
        self.doc_loc_tab = Listbox(self.canvas_back, height=20, width=20, exportselection=False)
        self.doc_loc_tab.place(x=530, y=150)
        self.doc_name.insert(END, "Document Name")
        self.doc_name.insert(END, "-----------------")
        self.doc_ref.insert(END, "Document Ref.")
        self.doc_ref.insert(END, "-----------------")
        self.doc_issue.insert(END, "Issue")
        self.doc_issue.insert(END, "----------------")


        Button(self.canvas_back, text="Read", command=self.training,
               width=10, bg='#54BAB9').place(x=620, y=480)
        self.doc_name.bind("<MouseWheel>", self.OnMouseWheel)
        self.doc_ref.bind("<MouseWheel>", self.OnMouseWheel)

        for ref, body in self.data.items():
            self.doc_ref.insert(END, ref)
            self.doc_name.insert(END, body['name'])
            self.doc_issue.insert(END, body['issue'])
            self.doc_loc_tab.insert(END, body['location'])

        self.doc_issue.insert(END, "")
        self.doc_name.insert(END, "")
        self.doc_ref.bind('<<ListboxSelect>>', self.onselect)

    def OnMouseWheel(self, event):
        self.doc_ref.yview("scroll", event.delta, "units")
        self.doc_issue.yview("scroll", event.delta, "units")
        self.doc_name.yview("scroll", event.delta, "units")
        # this prevents default bindings from firing, which
        # would end up scrolling the widget twice
        return "break"

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def training(self):
        logged_in_user = TR.get_logged_in_user()
        if self.index == -1:
            mb.showerror(title="Document selection error", message="Please select a document")
        else:
            doc = TR.get_a_document(self.doc_selected)
            # path = doc['location']
            path = "https://empower1902.bsientropy.com/DeltexMedical/Document/Permalink/PRC-000649"
            webbrowser.open_new(path)

            # entropy permalink address for each document
            # show that user has trained on a document from document reference no
            # TR.register_trained(self.doc_selected, logged_in_user)
            self.refresh_window()

    def search_data(self):
        print(self.search_item)

    def onselect(self, event):
        w = event.widget
        self.form_data.clear()
        if self.index == -1:
            idx = int(self.doc_ref.curselection()[0])
            self.index = idx
            name = self.doc_name.get(idx)
            self.form_data.insert(0, name)
            self.doc_name.selection_set(idx)
            num = self.doc_ref.get(idx)
            self.form_data.insert(0, num)
            self.doc_ref.selection_set(idx)
            issue = self.doc_issue.get(idx)
            self.form_data.insert(0, issue)
            self.doc_issue.selection_set(idx)
            location = self.doc_loc_tab.get(idx)
            self.form_data.insert(0, location)
            self.doc_loc_tab.selection_set(idx)
            self.doc_location = location
            self.doc_selected = num
        else:
            self.index = -1
            self.refresh_window()


class show_event_window(tk.Frame):
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

    def refresh_window(self):
        self.time.set(TR.get_date_now())
        Button(self.canvas_btndis, text="New Event", width=12,
               command=self.add_event, bg='#54BAB9').place(x=20, y=80)
        Button(self.canvas_btndis, text="Delete",
               width=12, bg='#54BAB9').place(x=20, y=160)
        Button(self.canvas_btndis, text="Edit",
               width=12, bg='#54BAB9').place(x=20, y=240)
        Button(self.canvas_btndis, text="Main", width=12,
               command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="Events").place(x=10, y=15)

        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)

        Label(self.canvas_back, text="Upcoming training events").place(x=50, y=50)
        self.check_for_email()

    def check_for_email(self):
        # mb.showinfo(title="Email", message="Email function disabled..")
        sent = False
        text_area = tk.Text(self.canvas_back, height=25, width=85)
        text_area.place(x=50, y=100)
        for user, event in TR.get_all_training().items():
            for ref, items in event.items():
                if not items['note'] or type(items['note']) == str and "No longer an employee" in items['note']:
                    pass
                else:
                    if ref != "Login" and TR.get_email_date(items['review_date']):
                        text_area.insert(INSERT,
                                         f"{user} \t\t: {items['name']} : {ref}\t\t: review {items['review_date']}\n")
                        self.generate_email(user,ref)
                        sent = True
        text_area.config(state=DISABLED)
        if sent:
            return True
        else:
            return False

    def generate_email(self, name, ref):
        EM.notify_training(name,ref)
        EM.send_copy_to_trainer(name,ref)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def add_event(self):
        self.control.show_frame(AU.ShowUsers)