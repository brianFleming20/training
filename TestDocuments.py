import unittest

import Documents
import Training

DOC = Documents
TR = Training.Training()

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

        result_docs = TR.get_documents()

        result = len(result_docs)

        self.assertGreater(result,0)

        for a_key,a_doc in result_docs.items():
            self.assertIsNot(a_key,None)
            self.assertIsNot(a_doc,None)

      




    def test_update_name(self):
        print("Update a document name")

        doc1 = DOC.MakeDoc("Spring Tubing",10,"9070-1234","the_location_here")
        TR.add_document(doc1)

        new_doc_name = "Spring Tubing Assembly"

        expected = DOC.Document.update_doc_name(self,doc1,new_doc_name)

        self.assertEqual(True,expected)





    def test_update_issue_number(self):
        print("Update document issue number")

        doc2 = DOC.MakeDoc("Spring Tube Assembly",8,"9070-8723","another_location")
        TR.add_document(doc2)

        new_issue_number = 8.1

        expected = DOC.Document.update_issue_number(self,doc2,new_issue_number)

        self.assertEqual(True,expected)




    def test_update_ref_number(self):
        print("Update reference number")

        doc3 = DOC.MakeDoc(name="Printing",issue=2,ref="3000-0123",location="Location_Location")
        TR.add_document(doc3)

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
        TR.add_document(doc1)
 
        doc2 = DOC.MakeDoc(name=doc_name2,issue=issue_num2,ref=ref_num2,location=location2)
        TR.add_document(doc2)

        doc3 = DOC.MakeDoc(name=doc_name3,issue=issue_num3,ref=ref_num3,location=location3)
        TR.add_document(doc3)

        test = TR.remove_document(doc2.reference_number)

        docs = TR.get_documents()

        if doc2.reference_number in docs.keys():
            result = True
        else:
            result = False

        self.assertEqual(test, True)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()