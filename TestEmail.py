import unittest
import Email
import Training

E = Email.send_emails()
TR = Training.Training()

class TestEmailSend(unittest.TestCase):

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

    def test_get_trainer(self):
        print("Test get trainer")
        user = "Carey Grey"
        ref = "9070-1203 6.2.4"
        user_obj = TR.get_training_record(user,ref)
        expected = user_obj['trainer']
        trainer, email = E.get_trainer(user,ref)

        result = trainer

        self.assertEqual(result,expected)

    def test_get_doc_details(self):
        print("Test get document details")
        user = "Carey Grey"
        doc_ref = "9070-1203 6.2.4"
        doc_name,review_date = E.get_document_details(user,doc_ref)

        doc_obj = TR.get_a_document(doc_ref)
        result1 = doc_obj['name']
        self.assertEqual(result1,doc_name)

        training = TR.get_training_record(user,doc_ref)
        result2 = training['review_date']
        if result2 == 0:
            result2 = TR.get_date_now()

        self.assertEqual(result2,review_date)

    def test_check_email(self):
        print("Test valid email")
        email = "brian.fleming@deltexmedical.com"
        fake_email = "no email yet"
        expected = "lee.lindfield@deltexmedical.com"

        result = E.check_valid_email(email)
        self.assertEqual(result,email)

        result2 = E.check_valid_email(fake_email)
        self.assertEqual(result2,expected)


if __name__ == '__main__':
    unittest.main()