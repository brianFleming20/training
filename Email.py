
'''
Send an email to the user on training review date reached or near.
'''


import Training
import smtplib

TR = Training.Training()

class send_emails():

    def notify_training(self,a_user,the_ref):
        sent = False
        doc_name = "---"
        review = "---"
        the_user = TR.get_user(a_user)
        if type(the_user['trainer']) == str:
            trainer = the_user['trainer']
        else:
            trainer = "Trainer not stated"
        email = the_user['email']
        for user, event in TR.get_all_training().items():
            for ref, items in event.items():
                if the_ref == ref:
                    if type(items['review_date']) == str:
                        review = items['review_date']
                    else:
                        review = TR.get_date_now()
                    doc_name = items['name']
        print(f"{doc_name} : {review} : {trainer}")
        filepath = "training_email.txt"
        with open(filepath) as letter_file:
            contents = letter_file.read()
            contents = contents.replace(
                "[NAME]", a_user).replace("[document]",doc_name).replace(
                "[ref]",the_ref).replace("[expire]",review).replace(
                "[trainer]",trainer).replace("[email]",email)
            sent = True
        self.send_email(contents,email)
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


    def send_copy_to_trainer(self,a_user,the_ref):
        sent = False
        doc_name = "---"
        review = "---"
        the_user = TR.get_user(a_user)
        if type(the_user['trainer']) == str:
            trainer = the_user['trainer']
        else:
            trainer = " not stated"
        for user, event in TR.get_all_training().items():
            for ref, items in event.items():
                if the_ref == ref:
                    if type(items['review_date']) == str:
                        review = items['review_date']
                    else:
                        review = TR.get_date_now()
                    doc_name = items['name']
        print(f" > {trainer} < ")
        if trainer == " not stated" or trainer == 0.0 or trainer is None:
            trainer = "Lee Lindfield"
        if type(trainer) == str:
            user2 = TR.get_user(trainer)
            trainer_email = user2['email']
        else:
            trainer_email = "lee.lindfield@deltexmedical.com"
        filepath = "training_email.txt"
        with open(filepath) as letter_file:
            contents = letter_file.read()
            contents = contents.replace(
                "[NAME]", trainer).replace("[document]",doc_name).replace(
                "[ref]",the_ref).replace("[expire]",review).replace(
                "[user]",a_user).replace("[email]",trainer_email)
            sent = True
        self.send_email(contents,trainer_email)
        if sent:
            return True
        else:
            return False

    def send_email(self, content,recipetent):
        my_email = "deltex.medical3mail@gmail.com"
        my_password = "Hf4aubkDFz6yHjRS"
        print(content)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=my_email, password=my_password)
        #     connection.sendmail(
        #         from_addr=my_email,
        #         #to_addrs="lee.lindfield@deltexmedical.com",
        #         to_addrs="brian.fleming@deltexmedical.com",
        #         msg=f"Subject:Deltex Medical Training\n\n{content}"
        #     )
