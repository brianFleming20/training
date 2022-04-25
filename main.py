'''
Created on 9 March 2022


@Author by Brian F

Naming convention
- Variables = no spaces, capitals for every word except the first : thisIsAVariable
- Local functions = prefixed with _, _ for spaces, no capitals : _a_local_function


to do:


#         s = ttk.Separator(self.root, orient=VERTICAL)
#         s.grid(row=0, column=1, sticky=(N,S))

'''

import tkinter as tk
from tkinter import *

import LoginWindow as UL
import Screen as SC
import DisplayScreens as DSP
import AdminUser as AU


Training_Version = 'Deltex Medical : Training Register V 1'
w = 1000  # window width
h = 700  # window height
LARGE_FONT = ("Verdana", 14)

class WindowController(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title(Training_Version)
        # get window width and height
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        # calculate x and y coordinates for the window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        
        for F in (UL.LoginWindow,
                  SC.main_screen,
                  DSP.show_user_window,
                  DSP.show_document_window,
                  DSP.show_event_window,
                  AU.AddNewUser,
                  AU.ShowUsers,
                  AU.EditUser,
                  DSP.addNewDocument
                  ):

            frame = F(container, self)
            

            self.frames[F] = frame
            

            frame.grid(row=0, column=0, sticky="nsew")
            # self.attributes('-fullscreen', True)
            
            

        self.show_frame(UL.LoginWindow)
        
        
        
       

    def show_frame(self, newFrame):

        frame = self.frames[newFrame]
      
        frame.tkraise()

        # Does the frame have a refresh method, if so call it.
        if hasattr(newFrame, 'refresh_window') and callable(getattr(newFrame, 'refresh_window')):
            self.frames[newFrame].refresh_window()

    

              

app = WindowController()
app.mainloop()