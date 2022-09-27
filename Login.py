import User
import DataStore
import cryptocode
from tkinter import messagebox as mb

DS = DataStore.data_store()
UR = User


ENTRY = "ByH1KHdo7y30I6aN"
###################################
# The logged in user holder array #
###################################
LI_user = []


class Login():
    ##############################################################
    # Create a login object and passing it to the login checker  #
    ##############################################################
    def __init__(self,username,password):
        self.name = username
        self.password = password
        self.login_user()

    def get_logged_in_user(self):
        if LI_user:
            return LI_user[0]
        else:
            return False

    def login_user(self):
        #####################################################################
        # Clearing the login array for the next user to enter their details #
        # and get the login details of all of the users to check against.   #
        # The password from the login details is then decrypted and matched #
        # against the user input.                                           #
        #####################################################################
        self.reset_user()
        user_data = DS.get_login_data()
        for name in user_data:
            if name["Name"] == self.name:
                plain_password = cryptocode.decrypt(name['Password'],ENTRY)
                # encrypt_password = onetimepad.decrypt(name['Password'],ENTRY)
                # plain_password = onetimepad.decrypt(encrypt_password,ENTRY)
                if plain_password == self.password:
                    self.write_user(name['Name'], name['admin'])
                    return True
                else:
                    mb.showerror(title="Log in error",message="Login username or password incorrect.")
                    self.reset_user()
                    return False

    def write_user(self,user,admin):
        ############################################
        # Writes the successful login to the login #
        # array for the system to check who is     #
        # logged in.                               #
        ############################################
        LI_user.append(user)
        LI_user.append(admin)

    def reset_user(self):
        #############################################
        # Clears the login array.                   #
        #############################################
        LI_user.clear()




