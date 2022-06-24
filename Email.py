
'''
Send an email to the user on training review date reached or near.
'''


import Training
import smtplib

TR = Training.Training()

class send_emails():

    def notify_training(self,a_user,doc_ref):
        filepath = "training_email.txt"
        sent = False
        user = TR.get_user(a_user)
        # training = TR.get_training_record(a_user,doc_ref)
        trainer, trainer_email = self.get_trainer(a_user,doc_ref)
        # if type(training['trainer']) == str:
        #     trainer = training['trainer']
        # else:
        #     trainer = "Trainer not stated"
        email = self.check_valid_email(user['email'])
        doc_name,review = self.get_document_details(doc_ref)
        with open(filepath) as letter_file:
            contents = letter_file.read()
            new_contents = contents.replace(
                "[NAME]", a_user).replace("[document]",doc_name).replace(
                "[ref]",doc_ref).replace("[expire]",review).replace(
                "[trainer]",trainer).replace("[email]",email)
            print(new_contents)
            sent = True
        # self.send_email(new_contents,email)
        print(new_contents)
        if sent:
            return True
        else:
            return False

    # def overdue_training(self,a_user,the_ref):
    #     the_user = TR.get_user(a_user)
    #     trainer = the_user['trainer']
    #     email = the_user['email']
    #     for user, event in TR.get_all_training().items():
    #         for ref, items in event.items():
    #             if the_ref == ref:
    #                 review = items['review_date']
    #                 doc_name = items['name']
    #     print(f"remind user {a_user} : ref {the_ref} : trainer {trainer} : email {email}")
    #     filepath = "expired_training.txt"
    #     with open(filepath) as letter_file:
    #         contents = letter_file.read()
    #         contents = contents.replace(
    #             "[NAME]", a_user).replace("[document]", doc_name).replace(
    #             "[ref]", the_ref).replace("[expire]", review).replace("[trainer]", trainer)
    #     self.send_email(contents, email)

    def send_copy_to_trainer(self,a_user,doc_ref):
        sent = False
        filepath = "trainer_notification.txt"
        trainer, trainer_email = self.get_trainer(a_user, doc_ref)
        doc_name,review = self.get_document_details(doc_ref)
        with open(filepath) as letter_file:
            contents = letter_file.read()
            new_contents = contents.replace(
                "[NAME]", trainer).replace("[document]",doc_name).replace(
                "[ref]",doc_ref).replace("[expire]",review).replace(
                "[user]",a_user).replace("[email]",trainer_email)
            print(new_contents)
            sent = True
        # self.send_email(new_contents,trainer_email)
        print(new_contents)
        if sent:
            return True
        else:
            return False

    def send_email(self, content,recipetent):
        my_email = "deltex.medical3mail@gmail.com"
        # my_password = "Hf4aubkDFz6yHjRS"
        app_password = "yicacircbaoqimgb"
        print(content)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(
                from_addr=my_email,
                # to_addrs="lee.lindfield@deltexmedical.com",
                # to_addrs="brian.fleming@deltexmedical.com",
                to_addrs=recipetent,
                msg=f"Subject:Deltex Medical Training\n\n{content}"
            )

    def check_valid_email(self, email):
        if '@' not in email:
            return "lee.lindfield@deltexmedical.com"
        else:
            return email

    def get_document_details(self, doc):
        doc_name = "---"
        review = "---"
        for user, event in TR.get_all_training().items():
            for ref, items in event.items():
                if doc == ref:
                    if type(items['review_date']) == str:
                        review = items['review_date']
                    else:
                        review = TR.get_date_now()
                    doc_name = items['name']
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

