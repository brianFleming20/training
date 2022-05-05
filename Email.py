
'''
Send an email to the user on training review date reached or near.
'''

from tkinter import messagebox as mb
import AdminUser as AU
import Training
from datetime import datetime, timedelta
import smtplib

TR = Training.Training()


class send_emails():

    def notify_training(self,a_user,the_ref):
        the_user = TR.get_user(a_user)
        trainer = the_user['trainer']
        email = the_user['email']
        for user, event in TR.get_all_training().items():
            for ref, items in event.items():
                if the_ref == ref:
                    review = items['review_date']
                    doc_name = items['name']
        print(f"train user {a_user} : ref {the_ref} : trainer {trainer} : email {email}")
        filepath = "training_email.txt"
        with open(filepath) as letter_file:
            contents = letter_file.read()
            contents = contents.replace(
                "[NAME]", a_user).replace("[document]",doc_name).replace(
                "[ref]",the_ref).replace("[expire]",review).replace("[trainer]",trainer)

        self.send_email(contents,email)

    def overdue_training(self,a_user,the_ref):
        the_user = TR.get_user(a_user)
        trainer = the_user['trainer']
        email = the_user['email']
        for user, event in TR.get_all_training().items():
            for ref, items in event.items():
                if the_ref == ref:
                    review = items['review_date']
                    doc_name = items['name']
        print(f"remind user {a_user} : ref {the_ref} : trainer {trainer} : email {email}")
        filepath = "expired_training.txt"
        with open(filepath) as letter_file:
            contents = letter_file.read()
            contents = contents.replace(
                "[NAME]", a_user).replace("[document]", doc_name).replace(
                "[ref]", the_ref).replace("[expire]", review).replace("[trainer]", trainer)
        self.send_email(contents, email)


    def send_copy_to_trainer(self,a_user,the_ref):
        the_user = TR.get_user(a_user)
        trainer = the_user['trainer']
        for user, event in TR.get_all_training().items():
            for ref, items in event.items():
                if the_ref == ref:
                    review = items['review_date']
                    doc_name = items['name']
        print(f"user {a_user} : ref {the_ref} : trainer {trainer} ")
        user2 = TR.get_user(trainer)
        trainer_email = user2['email']
        filepath = "training_email.txt"

        with open(filepath) as letter_file:
            contents = letter_file.read()
            contents = contents.replace(
                "[NAME]", trainer).replace("[document]",doc_name).replace(
                "[ref]",the_ref).replace("[expire]",review).replace("[user]",a_user)

        self.send_email(contents,trainer_email)

    def send_email(self, content,recipetent):
        my_email = "deltex.medical3mail@gmail.com"
        my_password = "Hf4aubkDFz6yHjRS"
        print(recipetent)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=my_email, password=my_password)
        #     connection.sendmail(
        #         from_addr=my_email,
        #         #to_addrs="lee.lindfield@deltexmedical.com",
        #         to_addrs="brian.fleming@deltexmedical.com",
        #         msg=f"Subject:Deltex Medical Training\n\n{content}"
        #     )