'''
Creates a document object 
'''


class MakeDoc():

    def __init__(self,name="",issue=0,ref=""):
        self.doc_name = name
        self.issue_number = issue
        self.reference_number = ref


    def get_document(self):
        return self