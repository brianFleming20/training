'''
Creates a user object for the system to use.
'''

import DataStore

DS = DataStore.data_store()


class User:

    def __init__(self, name,is_trainer=True, email=""):
        self.name = name
        self.is_trainer = is_trainer
        self.email = email






