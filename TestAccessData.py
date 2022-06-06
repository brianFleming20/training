import unittest
import os

import AccessDataBase
import Login

AD = AccessDataBase.GetExternalData()
LOG = Login


ENTRY = "ByH1KHdo7y30I6aN"

class remoteDataTests(unittest.TestCase):

    def setUp(self):
        self.login_path = os.path.join("C:\\Users", os.getenv('username'), "Desktop\\Training\\Docs", "")


    def test_get_info_from_file(self):
        print("Test getting data from file")

        user = "Brian Fleming"
        password = "password"
        LOG.Login(user,password)

        AD.get_user_info()


if __name__ == '__main__':
    unittest.main()