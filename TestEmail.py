import unittest
import Email

E = Email.send_emails()

class TestEmailSend(unittest.TestCase):

    def setUp(self):
        pass

    def test_send_email(self):
        print("Test sending user email")
        user = "Carey Grey"
        ref = "9070-3131"
        expected = True

        result = E.notify_training(user,ref)

        self.assertEqual(expected, result)

    def test_send_trainer_email(self):
        print("Send trainer emails")
        user = "Carey Grey"
        ref = "9070-1203 6.2.4"
        expected = True

        result = E.send_copy_to_trainer(user,ref)

        self.assertEqual(expected,result)


if __name__ == '__main__':
    unittest.main()