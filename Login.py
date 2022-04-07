import User
import DataStore

DS = DataStore.data_store()
UR = User.User()


class Login():

    def __init__(self,username,password):
        self.name = username
        self.password = password

        
    def get_user(self):
        UR.set_name(self.name)
        UR.set_password(self.password)
        user_obj = UR.get_user()
        return user_obj


    def login_user(self):
        user_obj = self.get_user()
        user = DS.get_user_obj(user_obj)
        if user != False:
            for item,value in user.items():
                if item == "pass":
                    password = value
                if item == "is_trainer":
                    admin = value
            if password == user_obj.password:
                return True,admin
            else:
                return False,False
        else:
            return False,False


  

    def write_user(self,trainer = False):
        user_obj = self.get_user()
        user_obj.set_is_trainer(trainer)

        done = DS.write_user(user_obj)
        if done:
            print("saved")
    
