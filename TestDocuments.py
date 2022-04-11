import unittest

import Documents

DOC = Documents


class DocsTests(unittest.TestCase):

    def setUp(self):
        self.doc = DOC.Document()

    def test_add_document(self):
        print("Test adding a document")
        doc_name = "Spring tube assembly"

        doc = DOC.Document(name=doc_name)

        result = self.doc.get_doc_name()
        print(f"result = {doc.doc_name}")

        self.assertEqual(doc_name,result)


    def test_add_issue_number(self):
        print("Adding a issue number")

        issue_num = 1.0

        DOC.Document(issue=issue_num)

        result = self.doc.get_issue()

        self.assertEqual(issue_num,result)


    def test_add_a_reference(self):
        print("Adding a reference number")

        ref_num = "9070-1234"

        DOC.Document(ref=ref_num)

        result = self.doc.get_reference_number()

        self.assertEqual(ref_num,result)


    def test_update_name(self):
        print("Update a document name")

        old_doc_name = "Spring tube assembly"

        DOC.Document(name=old_doc_name)

        new_doc_name = "Spring Tubing Assembly"

        expected = self.doc.update_doc_name(new_doc_name)

        result = self.doc.get_doc_name()

        self.assertEqual(new_doc_name,result)

        self.assertEqual(True,expected)

        self.assertIsNot(old_doc_name, result)


    def test_update_issue_number(self):
        print("Update document issue number")

        old_issue_number = 1.0

        DOC.Document(issue=old_issue_number)

        new_issue_number = 2.1

        expected = self.doc.update_issue_number(new_issue_number)

        result = self.doc.get_issue()

        self.assertEqual(new_issue_number, result)

        self.assertEqual(True,expected)

        self.assertGreater(result,old_issue_number)


    def test_update_ref_number(self):
        print("Update reference number")

        old_ref_number = "9070-1234"

        DOC.Document(ref=old_ref_number)

        new_ref_number = "9070-1245"

        expected = self.doc.update_ref_number(new_ref_number)

        result = self.doc.get_reference_number()

        self.assertEqual(new_ref_number, result)

        self.assertEqual(True,expected)

        self.assertIsNot(old_ref_number,result)

   
 
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

        # DOC.set_doc_name(doc_name1)
        # DOC.set_issue_number(issue_num1)
        # DOC.set_reference_number(ref_num1)
        # DOC.set_doc_location(location1)
        DOC.Document(name=doc_name1,issue=issue_num1,ref=ref_num1,location=location1)

        doc_obj1 = self.doc.get_doc_object()
        self.doc.update_doc_file(doc_obj1)

        # DOC.set_doc_name(doc_name2)
        # DOC.set_issue_number(issue_num2)
        # DOC.set_reference_number(ref_num2)
        # DOC.set_doc_location(location2)
        DOC.Document(name=doc_name2,issue=issue_num2,ref=ref_num2,location=location2)

        doc_obj2 = self.doc.get_doc_object()
        self.doc.update_doc_file(doc_obj2)

        # DOC.set_doc_name(doc_name3)
        # DOC.set_issue_number(issue_num3)
        # DOC.set_reference_number(ref_num3)
        # DOC.set_doc_location(location3)
        DOC.Document(name=doc_name3,issue=issue_num3,ref=ref_num3,location=location3)

        doc_obj3 = self.doc.get_doc_object()
        self.doc.update_doc_file(doc_obj3)


     

        result = self.doc.remove_document(doc_obj1)

        self.assertEqual(result, True)



if __name__ == '__main__':
    unittest.main()