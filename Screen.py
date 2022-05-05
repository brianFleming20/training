'''
Created on 9 March 2022


@Author by Brian F



'''
import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from datetime import datetime, timedelta
from tkinter.ttk import Combobox
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
DOC = Documents.Document()
INT = interface.interface()
EM = Email.send_emails()
AU = AdminUser
ADD = AccessDataBase.GetExternatData()

logged_user = []
TIME_TO_WAIT = 5000 # in milliseconds

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
        self.show = None
        self.form_data = []

    def refresh_window(self):
        self.index = -1
        self.time.set(TR.get_date_now())
        logged_in_user = LoggedInUser.get_logged_in_user()
        admins = TR.get_all_trainers()
     
        Canvas(self,bg="#E9DAC1",width=970, height=680).place(x=10, y=10)
        self.canvas_button = Canvas(self,bg="#F7ECDE",width=120,height=630)
        self.canvas_button.place(x=840,y=10)
        self.canvas_search = Canvas(self,bg="#F7ECDE", width=810,height=50)
        self.canvas_search.place(x=10,y=10)
        self.canvas_lists = Canvas(self, bg="#F7ECDE", width=810,height=560)
        self.canvas_lists.place(x=10,y=80)
        Button(self.canvas_button,text="Selected user", width=12, command=self.display_user,bg='#54BAB9').place(x=20,y=80)
        self.admin = Button(self.canvas_button,text="Admin", width=12, command=self.admin_user,bg='#54BAB9')
        self.admin.place(x=20,y=160)
        Button(self.canvas_button,text="Documents", width=12, command=self.display_documents,bg='#54BAB9').place(x=20,y=240)
        Button(self.canvas_button,text="Events", width=12, command=self.display_events,bg='#54BAB9').place(x=20,y=320)
        Button(self.canvas_button,text="Update", width=12, command=self.display_update,bg='#54BAB9').place(x=20,y=400)
        Button(self.canvas_button,text="Log Out", width=12, command=self.log_out,bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_search, text="Logged in -").place(x=10,y=15)

        Label(self.canvas_search, text="Search").place(x=300,y=15)
        if logged_in_user in admins:
            self.admin.config(state=NORMAL)
        else:
            self.admin.config(state=DISABLED)
        Label(self.canvas_search, text=logged_in_user).place(x=80,y=15)
        search = Entry(self.canvas_search, textvariable=self.serach_item,width=25)
        search.place(x=350, y=15)
        self.items = Combobox(self.canvas_search,state="readonly",values=["Select","Person","Document","Training"])
        self.items.bind("<<ComboboxSelected>>", self.selection_changed)
        self.items.place(x=530, y=20)
        self.items.current(0)
        Label(self.canvas_search,textvariable=self.time).place(x=700,y=18)
        Label(self.canvas_lists, text="  Document No.       Document Name                Issue               Users           Date Trained       Level       Expire Date        Trainer                   Notes").place(x=5,y=5)
      
        # while self.index == -1:
        self.show_list_data()
       
        

    def admin_user(self):
        
        self.control.show_frame(AU.ShowUsers) 


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




    def display_documents(self):
        docs = TR.get_documents()
        INT.provide_interface([LoggedInUser.get_logged_in_user()])
        self.control.show_frame(DSP.show_document_window)


    def display_events(self):
        self.control.show_frame(DSP.show_event_window)


    def display_update(self):
        # win = tk.Tk()
        # w = 400  # width for the Tk root
        # h = 250  # height for the Tk root
        # ws = win.winfo_screenwidth()  # width of the screen
        # hs = win.winfo_screenheight()  # height of the screen
        ADD.get_data()
        # # calculate x and y coordinates for the Tk root window
        # x = (ws / 2) - (w / 2)
        # y = (hs / 2) - (h / 2)
        # # set the dimensions of the screen
        # # and where it is placed
        # win.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # # Set the geometry of tkinter frame
        # win.geometry("350x220")
        # # Initialize a Label widget
        # Label(win, text="Updating system for any changes...",
        #       font=('Helvetica 12 bold')).pack(pady=20)
        # win.overrideredirect(True)
        # # Automatically close the window after 3 seconds
        # win.after(1000, lambda: win.destroy())
        self.control.show_frame(main_screen)


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
        self.doc_no = Listbox(self.canvas_lists,exportselection=False)
        self.doc_no.place(x=5, y=25)
        self.doc_no.config(height=32, width=15, bg="#E9DAC1")

        self.doc_name = Listbox(self.canvas_lists,exportselection=False)
        self.doc_name.place(x=100, y=25)
        self.doc_name.config(height=32, width=20, bg="#E9DAC1")

        self.doc_issue = Listbox(self.canvas_lists,exportselection=False)
        self.doc_issue.place(x=225, y=25)
        self.doc_issue.config(height=32, width=10, bg="#E9DAC1")

        self.doc_users = Listbox(self.canvas_lists,exportselection=False)
        self.doc_users.place(x=290, y=25)
        self.doc_users.config(height=32, width=15, bg="#E9DAC1")

        self.doc_train = Listbox(self.canvas_lists,exportselection=False)
        self.doc_train.place(x=385, y=25)
        self.doc_train.config(height=32, width=12, bg="#E9DAC1")

        self.doc_level = Listbox(self.canvas_lists,exportselection=False)
        self.doc_level.place(x=462, y=25)
        self.doc_level.config(height=32, width=8, bg="#E9DAC1")

        self.doc_expire = Listbox(self.canvas_lists,exportselection=False)
        self.doc_expire.place(x=515, y=25)
        self.doc_expire.config(height=32, width=10, bg="#E9DAC1")

        self.doc_trainer = Listbox(self.canvas_lists,exportselection=False)
        self.doc_trainer.place(x=580, y=25)
        self.doc_trainer.config(height=32, width=12, bg="#E9DAC1")

        self.doc_note = Listbox(self.canvas_lists,exportselection=False)
        self.doc_note.place(x=658, y=25)
        self.doc_note.config(height=32, width=24, bg="#E9DAC1")

        self.fill_users_lists()
        self.doc_no.bind('<<ListboxSelect>>', self.onselect)
     
    

    def fill_users_lists(self):
        date = datetime.now() + timedelta(days=4)
        # check to match days difference only using split()
        time_left = str(date - datetime.now())[:2]
        users = TR.get_all_users()
        training_events = TR.get_all_training()
        try:
            for user,event in training_events.items():
                if user in users:
                    for ref,items in event.items():
                        self.doc_no.insert(END, ref)
                        self.doc_train.insert(END, items['trained_on'])
                        self.doc_expire.insert(END, items['review_date'])
                        self.doc_note.insert(END, items['note'])
                        self.doc_name.insert(END, items['name'])
                        item = TR.get_a_document(ref)
                        self.doc_issue.insert(END, item['issue'])
                        user_data = TR.get_user(user)
                        self.doc_users.insert(END, user)
                        self.doc_level.insert(END, user_data['level'])
                        self.doc_trainer.insert(END, user_data['trainer'])
                        due = items['review_date'][:2]
                        if items['review_date'] > TR.get_date_now() and int(due) <= int(time_left):
                            EM.notify_training(user,ref,1)
                            EM.send_copy_to_trainer(user,ref)
        except:
            pass


      
class LoggedInUser():

    def set_logged_in_user(user):
        logged_user.clear()
        logged_user.insert(0,user)


    def get_logged_in_user():
        return logged_user[0]
    