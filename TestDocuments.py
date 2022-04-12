import unittest

import Documents

DOC = Documents


class DocsTests(unittest.TestCase):

    def setUp(self):
        self.doc1 = DOC.MakeDoc("Spring Tubing",10,"9070-1234","the_location_here")
        self.doc2 = DOC.MakeDoc("Spring Tube Assembly",8,"9070-8723","another_location")
        self.doc3 = DOC.MakeDoc("Printing",2,"3000-0123","Location_Location")

    def test_add_document(self):
        print("Test adding a document")
        doc_name = "Spring tube assembly"

        doc = DOC.MakeDoc(name=doc_name)

        result = doc.doc_name
        print(f"result = {doc.doc_name}")

        self.assertEqual(doc_name,result)


    def test_add_issue_number(self):
        print("Adding a issue number")

        issue_num = 1.0

        doc = DOC.MakeDoc(issue=issue_num)

        result = doc.issue_number

        self.assertEqual(issue_num,result)


    def test_add_a_reference(self):
        print("Adding a reference number")

        ref_num = "9070-1234"

        doc = DOC.MakeDoc(ref=ref_num)

        result = doc.reference_number

        self.assertEqual(ref_num,result)


    def test_document_location(self):
        print("Test file location")

        location = "somelocation"

        doc = DOC.MakeDoc(location=location)

        result = doc.doc_location

        self.assertEqual(result,location)


    def test_get_all_documents(self):
        print("Test get all documents")

        result_docs = []

        

        DOC.Document.insert_a_document(self,self.doc1)
        DOC.Document.insert_a_document(self,self.doc2)
        DOC.Document.insert_a_document(self,self.doc3)

        all_docs = DOC.Document.get_documents(self)

        for adoc in all_docs:
            result_docs.insert(0,adoc)

           

        self.assertEqual(result_docs[0],self.doc1)
        self.assertEqual(result_docs[1],self.doc2)
        self.assertEqual(result_docs[2],self.doc3)
      




    def test_update_name(self):
        print("Update a document name")

        doc1 = DOC.MakeDoc("Spring Tubing",10,"9070-1234","the_location_here")
        DOC.Document.insert_a_document(self,doc1)

        new_doc_name = "Spring Tubing Assembly"

        expected = DOC.Document.update_doc_name(self,doc1,new_doc_name)

        self.assertEqual(True,expected)





    def test_update_issue_number(self):
        print("Update document issue number")

        doc2 = DOC.MakeDoc("Spring Tube Assembly",8,"9070-8723","another_location")
        DOC.Document.insert_a_document(self,doc2)

        new_issue_number = 8.1

        expected = DOC.Document.update_issue_number(self,doc2,new_issue_number)

        self.assertEqual(True,expected)




    def test_update_ref_number(self):
        print("Update reference number")

        doc3 = DOC.MakeDoc(name="Printing",issue=2,ref="3000-0123",location="Location_Location")
        DOC.Document.insert_a_document(self,doc3)

        new_ref_number = "9070-1245"

        expected = DOC.Document.update_ref_number(self,doc3,new_ref_number)

        self.assertEqual(True,expected)

    

   
 
    def test_remove_document(self):
        print("Test remove a document")

        doc_name1 = "Spring tube assembly"
        ref_num1 = "9070-1234"
        issue_num1 = 1.0
        location1 = "some-location"

        doc_name2 = "Spring tubeing"
        ref_num2 = "9070-4321"
        issue_num2 = 12.0
        location2 = "other-location"

        doc_name3 = "Monitors"
        ref_num3 = "9070-9812"
        issue_num3 = 4.0
        location3 = "again-location"

        doc1 = DOC.MakeDoc(name=doc_name1,issue=issue_num1,ref=ref_num1,location=location1)
        DOC.Document.insert_a_document(self,doc1)
 
        doc2 = DOC.MakeDoc(name=doc_name2,issue=issue_num2,ref=ref_num2,location=location2)
        DOC.Document.insert_a_document(self,doc2)

        doc3 = DOC.MakeDoc(name=doc_name3,issue=issue_num3,ref=ref_num3,location=location3)
        DOC.Document.insert_a_document(self,doc3)

        result = DOC.Document.remove_document(self,doc2)

        self.assertEqual(result, True)



if __name__ == '__main__':
    unittest.main()