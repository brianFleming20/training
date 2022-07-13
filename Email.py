
'''
Send an email to the user on training review date reached or near.
'''
import os

import Training
import smtplib

TR = Training.Training()

class send_emails():

    def notify_training(self,a_user,doc_ref):
        filepath = "training_email.txt"
        user = TR.get_user(a_user)
        trainer, trainer_email = self.get_trainer(a_user,doc_ref)
        email = self.check_valid_email(user['email'])
        doc_name,review = self.get_document_details(a_user,doc_ref)
        with open(filepath) as letter_file:
            contents = letter_file.read()
            new_contents = contents.replace(
                "[NAME]", a_user).replace("[document]",doc_name).replace(
                "[ref]",doc_ref).replace("[expire]",review).replace(
                "[trainer]",trainer).replace("[email]",email)

        if self.send_email(new_contents,email):
            return True
        else:
            return False

    def send_copy_to_trainer(self,a_user,doc_ref):
        filepath = "trainer_notification.txt"
        trainer, trainer_email = self.get_trainer(a_user, doc_ref)
        doc_name,review = self.get_document_details(a_user,doc_ref)
        with open(filepath) as letter_file:
            contents = letter_file.read()
            new_contents = contents.replace(
                "[NAME]", trainer).replace("[document]",doc_name).replace(
                "[ref]",doc_ref).replace("[expire]",review).replace(
                "[user]",a_user).replace("[email]",trainer_email)
        if self.send_email(new_contents,trainer_email):
            return True
        else:
            return False

    def send_email(self, content,recipetent):
        my_email = "deltex.medical3mail@gmail.com"
        # my_password = "Hf4aubkDFz6yHjRS"
        app_password = "yicacircbaoqimgb"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(
                from_addr=my_email,
                # to_addrs="lee.lindfield@deltexmedical.com",
                # to_addrs="brian.fleming@deltexmedical.com",
                to_addrs=recipetent,
                msg=f"Subject:Deltex Medical Training Request\n\n{content}"
            )
        return True

    def check_valid_email(self, email):
        if '@' not in email:
            return "lee.lindfield@deltexmedical.com"
        else:
            return email

    def get_document_details(self, user,doc_ref):
        doc_name = "---"
        review = "---"
        events = TR.get_training_record(user,doc_ref)
        if type(events['review_date']) == str:
            review = events['review_date']
        else:
            review = TR.get_date_now()
        doc_name = events['name']
        return doc_name,review

    def get_trainer(self, user, doc_ref):
        training = TR.get_training_record(user, doc_ref)
        trainer_user = None
        if type(training['trainer']) == str:
            trainer = training['trainer']
            trainer_user = TR.get_user(trainer)
        else:
            trainer = " not stated, redirected to Lee Lindfield"
        email = self.check_valid_email(trainer_user['email'])
        if email:
            trainer_email = email
        else:
            trainer_email = "lee.lindfield@deltexmedical.com"
        return trainer,trainer_email

