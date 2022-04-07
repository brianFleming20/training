'''
Created on 9 March 2022


@Author by Brian F



'''

from asyncio.windows_events import NULL
from msilib.schema import ComboBox
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from time import gmtime, strftime
from tkinter.ttk import Combobox
import DisplayScreens
import Training
import Documents
import interface
import LoginWindow as UL
import DataStore
import NewUser


DSP = DisplayScreens
TR = Training.Training()
DOC = Documents.Document()
INT = interface.interface()
DS = DataStore.data_store()
NU = NewUser



class main_screen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.items = None
        self.canvas_lists = None
        self.canvas_search = None
        self.canvas_button = None
        self.control = controller
        self.base = Canvas(self,bg="#FBF8F1",width=980, height=680)
        self.base.place(x=10, y=10)
        self.serach_item = StringVar()
        self.time = StringVar()
        self.admin = None
        self.index = -1
        self.form_data = []
    



    def refresh_window(self):
        self.time.set(TR.get_now_time())
        logged_in_user = INT.extend_interface()[0]

        admins = TR.get_all_trainers()
     
        Canvas(self,bg="#E9DAC1",width=970, height=680).place(x=10, y=10)
        self.canvas_button = Canvas(self,bg="#F7ECDE",width=120,height=630)
        self.canvas_button.place(x=840,y=10)
        self.canvas_search = Canvas(self,bg="#F7ECDE", width=810,height=50)
        self.canvas_search.place(x=10,y=10)
        self.canvas_lists = Canvas(self, bg="#F7ECDE", width=810,height=560)
        self.canvas_lists.place(x=10,y=80)
        Button(self.canvas_button,text="Users", width=12, command=self.display_user,bg='#54BAB9').place(x=20,y=80)
        self.admin = Button(self.canvas_button,text="Admin", width=12, command=self.admin_user,bg='#54BAB9')
        self.admin.place(x=20,y=160)
        Button(self.canvas_button,text="Documents", width=12, command=self.display_documents,bg='#54BAB9').place(x=20,y=240)
        Button(self.canvas_button,text="Events", width=12, command=self.display_events,bg='#54BAB9').place(x=20,y=320)
        Button(self.canvas_button,text="Update", width=12, command=self.display_events,bg='#54BAB9').place(x=20,y=400)
        Button(self.canvas_button,text="Log Out", width=12, command=self.log_out,bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_search, text="Training Documents").place(x=10,y=15)
        Label(self.canvas_search, text="Search").place(x=250,y=15)
        if logged_in_user in admins:
            self.admin.config(state=NORMAL)
        else:
            self.admin.config(state=DISABLED)
        search = Entry(self.canvas_search, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        self.items = Combobox(self.canvas_search,state="readonly",values=["Select","Person","Document","Training"])
        self.items.bind("<<ComboboxSelected>>", self.selection_changed)
        self.items.place(x=530, y=20)
        self.items.current(0)
        Label(self.canvas_search,textvariable=self.time).place(x=700,y=18)
        Label(self.canvas_lists, text="  Document No.       Document Name                Issue               Users           Date Trained       Level       Expire Date        Trainer                   Notes").place(x=5,y=5)
      
        # while self.index == -1:
        self.show_list_data()
       
        

    def admin_user(self):
        
        self.control.show_frame(NU.ShowUsers) 


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



    def display_add_user(self):
        self.control.show_frame(DSP.show_add_user_window)



    def display_documents(self):
        self.control.show_frame(DSP.show_document_window)


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
            INT._interface(self.form_data)
            
        else:
            self.index = -1
            self.show_list_data()
        
      
    def show_list_data(self):

        self.doc_no = Listbox(self.canvas_lists,exportselection=False)
        self.doc_no.place(x=5, y=25)
        self.doc_no.config(height=32, width=15, bg="#E9DAC1")
        

        for no in range(1000,7000,300):
            self.doc_no.insert(END, no)

        self.doc_name = Listbox(self.canvas_lists,exportselection=False)
        self.doc_name.place(x=100, y=25)
        self.doc_name.config(height=32, width=20, bg="#E9DAC1")
       

        for no in range(1,25,1):
            self.doc_name.insert(END, no)

        self.doc_issue = Listbox(self.canvas_lists,exportselection=False)
        self.doc_issue.place(x=225, y=25)
        self.doc_issue.config(height=32, width=10, bg="#E9DAC1")

        for no in range(1,25,1):
            self.doc_issue.insert(END, no)
       

        self.doc_users = Listbox(self.canvas_lists,exportselection=False)
        self.doc_users.place(x=290, y=25)
        self.doc_users.config(height=32, width=15, bg="#E9DAC1")
        


        self.doc_train = Listbox(self.canvas_lists,exportselection=False)
        self.doc_train.place(x=385, y=25)
        self.doc_train.config(height=32, width=12, bg="#E9DAC1")

        for no in range(1,25,2):
            self.doc_train.insert(END, no)
     

        self.doc_level = Listbox(self.canvas_lists,exportselection=False)
        self.doc_level.place(x=462, y=25)
        self.doc_level.config(height=32, width=8, bg="#E9DAC1")
    

        self.doc_expire = Listbox(self.canvas_lists,exportselection=False)
        self.doc_expire.place(x=515, y=25)
        self.doc_expire.config(height=32, width=10, bg="#E9DAC1")
        

        for no in range(1,130,5):
            self.doc_expire.insert(END, no)

        self.doc_trainer = Listbox(self.canvas_lists,exportselection=False)
        self.doc_trainer.place(x=580, y=25)
        self.doc_trainer.config(height=32, width=15, bg="#E9DAC1")
        

        self.doc_note = Listbox(self.canvas_lists,exportselection=False)
        self.doc_note.place(x=675, y=25)
        self.doc_note.config(height=32, width=22, bg="#E9DAC1")
     

        for no in range(1,130,5):
            self.doc_note.insert(END, no)
       
        self.fill_users_lists()
        self.doc_no.bind('<<ListboxSelect>>', self.onselect)
     
    

    def fill_users_lists(self):
        users = TR.get_all_users()
        for no in users:
            self.doc_users.insert(END, no)
            user_data = TR.get_user(no)
            for item,value in user_data.items():
                if item == "level":
                    self.doc_level.insert(END, value)
                if item == "trainer":
                    self.doc_trainer.insert(END, value)

      
       
    