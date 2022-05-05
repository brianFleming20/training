import User
import DataStore
import cryptocode

DS = DataStore.data_store()
UR = User

ENTRY = "ByH1KHdo7y30I6aN"

LI_user = []
class Login():

    def __init__(self,username,password):
        self.name = username
        self.password = password

        
    def get_user(self):
        user = UR.User(self.name,self.password)
        return user

    def get_logged_in_user(self):
        return LI_user


    def login_user(self):
        user_obj = self.get_user()
        user = DS.get_user_obj(user_obj)
        if user != False:
            for item,value in user.items():
                if item == "passwd":
                    password = value
                if item == "is_trainer":
                    admin = value
            plain_password = cryptocode.decrypt(password, ENTRY)
            #plain_password = password
            if plain_password == user_obj.password:
                self.write_user(user_obj)
                return True,admin
            else:
                return False,False
        else:
            return False,False

    def write_user(self,user):
        LI_user.append(user)

    
