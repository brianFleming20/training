'''
Creates a document object 
'''

from tkinter import messagebox as mb
import Training




documents = []
class Document():

    def __init__(self,name="",issue=0.0,ref="",location=""):
        self.doc_name = name
        self.issue_number = issue
        self.reference_number = ref
        self.doc_location = location
        

    def get_doc_obj(self):
        print(self)
        return self


    def get_doc_name(self):
        return self.doc_name


    def get_issue(self):
        return self.issue_number


    def get_reference_number(self):
        return self.reference_number


    # def set_doc_name(self, name):
    #     self.doc_name = name


    # def set_issue_number(self,issue):
    #     self.issue_number = issue


    # def set_reference_number(self,ref):
    #     self.reference_number = ref

    # def set_doc_location(self, location):
    #     self.doc_location = location


    def get_doc_location(self):
        return self.doc_location


    # def save_doc_obj(self,doc_obj):
    #     documents.insert(0,doc_obj)




    # def save_all_docs_to_file(self):
    #     print(documents)
    #     for doc in documents:
            
    #         TR.write_document(doc)



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

    
    # def remove_document(self, doc_obj):
    #     docs = TR.get_documents()
    #     if docs != False:
    #         print(docs)
    #         for doc in docs:
    #             if doc == doc_obj.doc_name:
    #                 docs.pop(doc)
    #                 TR.write_documents(docs)
    #                 return True
    #             else:
    #                 return False
    #     else:
    #         return False
                    

