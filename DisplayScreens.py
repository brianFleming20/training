'''
Created on 9 March 2022


@Author by Brian F



'''

import tkinter as tk
import webbrowser
from tkinter import *


import AdminUser as AU
import Screen as SC
import Training
import interface

TR = Training.Training()
INT = interface.interface()




class show_user_window(tk.Frame):
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
        self.data = []

        

    def refresh_window(self):
        self.time.set(TR.get_now_time())
        self.data.clear()
        self.data.extend(INT.extend_interface())
        print(self.data)
        self.canvas_back.delete('all')
      
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="Selected User").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)
        Label(self.canvas_back, text="Name",bg="#E9DAC1").place(x=50,y=90)
        
        Label(self.canvas_back, text="Trained By ", bg="#E9DAC1").place(x=50,y=170)
        Label(self.canvas_back, text="Trained On Date", bg="#E9DAC1").place(x=50,y=210)
        Label(self.canvas_back, text="Training Exrires", bg="#E9DAC1").place(x=50,y=250)
        Label(self.canvas_back, text="Competence Level", bg="#E9DAC1").place(x=50,y=290)
        Label(self.canvas_back, text="Notes", bg="#E9DAC1").place(x=50,y=340)
        self.usr = self.canvas_back.create_text(400,90,text=" ",font=('Helvetica 12 bold'))
      
        self.train = self.canvas_back.create_text(400,170,text=" ",font=('Helvetica 12 bold'))
        self.train_date = self.canvas_back.create_text(400,210,text=" ",font=('Helvetica 12 bold'))
        self.exp = self.canvas_back.create_text(400,250,text=" ",font=('Helvetica 12 bold'))
        self.comp = self.canvas_back.create_text(400,290,text=" ",font=('Helvetica 12 bold'))
  
        self.text_area = tk.Text(self, height=8, width=50)
        self.text_area.place(x=50, y=450)
        Label(self.canvas_back, text="Trained on ").place(x=500,y=50)
        self.doc_name = Listbox(self, height=20, width=20)
        self.doc_name.place(x=480, y=180)
        self.doc_ref = Listbox(self, height=20, width=16)
        self.doc_ref.place(x=615, y=180)
        self.doc_issue = Listbox(self,height=20, width=10)
        self.doc_issue.place(x=730,y=180)
        self.doc_name.insert(END, "Document Name")
        self.doc_name.insert(END,"-----------------")
        self.doc_ref.insert(END, "Document Ref.")
        self.doc_ref.insert(END,"-----------------")
        self.doc_issue.insert(END,"Issue")
        self.doc_issue.insert(END,"----------------")
        self.transfer_info()
        

    def transfer_info(self):
        self.canvas_back.itemconfigure(self.usr, text=self.data[3])
      
        self.canvas_back.itemconfigure(self.train_date, text=self.data[4])
        self.canvas_back.itemconfigure(self.exp, text=self.data[6])
        self.canvas_back.itemconfigure(self.comp, text=self.data[5])
        self.canvas_back.itemconfigure(self.train, text=self.data[7])
        self.text_area.insert('1.0',self.data[8])
        self.doc_name.insert(END,self.data[1])
        self.doc_ref.insert(END,self.data[0])
        self.doc_issue.insert(END,self.data[2])



    def return_to_home(self):
        self.control.show_frame(SC.main_screen)



class show_document_window(tk.Frame):
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
        self.data = []


    def refresh_window(self):
        # text = Text(self, width=80, height=30)
        self.time.set(TR.get_now_time())
        self.data.clear()
        self.data.extend(INT.extend_interface())
        self.canvas_back.delete('all')
        Button(self.canvas_btndis,text="New", width=12 ,bg='#54BAB9').place(x=20,y=80)
        Button(self.canvas_btndis,text="Delete", width=12, bg='#54BAB9').place(x=20,y=160)
        Button(self.canvas_btndis,text="Edit", width=12, bg='#54BAB9').place(x=20,y=240)
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="Train on a document").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)
   
        Label(self.canvas_back, text="Trained on ").place(x=200,y=50)
        self.doc_name = Listbox(self.canvas_back, height=20, width=20)
        self.doc_name.place(x=180, y=150)
        self.doc_ref = Listbox(self.canvas_back, height=20, width=20)
        self.doc_ref.place(x=315, y=150)
        self.doc_issue = Listbox(self.canvas_back,height=20, width=10)
        self.doc_issue.place(x=480,y=150)
        self.doc_name.insert(END, "Document Name")
        self.doc_name.insert(END,"-----------------")
        self.doc_ref.insert(END, "Document Ref.")
        self.doc_ref.insert(END,"-----------------")
        self.doc_issue.insert(END,"Issue")
        self.doc_issue.insert(END,"----------------")
        print(self.data)
        for item in self.data:
            self.doc_ref.insert(END,item)

        self.doc_issue.insert(END,"")
        self.doc_name.insert(END,"")
        
        self.get_info()



    def return_to_home(self):
        self.control.show_frame(SC.main_screen)



    def get_info(self):
        pass

    
        
    def show_pdf(self):
        path = 'https://empower1902.bsientropy.com/deltexmedical/Login/Login'
        self.text_area.insert(webbrowser.open_new(path))
    



class show_event_window(tk.Frame):
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

    def refresh_window(self):
        self.time.set(TR.get_now_time())
        Button(self.canvas_btndis,text="New", width=12 ,command=self.add_user,bg='#54BAB9').place(x=20,y=80)
        Button(self.canvas_btndis,text="Delete", width=12, bg='#54BAB9').place(x=20,y=160)
        Button(self.canvas_btndis,text="Edit", width=12, bg='#54BAB9').place(x=20,y=240)
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="Events").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)


    def return_to_home(self):
        self.control.show_frame(SC.main_screen)

    def add_user(self):
        self.control.show_frame(AU.admin_user_window)




