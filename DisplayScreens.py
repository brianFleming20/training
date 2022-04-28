'''
Created on 9 March 2022


@Author by Brian F



'''

import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import messagebox as mb
import AdminUser as AU
import Documents as DOC
import interface
import Screen as SC
import Training

TR = Training.Training()
TE = Training
INT = interface.interface()


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
        Label(self.canvas_srdis, text="Search").place(x=250, y=15)
        search = Entry(self.canvas_srdis,
                       textvariable=self.serach_item, width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)
        Label(self.canvas_back, text="Name", bg="#E9DAC1").place(x=50, y=90)

        Label(self.canvas_back, text="Trained By ",
              bg="#E9DAC1").place(x=50, y=170)
        Label(self.canvas_back, text="Trained On Date",
              bg="#E9DAC1").place(x=50, y=210)
        Label(self.canvas_back, text="Training Exrires",
              bg="#E9DAC1").place(x=50, y=250)
        Label(self.canvas_back, text="Competence Level",
              bg="#E9DAC1").place(x=50, y=290)
        Label(self.canvas_back, text="Notes", bg="#E9DAC1").place(x=50, y=340)
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

        self.text_area = tk.Text(self, height=8, width=50)
        self.text_area.place(x=50, y=450)
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
        for user,data in training.items():
            for ref,values in data.items():
                if user == self.data[3]:
                    self.doc_ref.insert(END, ref)
                    self.canvas_back.itemconfigure(self.train_date, text=values['trained_on'])
                    self.canvas_back.itemconfigure(self.exp, text=values['review_date'])
                    self.text_area.insert('1.0', self.data[8])
                    self.doc_name.insert(END, values['name'])
                    doc_data = TR.get_a_document(ref)
                    self.doc_issue.insert(END, doc_data['issue'])

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


class show_document_window(tk.Frame):
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
        self.user_trained_on_doc = ""
        self.form_data = []
        self.data = []
        self.doc_location = ""

    def refresh_window(self):
        # text = Text(self, width=80, height=30)
        self.time.set(TR.get_date_now())
        self.data.clear()
        self.data = TR.get_documents()
        self.index = -1
        self.canvas_back.delete('all')
        Button(self.canvas_btndis, text="New", command=self.add_new_document,
               width=12, bg='#54BAB9').place(x=20, y=80)
        Button(self.canvas_btndis, text="Delete",
               width=12, bg='#54BAB9').place(x=20, y=160)
        Button(self.canvas_btndis, text="Edit",
               width=12, bg='#54BAB9').place(x=20, y=240)
        Button(self.canvas_btndis, text="Main", width=12,
               command=self.return_to_home, bg='#54BAB9').place(x=20, y=500)
        Label(self.canvas_srdis, text="Train on a document").place(x=10, y=15)
        Label(self.canvas_srdis, text="Search").place(x=250, y=15)
        search = Entry(self.canvas_srdis,
                       textvariable=self.serach_item, width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)

        Label(self.canvas_back, text="Trained on ").place(x=200, y=50)
        self.doc_name = Listbox(self.canvas_back, height=20, width=20,exportselection=False)
        self.doc_name.place(x=180, y=150)
        self.doc_ref = Listbox(self.canvas_back, height=20, width=20,exportselection=False)
        self.doc_ref.place(x=315, y=150)
        self.doc_issue = Listbox(self.canvas_back, height=20, width=10,exportselection=False)
        self.doc_issue.place(x=450, y=150)
        self.doc_loc_tab = Listbox(self.canvas_back, height=20, width=20,exportselection=False)
        self.doc_loc_tab.place(x=530,y=150)
        self.doc_name.insert(END, "Document Name")
        self.doc_name.insert(END, "-----------------")
        self.doc_ref.insert(END, "Document Ref.")
        self.doc_ref.insert(END, "-----------------")
        self.doc_issue.insert(END, "Issue")
        self.doc_issue.insert(END, "----------------")
        self.doc_loc_tab.insert(END,"Document Location")
        self.doc_loc_tab.insert(END, "-----------------")

        Button(self.canvas_back, text="Read", command=self.show_pdf,
               width=10, bg='#54BAB9').place(x=620, y=480)

        for ref,body in self.data.items():
            self.doc_ref.insert(END, ref)
            self.doc_name.insert(END, body['name'])
            self.doc_issue.insert(END, body['issue'])
            self.doc_loc_tab.insert(END, body['location'])

        self.doc_issue.insert(END, "")
        self.doc_name.insert(END, "")
        self.doc_name.bind('<<ListboxSelect>>', self.onselect)


    def return_to_home(self):
        self.control.show_frame(SC.main_screen)


    def add_new_document(self):
        self.control.show_frame(addNewDocument)

    def show_pdf(self):
        logged_in_user = INT.extend_interface()[0]
        if self.index == -1:
            mb.showerror(title="Document selection error",message="Please select a document")
        else:
            path = "https://empower1902.bsientropy.com/DeltexMedical/Document/Permalink/PRC-000649"
            webbrowser.open_new(path)
            # entropy permalink address for each document
            # show that user has trained on a document from document reference no
            TR.register_trained(self.doc_selected, logged_in_user)



    def onselect(self,event):
        w = event.widget
        self.form_data.clear()
        if self.index == -1:
            idx = int(self.doc_name.curselection()[0])
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
        Label(self.canvas_srdis, text="Search").place(x=250, y=15)
        search = Entry(self.canvas_srdis,
                       textvariable=self.serach_item, width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis, textvariable=self.time).place(x=700, y=18)



    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def add_event(self):
        self.control.show_frame(AU.ShowUsers)


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
        self.doc_issue = Entry(
            self.canvas_back, textvariable=self.doc_issue, width=30)
        self.doc_issue.place(x=210, y=180)
        self.doc_location = Entry(
            self.canvas_back, textvariable=self.doc_location, width=40)
        self.doc_location.place(x=210, y=220)

        Button(self.canvas_back, text="Add Document", width=12,
               command=self.add_new_document,
               bg='#54BAB9', ).place(x=680, y=500)

    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def documents(self):
        self.control.show_frame(show_document_window)

    def add_new_document(self):
        document = DOC.MakeDoc(name=self.name.get(), issue=self.doc_issue.get(),
                               ref=self.doc_reference.get(), location=self.doc_location.get())
        TR.add_document(document)
        self.name.set("")
        self.doc_reference.set("")
        self.doc_issue.set("")
        self.doc_location.set("")
        self.control.show_frame(show_document_window)
