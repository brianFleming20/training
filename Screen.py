'''
Created on 9 March 2022


@Author by Brian F



'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import DisplayScreens
import Training
import Documents
import interface
import LoginWindow as UL
import AdminUser
import Email
import AccessDataBase

DSP = DisplayScreens
TR = Training.Training()
DOC = Documents
INT = interface.interface()
EM = Email.send_emails()
AU = AdminUser
ADD = AccessDataBase.GetExternalData()


logged_user = []

class main_screen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.document_name = None
        self.items = None
        self.canvas_lists = None
        self.canvas_search = None
        self.canvas_button = None
        self.control = controller
        self.base = Canvas(self,bg="#FBF8F1",width=980, height=680)
        self.base.place(x=10, y=10)
        self.serach_item = StringVar()
        self.search_doc = StringVar()
        self.time = StringVar()
        self.admin = None
        self.show = None
        self.form_data = []
        self.search_item = StringVar()
        self.search_document = StringVar()
        self.search_name = ""
        self.finish = False

    def refresh_window(self):
        self.index = -1
        self.time.set(TR.get_date_now())
        logged_in_user = TR.get_logged_in_user()
        Canvas(self,bg="#E9DAC1",width=970, height=680).place(x=10, y=10)
        self.canvas_button = Canvas(self,bg="#F7ECDE",width=120,height=630)
        self.canvas_button.place(x=840,y=10)
        self.canvas_search = Canvas(self,bg="#F7ECDE", width=810,height=50)
        self.canvas_search.place(x=10,y=10)
        self.canvas_lists = Canvas(self, bg="#F7ECDE", width=810,height=560)
        self.canvas_lists.place(x=10,y=80)
        self.canvas_top = Canvas(self, bg="#C2DED1", width=810, height=240)
        self.canvas_top.place(x=10, y=80)
        Button(self.canvas_button,text="Selected user", width=12, command=self.display_user,bg='#54BAB9').place(x=20,y=80)
        self.admin = Button(self.canvas_button,text="Admin", width=12, command=self.admin_user,bg='#54BAB9')
        self.admin.place(x=20,y=160)

        Button(self.canvas_button,text="Events", width=12, command=self.display_events,bg='#54BAB9').place(x=20,y=240)

        Button(self.canvas_button,text="Log Out", width=12, command=self.log_out,bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_search, text="Logged in -", bg="#F7ECDE").place(x=10,y=15)
        Label(self.canvas_top, text="Search", font=("Courier", 16), bg="#C2DED1").place(x=350, y=15)
        Label(self.canvas_top, text="Name", bg="#C2DED1").place(x=30, y=80)

        names = TR.get_all_users()
        self.search_item.set("Choose")
        search_name = OptionMenu(self.canvas_top, self.search_item, *names)
        search_name.place(x=80, y=80)

        Label(self.canvas_top, text="Document Number", bg="#C2DED1").place(x=270, y=80)
        Label(self.canvas_top, text="Document Name", bg="#C2DED1").place(x=270, y=120)
        self.document_name = Label(self.canvas_top, textvariable=self.search_document, bg="#C2DED1")
        self.document_name.place(x=390, y=120)
        search_doc = Entry(self.canvas_top, textvariable=self.search_doc, width=25)
        search_doc.place(x=390, y=80)
        btn = Button(self.canvas_top, text="Search", command=self.search_data, width=8, bg='#54BAB9')
        btn.place(x=630, y=180)
        self.search_document.set("----------------")
        Label(self.canvas_top,text="Needs training soon", bg="#A0D995").place(x=10, y=160)
        Label(self.canvas_top,text="Overdue training     ", bg="#F24C4C").place(x=10, y=183)
        admin = TR.get_user_admin()
        if admin:
            self.admin.config(state=NORMAL)
        else:
            self.admin.config(state=DISABLED)
        Label(self.canvas_search, text=logged_in_user, bg="#F7ECDE").place(x=80,y=15)
        Label(self.canvas_search, text="Date", bg="#F7ECDE").place(x=640, y=18)
        Label(self.canvas_search,textvariable=self.time, bg="#F7ECDE").place(x=700,y=18)
        Label(self.canvas_top, text="  Document No.       Document Name                Issue               Users           Date Trained       Level       Expire Date        Trainer                   Notes                            ").place(x=3,y=220)
        self.show_list_data()
        self.fill_form()

    def admin_user(self):
        self.control.show_frame(AU.ShowUsers)

    def search_data(self):
        self.show_list_data()
        if self.finish:
            for name,item in TR.get_all_training().items():
                for doc,data in item.items():
                    if self.search_doc.get() == doc[:9]:
                        self.fill_docs_list(doc)
        else:
            if self.search_item.get() == "Choose":
                mb.showerror(title="Search Error", message="Please select a name.")
            else:
                for name,item in TR.get_all_training().items():
                    try:
                        trainer = TR.get_user(name)['trainer']
                    except :
                        trainer = "-"
                    if self.search_item.get() == name:
                        self.fill_users_lists(name)
                    if self.search_item.get() == trainer:
                        self.fill_users_lists(name)

    def fill_form(self):
        if not self.finish:
            self.control.after(1000, func=self.check_data)

    def check_data(self):
        doc = TR.get_a_document(self.search_doc.get())
        if not doc:
            pass
        else:
            self.search_document.set(doc['name'])
            self.finish = True
        Tk.update(self)
        self.fill_form()

    def selection_changed(self, event):
        selection = self.items.get()
        mb.showinfo(
                title="New Selection",
                message=f"Selected option: {selection}"
    )


    def display_user(self):
        if self.index == -1:
            mb.showerror(title="Selection Error",message="Please select a row.")
        else:
            self.control.show_frame(DSP.show_user_window)


    def display_events(self):
        self.control.show_frame(DSP.show_event_window)



    def log_out(self):
        shut = mb.askyesno("Log Out","Do you wish to proceed?")
        #################################
        # Clear screen and distroy app  #
        #################################
        if shut:
            self.control.show_frame(UL.LoginWindow)

        

    def onselect(self,event):
        w = event.widget
        self.form_data.clear()
        if self.index == -1:
            idx = int(self.doc_no.curselection()[0])
            self.index = idx
            num = self.doc_no.get(idx)
            self.form_data.insert(0,num)
            name = self.doc_name.get(idx)
            self.form_data.insert(1,name)
            self.doc_name.selection_set(idx)
            issue = self.doc_issue.get(idx)
            self.form_data.insert(2,issue)
            self.doc_issue.selection_set(idx)
            user = self.doc_users.get(idx)
            self.form_data.insert(3,user)
            self.doc_users.selection_set(idx)
            date_train = self.doc_train.get(idx)
            self.form_data.insert(4,date_train)
            self.doc_train.selection_set(idx)
            level = self.doc_level.get(idx)
            self.form_data.insert(5,level)
            self.doc_level.selection_set(idx)
            expire = self.doc_expire.get(idx)
            self.form_data.insert(6,expire)
            self.doc_expire.selection_set(idx)
            trainer = self.doc_trainer.get(idx)
            self.form_data.insert(7,trainer)
            self.doc_trainer.selection_set(idx)
            note = self.doc_note.get(idx)
            self.form_data.insert(8,note)
            self.doc_note.selection_set(idx)
            INT.provide_interface(self.form_data)

        else:
            self.index = -1
            self.show_list_data()
      
    def show_list_data(self):
        self.doc_no = Listbox(self.canvas_lists ,exportselection=False)
        self.doc_no.place(x=5, y=250)
        self.doc_no.config(height=19, width=15, bg="#E9DAC1")


        self.doc_name = Listbox(self.canvas_lists,exportselection=False)
        self.doc_name.place(x=100, y=250)
        self.doc_name.config(height=19, width=20, bg="#E9DAC1")

        self.doc_issue = Listbox(self.canvas_lists,exportselection=False)
        self.doc_issue.place(x=225, y=250)
        self.doc_issue.config(height=19, width=10, bg="#E9DAC1")

        self.doc_users = Listbox(self.canvas_lists,exportselection=False)
        self.doc_users.place(x=290, y=250)
        self.doc_users.config(height=19, width=15, bg="#E9DAC1")

        self.doc_train = Listbox(self.canvas_lists,exportselection=False)
        self.doc_train.place(x=385, y=250)
        self.doc_train.config(height=19, width=12, bg="#E9DAC1")

        self.doc_level = Listbox(self.canvas_lists,exportselection=False)
        self.doc_level.place(x=462, y=250)
        self.doc_level.config(height=19, width=8, bg="#E9DAC1")

        self.doc_expire = Listbox(self.canvas_lists,exportselection=False)
        self.doc_expire.place(x=515, y=250)
        self.doc_expire.config(height=19, width=10, bg="#E9DAC1")

        self.doc_trainer = Listbox(self.canvas_lists,exportselection=False)
        self.doc_trainer.place(x=580, y=250)
        self.doc_trainer.config(height=19, width=12, bg="#E9DAC1")

        self.doc_note = Listbox(self.canvas_lists,exportselection=False)
        self.doc_note.place(x=658, y=250)
        self.doc_note.config(height=19, width=20, bg="#E9DAC1")


        self.doc_no.bind('<<ListboxSelect>>', self.onselect)
        self.doc_users.bind('<<ListboxSelect>>', self.onselect)
        self.doc_name.bind('<<ListboxSelect>>', self.onselect)
        self.doc_no.bind("<MouseWheel>", self.OnMouseWheel)
     

    def fill_users_lists(self,name):
        index = 0
        training_events = TR.get_all_training()
        for user,event in training_events.items():
            if user == name:
                for ref,items in event.items():
                    self.doc_no.insert(END, ref)
                    self.doc_train.insert(END, items['trained_on'])
                    self.doc_expire.insert(END, items['review_date'])
                    self.doc_note.insert(END, items['note'])
                    self.doc_name.insert(END, items['name'])
                    user_item = TR.get_a_document(ref[:9])
                    self.doc_issue.insert(END, user_item['issue'])
                    user_data = TR.get_user(user)
                    self.doc_users.insert(END, user)
                    self.doc_level.insert(END, items['level'])
                    self.doc_trainer.insert(END, user_data['trainer'])
                    if TR.get_email_date(items['review_date']):
                        self.doc_no.itemconfig(index,{"bg":"#A0D995"})
                    if TR.get_overdue_train(items['review_date']):
                        self.doc_no.itemconfig(index,{"bg":"#F24C4C"})
                    index += 1


    def fill_docs_list(self, doc):
        index = 0
        training_events = TR.get_all_training()
        for user, event in training_events.items():
            for ref, items in event.items():
                if ref[:9] == doc:
                    self.doc_no.insert(END, ref)
                    self.doc_train.insert(END, items['trained_on'])
                    self.doc_expire.insert(END, items['review_date'])
                    self.doc_note.insert(END, items['note'])
                    self.doc_name.insert(END, items['name'])
                    item = TR.get_a_document(ref[:9])
                    self.doc_issue.insert(END, item['issue'])
                    user_data = TR.get_user(user)
                    self.doc_users.insert(END, user)
                    self.doc_level.insert(END, items['level'])
                    self.doc_trainer.insert(END, user_data['trainer'])
                    due = items['review_date']
                    # if TR.get_email_date(due):
                    #
                    #     EM.notify_training(user, ref)
                    #     EM.send_copy_to_trainer(user, ref)
                    if TR.get_email_date(items['review_date']):
                        self.doc_no.itemconfig(index,{"bg":"#A0D995"})
                    if TR.get_overdue_train(items['review_date']):
                        self.doc_no.itemconfig(index,{"bg":"#F24C4C"})
                    index += 1


    def OnMouseWheel(self, event):
        self.doc_no.yview("scroll", event.delta, "units")
        self.doc_issue.yview("scroll", event.delta, "units")
        self.doc_name.yview("scroll", event.delta, "units")
        self.doc_users.yview("scroll", event.delta, "units")
        self.doc_train.yview("scroll", event.delta, "units")
        self.doc_trainer.yview("scroll", event.delta, "units")
        self.doc_level.yview("scroll", event.delta, "units")
        self.doc_expire.yview("scroll", event.delta, "units")
        self.doc_note.yview("scroll", event.delta, "units")
        return "break"

class LoggedInUser():
    def set_logged_in_user(user):
        logged_user.clear()
        logged_user.insert(0,user)

    def get_logged_in_user(self):
        return logged_user[0]
    