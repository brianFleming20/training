'''
Creats a training event
'''
import datetime as DT
from tkinter import messagebox as mb
import DataStore
import User
import Login

DS = DataStore.data_store()
UR = User
LGI = Login


class Training:

    def get_date_now(self):
        presentime = DT.datetime.now()
        date = presentime.strftime('%d-%m-%Y')
        return date

    def get_review_date(self):
        dt = DT.datetime.now()
        dt = dt.replace(year=dt.year + 1)
        return dt.strftime('%d-%m-%y')

    def convert_date(self, review):
        review_date = self.check_date_format(review)
        if review_date[2:3] == "-":
            date_convert = DT.datetime.strptime(review_date, "%d-%m-%Y")
        else:
            date_convert = DT.datetime.strptime(review_date, "%d/%m/%Y")
        return date_convert

    def check_date_format(self, review):
        if review == "" or type(review) == int or type(review) == float:
            review = DT.datetime.strftime(DT.datetime.now(), "%d/%m/%Y")
        # if len(review) < 8:
        #     review = DT.datetime.strftime(DT.datetime.now(), "%d/%m/%Y")
        if type(review) == str:
            if len(review) < 9:
                mon = review[:6]
                year = review[6:]
                return f"{mon}20{year}"
            else:
                return review
        else:
            return DT.datetime.strftime(DT.datetime.now(), "%d/%m/%Y")

    def get_email_date(self, review_date):
        check = self.check_date_format(review_date)
        email_date = self.convert_date(check) - DT.timedelta(days=-7)
        present = DT.datetime.now()
        if email_date > present:
            return True
        else:
            return False

    def get_trained(self, review):
        review_date = self.check_date_format(review)
        if self.convert_date(review_date) > DT.datetime.now():
            return True
        else:
            return False

    def get_overdue_train(self, review_date):
        overdue = self.convert_date(review_date)
        limit = DT.datetime.now() - DT.timedelta(30)
        if overdue < limit:
            return True
        else:
            return False

    def get_documents(self):
        docs = DS.get_all_documents()
        return docs

    def get_user_password(self, name):
        user_obj = DS.get_login_data()
        password = False
        for user in user_obj:
            if name == user['Name']:
                password = user['Password']
        return password

    def get_a_document(self, doc_ref):
        documents = self.get_documents()
        doc_items = None
        for doc, item in documents.items():
            if doc_ref == doc:
                doc_items = item
        return doc_items

    def get_all_users(self):
        users = DS.read_users_data()
        return users

    def get_user(self, username):
        for user, data in self.get_all_users().items():
            if user == username:
                data["name"] = user
                return data

    def get_logged_in_user(self):
        return LGI.LI_user[0]

    def get_user_admin(self):
        return LGI.LI_user[1]

    def get_trainer_status(self):
        user = self.get_user(self.get_logged_in_user())
        if user['is_trainer']:
            return True
        else:
            return False

    def save_user(self, user):
        return DS.write_user(user)

    def save_user_login(self, user, password, admin):
        DS.write_user_admin(user.name, password, admin)

    def register_trained(self, document, user, level,trainer, note):
        doc_data = self.get_a_document(document)
        # user_data = self.get_user(user)
        if document in self.get_documents():
            training = CreateTraining(username=user, doc_ref=document, doc_name=doc_data['name'],
                                      train_date=self.get_date_now(),trainer=trainer,review=self.get_review_date(),
                                      level=level, logger=self.get_logged_in_user(),note=note)
            # training_to_file = [doc_data['issue'], user_data['name'], level, trainer, self.get_date_now(),
            #                     self.get_review_date(), self.get_logged_in_user(), self.get_date_now(), note]
            result = DS.add_training_to_user(training)
            # result = DS.update_training_file(training_to_file, document)

            return result
        else:
            return False

    def who_is_trainer(self):
        result = []
        for usr, value in self.get_all_users().items():
            for item, i_val in value.items():
                if item == "trainer":
                    result.insert(0, i_val)
        return list(dict.fromkeys(result))

    def get_all_training(self):
        return DS.get_all_training()

    def add_document(self, doc):
        DS.write_document(doc)

    def remove_document(self, ref):
        documents = self.get_documents()

        if ref in documents.keys():
            documents.pop(ref)
            DS.dump_documents(documents)
            return True
        else:
            mb.showerror(title="Reference Error", message="The old reference number not found.")
            return False

    def delete_user(self, name):
        users = self.get_all_users()
        if name in users.keys():
            user_set = self.get_all_users()
            user_set.pop(name)
            DS.login_delete_user(name)
            DS.dump_users(user_set)
            self.record_user_left(name)
            return True
        else:
            return False

    def record_user_left(self, name):
        training = self.get_all_training()
        for user,data in training.items():
            if user == name:
                update = CreateTraining(name)
                for ref,item in data.items():
                    update.username = name
                    update.document_ref = ref
                    update.trained_on = item['trained_on']
                    update.level = item['level']
                    update.trainer = item['trainer']
                    update.document_name = item['name']
                    update.review_date = item['review_date']
                    update.logger = item['trainer']
                    update.notes = "(No longer an employee)"
                    DS.add_training_to_user(update)



    def overwrite_docs(self, docs):
        DS.dump_documents(docs)

    def update_document(self, doc):
        self.add_document(doc)

    def get_blank_user(self):
        return UR.User(name="")

    def update_password(self, name, password):
        admin = DS.get_user_admin_status(name)
        if DS.update_user(name, password, admin):
            return True
        else:
            return False

    def get_training_record(self, username, doc_ref):
        training_data = []
        training = self.get_all_training()
        for name, doc in training.items():
            if name == username:
                training_data.append(doc)
                if doc_ref in training_data[0].keys():
                    return training_data[0][doc_ref]


class CreateTraining():

    def __init__(self, username="", doc_name="", trainer="",doc_ref="", train_date="", review="", logger="", level=0, note=""):
        self.notes = note
        self.trained_on = train_date
        self.trainer = trainer
        self.review_date = review
        self.username = username
        self.document_ref = doc_ref
        self.document_name = doc_name
        self.logger = logger
        self.level = level
