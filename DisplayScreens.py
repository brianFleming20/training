'''
Created on 9 March 2022


@Author by Brian F



'''

import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import filedialog

import AdminUser as AU
import Screen as SC
import Training
import interface

TR = Training.Training()
INT = interface.interface()


class ShowMainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#F7ECDE')
        self.control = controller
        self.canvas_btndis = Canvas(self,bg="#E9DAC1",width=120,height=630)
        self.canvas_btndis.place(x=840,y=10)
        self.canvas_srdis = Canvas(self,bg="#E9DAC1", width=810,height=50)
        self.canvas_srdis.place(x=10,y=10)
        self.canvas_back = Canvas(self, bg="#E9DAC1", width=810,height=560)
        self.canvas_back.place(x=10,y=80)
        pdfFileObject = open('../test.pdf','rb')

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
        self.canvas_back.delete('all')
        Button(self.canvas_btndis,text="New", width=12 ,bg='#54BAB9').place(x=20,y=80)
        Button(self.canvas_btndis,text="Delete", width=12, bg='#54BAB9').place(x=20,y=160)
        Button(self.canvas_btndis,text="Edit", width=12, bg='#54BAB9').place(x=20,y=240)
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="Selected User").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)
        Label(self.canvas_back, text="Name",bg="#E9DAC1").place(x=50,y=50)
        Label(self.canvas_back, text="Documents Name ", bg="#E9DAC1").place(x=50,y=90)
        Label(self.canvas_back, text="Documents Issue ", bg="#E9DAC1").place(x=50,y=90)
        Label(self.canvas_back, text="Document Ref.", bg="#E9DAC1").place(x=50,y=130)
        Label(self.canvas_back, text="Trained By ", bg="#E9DAC1").place(x=50,y=170)
        Label(self.canvas_back, text="Trained On Date", bg="#E9DAC1").place(x=50,y=210)
        Label(self.canvas_back, text="Training Exrires", bg="#E9DAC1").place(x=50,y=250)
        Label(self.canvas_back, text="Competence Level", bg="#E9DAC1").place(x=50,y=290)
        Label(self.canvas_back, text="Notes", bg="#E9DAC1").place(x=50,y=340)
        self.a = self.canvas_back.create_text(400,55,text=" ",font=('Helvetica 12 bold'))
        self.b = self.canvas_back.create_text(400,95,text=" ",font=('Helvetica 12 bold'))
        self.h = self.canvas_back.create_text(400,95,text=" ",font=('Helvetica 12 bold'))
        self.c = self.canvas_back.create_text(400,135,text=" ",font=('Helvetica 12 bold'))
        self.d = self.canvas_back.create_text(400,175,text=" ",font=('Helvetica 12 bold'))
        self.e = self.canvas_back.create_text(400,215,text=" ",font=('Helvetica 12 bold'))
        self.f = self.canvas_back.create_text(400,255,text=" ",font=('Helvetica 12 bold'))
        self.g = self.canvas_back.create_text(400,295,text=" ",font=('Helvetica 12 bold'))
        self.text_area = tk.Text(self, height=8, width=50)
        self.text_area.place(x=500, y=500, anchor=CENTER)
        self.transfer_info()
        

    def transfer_info(self):
        self.canvas_back.itemconfigure(self.a, text=self.data[3])
        self.canvas_back.itemconfigure(self.b, text=self.data[1])
        self.canvas_back.itemconfigure(self.c, text=self.data[0])
        self.canvas_back.itemconfigure(self.d, text=self.data[7])
        self.canvas_back.itemconfigure(self.e, text=self.data[4])
        self.canvas_back.itemconfigure(self.f, text=self.data[6])
        self.canvas_back.itemconfigure(self.g, text=self.data[5])
        self.canvas_back.itemconfigure(self.h, text=self.data[5])
        self.text_area.insert('1.0',self.data[8])


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
        text = Text(self, width=80, height=30)
        self.time.set(TR.get_now_time())
        self.data.clear()
        self.data.extend(INT.extend_interface())
        self.canvas_back.delete('all')
        Button(self.canvas_btndis,text="New", width=12 ,bg='#54BAB9').place(x=20,y=80)
        Button(self.canvas_btndis,text="Delete", width=12, bg='#54BAB9').place(x=20,y=160)
        Button(self.canvas_btndis,text="Edit", width=12, bg='#54BAB9').place(x=20,y=240)
        Button(self.canvas_btndis,text="Main", width=12, command=self.return_to_home, bg='#54BAB9').place(x=20,y=500)
        Label(self.canvas_srdis, text="Document").place(x=10,y=15)
        Label(self.canvas_srdis, text="Search").place(x=250,y=15)
        search = Entry(self.canvas_srdis, textvariable=self.serach_item,width=25)
        search.place(x=300, y=15)
        Label(self.canvas_srdis,textvariable=self.time).place(x=700,y=18)
        self.text_area = tk.Text(self, height=33, width=85)
        self.text_area.place(x=30, y=100)
        
        
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




