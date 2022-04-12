'''
Creates a document object 
'''

from tkinter import messagebox as mb
import Training


TR = Training.Training()



class Document():

  
    

    def refresh_window(self):
        self.get_all_documets()

    
    def get_all_documets(self):
        all_docs = TR.get_documents()
        all_docs = []
        for doc_id,doc_data in all_docs.items():
            for item,data in doc_data.items():
                print(f"item {item} : data {data}")
                if item == "name":
                    name = data
                if item == "issue":
                    issue = data
                if item == "location":
                    loc = data
            doc = MakeDoc(name=name,ref=doc_id,issue=issue,location=loc)
            TR.add_document(doc)

           

  
        



    def update_doc_name(self,doc_obj,name):
        for document in TR.get_local_docs():
            if doc_obj.doc_name == document.doc_name:
                print(document.doc_name)
                document.doc_name = name
                print(f"---new doc name {document.doc_name}")
                TR.write_document(document)
                return True
            else:
                return False


    def update_issue_number(self, doc_obj,issue):
        for document in TR.get_local_docs():
            if doc_obj.issue_number == document.issue_number:
                document.issue_number = issue
                print(f"--- new issue number {document.issue_number}")
                TR.write_document(document)
                return True
            else:
                return False


    def update_ref_number(self, doc_obj,ref):
        for document in TR.get_local_docs():
            if doc_obj.reference_number == document.reference_number:
                document.reference_number = ref
                TR.write_document(document)
                print(f"--- new document ref {document.reference_number}")
                return True
            else:
                mb.showerror(title="Reference Error",message="The old reference number is the \nsame as the new number")
                return False    

    
    

class MakeDoc():

    def __init__(self,name="",issue=0.0,ref="",location=""):
        self.doc_name = name
        self.issue_number = issue
        self.reference_number = ref
        self.doc_location = location


    def get_document(self):
        return self