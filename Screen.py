'''
Created on 9 March 2022


@Author by Brian F
The screen displays a set of lists to hold the training data form file
The upper part of the screen is to filter the required data in the
user centered data or a document centered data.


'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import DisplayScreens
import Training
import Documents
import interface
import LoginWindow as UL
import AdminUser
import Email
import AccessDataBase
import itertools

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
        #######################################################
        # Sets up the main screen attributes and resets the   #
        # index of the lists so the correct user information  #
        # is collected and transferred.                       #
        #######################################################
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.show_items = None
        self.idx = None
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.canvas_top = None
        self.index = -1
        self.document_name = None
        self.items = None
        self.canvas_lists = None
        self.canvas_search = None
        self.canvas_button = None
        self.control = controller
        self.base = Canvas(self, bg="#FBF8F1", width=self.ws - 10, height=self.hs - 10)
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
        self.anchor_button_top = self.hs / 8
        self.list_limit = 0
        self.focus_box = None

    def refresh_window(self):
        ##########################################################################
        # Setting up the screen canvases for each part of the screen.            #
        # The buttons are separated to allow the user distinguish information    #
        # from actions available.                                                #
        # The date is added to the screen to remind the user to check the        #
        # training review dates.                                                 #
        ##########################################################################
        self.index = -1
        self.show_items = {}
        self.canvas_button = Canvas(self, bg="#F7ECDE", width=self.ws / 8, height=self.hs - 50)
        self.canvas_button.place(x=self.ws - (self.ws / 7), y=self.anchor_button_top)
        self.canvas_search = Canvas(self, bg="#F7ECDE", width=self.ws - 30, height=self.hs / 10)
        self.canvas_search.place(x=10, y=15)
        self.canvas_lists = Canvas(self, bg="#F7ECDE", width=self.ws / 1.2, height=self.hs / 1.25)
        self.canvas_lists.place(x=10, y=self.anchor_button_top)
        self.canvas_top = Canvas(self, bg="#C2DED1", width=self.ws / 1.18, height=self.hs / 3.7)
        self.canvas_top.place(x=10, y=self.anchor_button_top)
        Button(self.canvas_button, text="Selected user", font=('Arial', 14), width=12, command=self.display_user, bg='#54BAB9').place(x=20, y=80)
        self.admin = Button(self.canvas_button,text="Admin", font=('Arial', 14), width=12, command=self.admin_user, bg='#54BAB9')
        self.admin.place(x=20, y=160)

        Button(self.canvas_button, text="Events", font=('Arial', 14), width=12, command=self.display_events, bg='#54BAB9').place(x=20, y=240)
        Button(self.canvas_button, text="Log Out", font=('Arial', 14), width=12, command=self.log_out, bg='#54BAB9').place(x=20, y=500)
        #################################################################
        # Drown down menu for the user to choose a trainee's name       #
        #################################################################
        names = TR.get_all_users()
        self.search_doc.set("")
        someStyle = ttk.Style()
        someStyle.configure('my.TMenubutton', font=('Futura', 16))
        search_name = ttk.OptionMenu(self.canvas_top, self.search_item, *names, style='my.TMenubutton')
        search_name['menu'].configure(font=('Futura', 16))
        search_name.place(x=80, y=80)
        self.search_item.set("Choose")
        ##################################################################
        # Labels for the screen and the user that is logged in.          #
        # The document name is lined out first of all, then added when   #
        # the document reference number is complete.                     #
        ##################################################################
        Label(self.canvas_search, text="Logged in -", font=('Courier', 14), bg="#F7ECDE").place(x=10, y=15)
        Label(self.canvas_top, text="Search", font=("Courier", 16), bg="#C2DED1").place(x=350, y=15)
        Label(self.canvas_top, text="Name", bg="#C2DED1").place(x=30, y=80)
        Label(self.canvas_top, text="Document Number", font=('Courier', 14), bg="#C2DED1").place(x=450, y=80)
        Label(self.canvas_top, text="Document Name", font=('Courier', 14), bg="#C2DED1").place(x=450, y=120)
        Label(self.canvas_top, text="Use Return to show Document users", bg="#C2DED1").place(x=200, y=183)

        self.document_name = Label(self.canvas_top, textvariable=self.search_document, bg="#C2DED1")
        self.document_name.place(x=650, y=120)
        doc = Entry(self.canvas_top, textvariable=self.search_doc, font=('Courier', 14), width=25)
        doc.place(x=650, y=80)
        btn1 = Button(self.canvas_top, text="Search", command=self.search_data, font=('Courier', 14), bg='#54BAB9')
        btn1.place(x=630, y=170)
        btn2 = Button(self.canvas_top, text="Clear search", command=self.refresh_window, font=('Courier', 14), bg="#54BAB9")
        btn2.place(x=780, y=170)
        self.search_document.set("----------------")
        ################################################################
        # Sets up the keys for the document numbers to be background   #
        # coloured according to the review date status.                #
        # Needs training is blue, overdue training is red and          #
        # is trained is green.                                         #
        ################################################################
        Label(self.canvas_top, text="Needs training soon", bg="#3AB0FF").place(x=10, y=160)
        Label(self.canvas_top, text="Overdue training      ", bg="#F24C4C").place(x=10, y=183)
        Label(self.canvas_top, text="Trained                      ", bg="#A0D995").place(x=10, y=137)
        ################################################################
        # If the logged in user is not an administrator, then the      #
        # admin functions button is disabled.                          #
        # This can be extended to include trainers as well.            #
        ################################################################
        admin = TR.get_user_admin()
        trainer = TR.get_trainer_status()
        if admin or trainer:
            self.admin.config(state=NORMAL)
        else:
            self.admin.config(state=DISABLED)
        #################################################################
        # Getting the logged in user details and the current date.      #
        #################################################################
        self.time.set(TR.get_date_now())
        logged_in_user = TR.get_logged_in_user()
        Label(self.canvas_search, text=logged_in_user, font=('Courier', 14),bg="#F7ECDE").place(x=150,y=15)
        Label(self.canvas_search, text="Date",font=('Courier', 14), bg="#F7ECDE").place(x=640, y=18)
        Label(self.canvas_search, textvariable=self.time, font=('Courier', 14), bg="#F7ECDE").place(x=700, y=18)
        ##################################################################
        # Start of the main display screen with the titles of the lists  #
        ##################################################################
        btn1.bind('<<Return>>', self.search_data)
        Label(self.canvas_top,
              text=" Document No.        Document Name              Issue       Name           Date Trained     Level    Expire Date       Trainer         Notes    ", font=('Courier', 10)).place(x=3,y=220)
        self.show_lists()
        self.fill_form()

    def admin_user(self):
        ################################################################
        # Link to the administrator section.                           #
        ################################################################
        self.control.show_frame(AU.ShowUsers)

    def search_data(self):
        ################################################################
        # Search for the user input from the dropdown trainee list     #
        # If the trainee is in the training records, the lists will    #
        # be filled in for the trainee and if the selected name is     #
        # als a trainer to others. This gives a complete view of the   #
        # name selected.                                               #
        ################################################################

        self.show_lists()
        if self.finish:
            self.fill_docs_list(self.get_document_requested())
        else:
            #############################################################
            # If the name is the default token of 'Choose' then no name #
            # has been selected.                                        #
            #############################################################
            if self.search_item.get() == "Choose":
                mb.showerror(title="Search Error", message="Please select a name.")
            else:
                self.fill_users_lists(self.get_selected_name())

    def get_document_requested(self):
        if TR.get_all_training():
            for name, item in TR.get_all_training().items():
                for doc, data in item.items():
                    if self.search_doc.get() == doc:
                        return doc[:9]

    def get_selected_name(self):
        if TR.get_all_training():
            for name, item in TR.get_all_training().items():
                if self.search_item.get() == name:
                    return name

    def fill_form(self):
        ##############################################################
        # When the flag of 'finish' is not set to true, the system   #
        # will continue to search for the document reference number  #
        # to be displayed under the document search entry area.      #
        # The system waits for 1 second before calling to check the  #
        # data input in the system again.                            #
        ##############################################################
        if not self.finish:
            self.control.after(1000, func=self.check_data)

    def check_data(self):
        ###############################################################
        # The system look through the documents to find the reference #
        # number and gets the document name back.                     #
        ###############################################################

        doc = TR.get_a_document(self.search_doc.get())
        if not doc:
            pass
        else:
            self.search_document.set(doc['name'])
            self.finish = True
            self.search_item.set("Choose")
        if not TR.get_all_training():
            self.update_system()
        Tk.update(self)
        self.fill_form()

    def selection_changed(self, event):
        selection = self.items.get()
        mb.showinfo(
                title="New Selection",
                message=f"Selected option: {selection}"
                )

    def display_user(self):
        if self.doc_no.size() == 0:
            mb.showerror(title="Selection Error", message="Please select a row.")
        else:
            self.control.show_frame(DSP.show_user_window)

    def display_document_window(self):
        self.control.show_frame(DSP.show_document_window)

    def display_events(self):
        ##########################################################
        # Displays the training review date screen.              #
        ##########################################################
        self.control.show_frame(DSP.show_event_window)

    def log_out(self):
        shut = mb.askyesno("Log Out", "Do you wish to proceed?")
        #################################
        # Clear screen and distroy app  #
        #################################
        if shut:
            self.canvas_search.destroy()
            self.canvas_lists.destroy()
            self.canvas_button.destroy()
            self.canvas_top.destroy()
            self.control.show_frame(UL.LoginWindow)

    def onselect(self, event):
        ######################################################
        # Receives the selected lists common index data.     #
        # Then transfers the data to the user screen         #
        ######################################################
        w = event.widget
        self.form_data.clear()
        if self.index == -1:
            self.idx = int(self.doc_no.curselection()[0])
            self.index = self.idx
            num = self.doc_no.get(self.idx)
            self.form_data.insert(0, num)
            self.doc_no.itemconfig(self.idx, {"bg": "#5CB8E4"})
            name = self.doc_name.get(self.idx)
            self.form_data.insert(1, name)
            self.doc_name.itemconfig(self.idx, {"bg": "#5CB8E4"})
            issue = self.doc_issue.get(self.idx)
            self.form_data.insert(2, issue)
            self.doc_issue.itemconfig(self.idx, {"bg": "#5CB8E4"})
            user = self.doc_users.get(self.idx)
            self.form_data.insert(3, user)
            self.doc_users.itemconfig(self.idx, {"bg": "#5CB8E4"})
            date_train = self.doc_train.get(self.idx)
            self.form_data.insert(4, date_train)
            self.doc_train.itemconfig(self.idx, {"bg": "#5CB8E4"})
            level = self.doc_level.get(self.idx)
            self.form_data.insert(5, level)
            self.doc_level.itemconfig(self.idx, {"bg": "#5CB8E4"})
            expire = self.doc_expire.get(self.idx)
            self.form_data.insert(6, expire)
            self.doc_expire.itemconfig(self.idx, {"bg": "#5CB8E4"})
            trainer = self.doc_trainer.get(self.idx)
            self.form_data.insert(7, trainer)
            self.doc_trainer.itemconfig(self.idx, {"bg": "#5CB8E4"})
            note = self.doc_note.get(self.idx)
            self.form_data.insert(8, note)
            self.doc_note.itemconfig(self.idx, {"bg": "#5CB8E4"})
            INT.provide_interface(self.form_data)

        else:
            self.index = -1
            #############################################################
            # If the lists area selected when there is no data entered  #
            # into them, does not crash, but re-displays the last       #
            # search data.                                              #
            #############################################################
            if self.search_item.get() == "Choose":
                self.show_lists()
                self.fill_docs_list(self.search_doc.get())
            else:
                self.show_lists()
                self.fill_users_lists(self.search_item.get())
      
    def show_lists(self):
        list_width = 13
        list_height = 24
        list_index = list_width * 5.4
        list_position = self.hs / 3.5
        self.idx = 0
        ######################################################################
        # Shows the data lists for the training data to be displayed .       #
        ######################################################################
        self.doc_no = Listbox(self.canvas_lists, exportselection=False)
        self.doc_no.place(x=5, y=list_position)
        self.doc_no.config(height=list_height, width=list_width + 3, bg="#E9DAC1", font=('Courier', 12))

        self.doc_name = Listbox(self.canvas_lists, exportselection=False)
        self.doc_name.place(x=list_index * 2.2, y=list_position)
        self.doc_name.config(height=list_height, width=24, bg="#E9DAC1", font=('Courier', 12))

        self.doc_issue = Listbox(self.canvas_lists, exportselection=False)
        self.doc_issue.place(x=list_index * 5.5, y=list_position)
        self.doc_issue.config(height=list_height, width=7, bg="#E9DAC1", font=('Courier', 12))

        self.doc_users = Listbox(self.canvas_lists, exportselection=False)
        self.doc_users.place(x=list_index * 6.4, y=list_position)
        self.doc_users.config(height=list_height, width=list_width, bg="#E9DAC1", font=('Courier', 12))

        self.doc_train = Listbox(self.canvas_lists, exportselection=False)
        self.doc_train.place(x=list_index * 8.3, y=list_position)
        self.doc_train.config(height=list_height, width=list_width, bg="#E9DAC1", font=('Courier', 12))

        self.doc_level = Listbox(self.canvas_lists, exportselection=False)
        self.doc_level.place(x=list_index * 10.2, y=list_position)
        self.doc_level.config(height=list_height, width=list_width - 5, bg="#E9DAC1", font=('Courier', 12))

        self.doc_expire = Listbox(self.canvas_lists, exportselection=False)
        self.doc_expire.place(x=list_index * 11.3, y=list_position)
        self.doc_expire.config(height=list_height, width=list_width, bg="#E9DAC1", font=('Courier', 12))

        self.doc_trainer = Listbox(self.canvas_lists, exportselection=False)
        self.doc_trainer.place(x=list_index * 13.2, y=list_position)
        self.doc_trainer.config(height=list_height, width=list_width, bg="#E9DAC1", font=('Courier', 12))

        self.doc_note = Listbox(self.canvas_lists, exportselection=False)
        self.doc_note.place(x=list_index * 15.1, y=list_position)
        self.doc_note.config(height=list_height, width=list_width + 1, bg="#E9DAC1", font=('Courier', 12))

        self.doc_id = Listbox(self.canvas_lists, exportselection=False)
        self.doc_id.place(x=list_index * 18, y=list_position)
        self.doc_id.config(height=2, width=2)

    def OnEntryDown(self, event):
        self.focus_box = event.widget
        if self.list_limit > self.idx:
            self.idx += 1
        if self.idx < 23:
            self.doc_name.itemconfig(self.idx - 1, {"bg": "#E9DAC1"})
            self.doc_issue.itemconfig(self.idx - 1, {"bg": "#E9DAC1"})
            self.doc_users.itemconfig(self.idx - 1, {"bg": "#E9DAC1"})
            self.doc_train.itemconfig(self.idx - 1, {"bg": "#E9DAC1"})
            self.doc_level.itemconfig(self.idx - 1, {"bg": "#E9DAC1"})
            self.doc_expire.itemconfig(self.idx - 1, {"bg": "#E9DAC1"})
            self.doc_trainer.itemconfig(self.idx - 1, {"bg": "#E9DAC1"})
            self.doc_note.itemconfig(self.idx - 1, {"bg": "#E9DAC1"})

        if self.idx > 23:
            lower = self.idx - 23
            upper = self.idx
            self.focus_box = event.widget
            self.show_list(lower, upper)
        self.show_selected()

    def OnEntryUp(self, event):
        if self.idx > 0:
            self.idx -= 1
        if self.idx < 23:
            self.doc_name.itemconfig(self.idx + 1, {"bg": "#E9DAC1"})
            self.doc_issue.itemconfig(self.idx + 1, {"bg": "#E9DAC1"})
            self.doc_users.itemconfig(self.idx + 1, {"bg": "#E9DAC1"})
            self.doc_train.itemconfig(self.idx + 1, {"bg": "#E9DAC1"})
            self.doc_level.itemconfig(self.idx + 1, {"bg": "#E9DAC1"})
            self.doc_expire.itemconfig(self.idx + 1, {"bg": "#E9DAC1"})
            self.doc_trainer.itemconfig(self.idx + 1, {"bg": "#E9DAC1"})
            self.doc_note.itemconfig(self.idx + 1, {"bg": "#E9DAC1"})

        if self.idx > 23:
            lower = self.idx - 23
            upper = self.idx
            self.focus_box = event.widget
            self.show_list(lower, upper)
        self.show_selected()

    def selection_stop(self, event):
        if event.keysym == 'Return':
            self.display_document_window()

    def fill_users_lists(self, name):
        upper = 23
        lower = 0
        self.show_items = {}
        self.search_document.set("----------------")
        self.search_doc.set("")
        ########################################################
        # Fill the lists using the username filter.            #
        ########################################################
        training_events = TR.get_all_training()
        for user, event in training_events.items():
            if user == name:
                for ref, items in event.items():
                    name = {"User": user}
                    items.update(name)
                    new_item = {ref: items}
                    self.show_items.update(new_item)
        self.list_limit = len(self.show_items) - 1
        self.show_list(lower, upper)
        self.doc_no.select_set(0)
        self.idx = int(self.doc_no.curselection()[0])
        self.doc_id.bind('<Down>', self.OnEntryDown)
        self.doc_id.bind('<Up>', self.OnEntryUp)
        self.doc_id.bind('<KeyRelease>', self.selection_stop)
        self.doc_id.focus_set()
        self.show_selected()

    def show_list(self, lower, upper):
        index = 0
        self.finish = False
        dict_slice = dict(itertools.islice(self.show_items.items(), lower, upper))
        for ref, items in dict_slice.items():
            self.doc_no.insert(index, ref)
            self.doc_train.insert(index, items['trained_on'])
            self.doc_expire.insert(index, items['review_date'])
            self.doc_name.insert(index, items['name'])
            user_item = TR.get_a_document(ref[:-2])
            if not user_item:
                user_item = TR.get_a_document(ref)
            self.doc_issue.insert(index, user_item['issue'])
            if not items['trainer']:
                trainer = "---"
            else:
                trainer = items['trainer']
            user = items['User']
            self.doc_users.insert(index, user)
            self.doc_level.insert(index, items['level'])

            self.doc_trainer.insert(index, trainer)
            if TR.get_email_date(items['review_date']):
                self.doc_no.itemconfig(index, {"bg": "#3AB0FF"})
            if TR.get_overdue_train(items['review_date']):
                self.doc_no.itemconfig(index, {"bg": "#F24C4C"})
            if TR.get_trained(items['review_date']):
                self.doc_no.itemconfig(index, {"bg": "#A0D995"})
            index += 1
            if self.idx > 23:
                self.focus_box.insert(index, items['note'])
            else:
                self.doc_note.insert(index, items['note'])

    def show_selected(self):
        index = self.idx
        if self.idx > 23:
            index = 23
        num = self.doc_no.get(index)
        self.form_data.insert(0, num)
        name = self.doc_name.get(index)
        self.form_data.insert(1, name)
        self.doc_name.itemconfig(index, {"bg": "#5CB8E4"})
        issue = self.doc_issue.get(index)
        self.form_data.insert(2, issue)
        self.doc_issue.itemconfig(index, {"bg": "#5CB8E4"})
        user = self.doc_users.get(index)
        self.form_data.insert(3, user)
        self.doc_users.itemconfig(index, {"bg": "#5CB8E4"})
        date_train = self.doc_train.get(index)
        self.form_data.insert(4, date_train)
        self.doc_train.itemconfig(index, {"bg": "#5CB8E4"})
        level = self.doc_level.get(index)
        self.form_data.insert(5, level)
        self.doc_level.itemconfig(index, {"bg": "#5CB8E4"})
        expire = self.doc_expire.get(index)
        self.form_data.insert(6, expire)
        self.doc_expire.itemconfig(index, {"bg": "#5CB8E4"})
        trainer = self.doc_trainer.get(index)
        self.form_data.insert(7, trainer)
        self.doc_trainer.itemconfig(index, {"bg": "#5CB8E4"})
        note = self.doc_note.get(index)
        self.form_data.insert(8, note)
        self.doc_note.itemconfig(index, {"bg": "#5CB8E4"})
        INT.provide_interface(self.form_data)
        Tk.update(self)

    def fill_docs_list(self, doc):
        ##############################################################
        # Fill the lists with document data from the document filter #
        ##############################################################
        upper = 23
        lower = 0
        index = 10
        self.show_items = {}
        self.search_item.set("Choose")
        training_events = TR.get_all_training()
        for user, event in training_events.items():
            for ref, items in event.items():
                if ref[:9] == doc:
                    name = {"User": user}
                    items.update(name)
                    ref = f"{ref}{index}"
                    new_item = {ref: items}
                    self.show_items.update(new_item)
                    index += 1

        self.list_limit = len(self.show_items) - 1
        self.show_list(lower, upper)
        self.doc_no.select_set(0)
        self.idx = int(self.doc_no.curselection()[0])
        self.doc_id.bind('<Down>', self.OnEntryDown)
        self.doc_id.bind('<Up>', self.OnEntryUp)
        self.doc_id.bind('<KeyRelease>', self.selection_stop)
        self.doc_id.focus_set()
        self.show_selected()

    def update_system(self):
        ADD.get_user_info()
        self.refresh_window()


class LoggedInUser():
    ###################################
    # Get system wide logged in user  #
    ###################################
    def set_logged_in_user(user):
        logged_user.clear()
        logged_user.insert(0,user)

    def get_logged_in_user(self):
        return logged_user[0]
    