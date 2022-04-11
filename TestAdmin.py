import unittest
import AdminUser
import Training


AU = AdminUser
TR = Training.Training()


class AdminTests(unittest.TestCase):

    def setUp(self):
        self.admin = False
        self.name = "Alan"
        self.password = "letmein"
        self.conf_pass = "letmein"
        self.level = 1


    def test_add_user(self):
        print("Test add new user")
        

        AU.AddNewUser.add_user(self,self.name,self.password,self.conf_pass,self.level)
        users = TR.get_all_users()
        if self.name in users.keys():
            result = self.name

        self.assertEqual(result,self.name)

    def test_change_name(self):
        print("Test change name")

        name = "Linn"
        result = None

        TR.change_name("Lee",name)

        users = TR.get_all_users()
        if name in users.keys():
            result = name

        self.assertEqual(result,name)




    def test_change_password(self):
        print("Test change password")





    def test_change_level(self):
        print("Test change level")


    def test_delete_user(self):
        print("Delete a user")

        users = TR.get_all_users()
        print(users)

        name = "Lee"

        deleted = TR.delete_user(name)

        new_users = TR.get_all_users()

        TR.save_all_users(new_users)

        if name in new_users.keys():
            result = True
        else:
            result = False

        self.assertEqual(result,deleted)

    


if __name__ == '__main__':
    unittest.main()