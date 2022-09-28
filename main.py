'''
Created on 9 March 2022


@Author by Brian F

Naming convention
- Variables = no spaces, capitals for every word except the first : thisIsAVariable
- Local functions = prefixed with _, _ for spaces, no capitals : _a_local_function


on conversion to exe use auto-py-2-exe
include the email template files and the onetimepad library from venv/lib/site-packages/onetimepad.py


#         s = ttk.Separator(self.root, orient=VERTICAL)
#         s.grid(row=0, column=1, sticky=(N,S))
#
# To convert to an .exe file user auto py 2 exe
#   Start process by using 'python run.py' from the auto py 2 exe module
#   Include the text files that are used for the email templetes
#   Include the following folders for the encrypting process
#   'cryptocode' in the venv/Lib/site-packages/
#   'Cryptodome' in the venv/Lib/site-packages/

'''

import tkinter as tk
import LoginWindow as UL
import Screen as SC
import DisplayScreens as DSP
import AdminUser as AU
import os

num = "3013-0036"
Training_Version = f'Deltex Medical : Training Database V4.0 {num: >190s}   '
w = 1300  # window width
h = 870  # window height
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
                  DSP.show_event_window,
                  AU.AddNewUser,
                  AU.ShowUsers,
                  AU.EditUser,
                  AU.addNewDocument,
                  AU.editDocument,
                  AU.RecordTraining,
                  DSP.show_document_window
                  ):

            frame = F(container, self)
            

            self.frames[F] = frame
            

            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(UL.LoginWindow)

        try:
            import pyi_splash
            pyi_splash.update_text('UI Loaded ...')
            pyi_splash.close()
        except:
            pass
        

    def show_frame(self, newFrame):

        frame = self.frames[newFrame]
      
        frame.tkraise()

        # Does the frame have a refresh method, if so call it.
        if hasattr(newFrame, 'refresh_window') and callable(getattr(newFrame, 'refresh_window')):
            self.frames[newFrame].refresh_window()
            self.attributes('-topmost', True)


app = WindowController()
app.mainloop()