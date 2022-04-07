'''
Creates a document object 
'''

from tkinter import messagebox as mb
import Training
import DataStore

TR = Training
DS = DataStore.data_store()

class Document():

    def __init__(self):
        self.doc_name = ""
        self.issue_number = 0.0
        self.reference_number = ""
        self.doc_location = ""
        self.documents = []

    def get_doc_obj(self):
        return self


    def get_doc_name(self):
        return self.doc_name


    def get_issue(self):
        return self.issue_number


    def get_reference_number(self):
        return self.reference_number


    def set_doc_name(self, name):
        self.doc_name = name


    def set_issue_number(self,issue):
        self.issue_number = issue


    def set_reference_number(self,ref):
        self.reference_number = ref

    def set_doc_location(self, location):
        self.doc_location = location


    def get_doc_location(self):
        return self.doc_location


    def save_doc_obj(self):
        self.documents.insert(0,self.get_doc_obj())


    def get_all_documents(self):
        return self.documents


    def get_doc_object(self):
        return self


    def save_docs_to_file(self):
        DS.write_documents(self.get_all_documents())


    def update_doc_name(self,name):
        old_name = self.get_doc_name()

        if old_name == name:
            mb.showerror(title="Document Error",message="The old and new document names are the same.")
            return False
        else:
            self.set_doc_name(name)
         
            return True


    def update_issue_number(self, issue):
        old_issue = self.get_issue()

        if old_issue == issue:
            mb.showerror(title="Issue Number Error",message="The new issue number is the same as the\nnew issue number")
            return False
        else:
            self.set_issue_number(issue)
            return True


    def update_ref_number(self, ref):
        old_ref = self.get_reference_number()

        if old_ref == ref:
            mb.showerror(title="Reference Error",message="The old reference number is the \nsame as the new number")
            return False
        else:
            self.set_reference_number(ref)
            return True

    
    def remove_document(self, document):
        train = TR.Training()
        docs = []
        docs.insert(0,train.get_document())
        for doc in docs:
            if doc.name == document.name:
                docs.pop(doc)
                train.write_documents(docs)
                return True
            else:
                return False
                    

