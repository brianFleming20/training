import unittest

import Documents

DOC = Documents.Document()


class DocsTests(unittest.TestCase):

   

    def test_add_document(self):
        print("Test adding a document")

        doc_name = "Spring tube assembly"

        DOC.set_doc_name(doc_name)

        result = DOC.get_doc_name()

        self.assertEqual(doc_name,result)


    def test_add_issue_number(self):
        print("Adding a issue number")

        issue_num = 1.0

        DOC.set_issue_number(issue_num)

        result = DOC.get_issue()

        self.assertEqual(issue_num,result)


    def test_add_a_reference(self):
        print("Adding a reference number")

        ref_num = "9070-1234"

        DOC.set_reference_number(ref_num)

        result = DOC.get_reference_number()

        self.assertEqual(ref_num,result)


    def test_update_name(self):
        print("Update a document name")

        old_doc_name = "Spring tube assembly"

        DOC.set_doc_name(old_doc_name)

        new_doc_name = "Spring Tubing Assembly"

        expected = DOC.update_doc_name(new_doc_name)

        result = DOC.get_doc_name()

        self.assertEqual(new_doc_name,result)

        self.assertEqual(True,expected)

        self.assertIsNot(old_doc_name, result)


    def test_update_issue_number(self):
        print("Update document issue number")

        old_issue_number = 1.0

        DOC.set_issue_number(old_issue_number)

        new_issue_number = 2.1

        expected = DOC.update_issue_number(new_issue_number)

        result = DOC.get_issue()

        self.assertEqual(new_issue_number, result)

        self.assertEqual(True,expected)

        self.assertGreater(result,old_issue_number)


    def test_update_ref_number(self):
        print("Update reference number")

        old_ref_number = "9070-1234"

        DOC.set_reference_number(old_ref_number)

        new_ref_number = "9070-1245"

        expected = DOC.update_ref_number(new_ref_number)

        result = DOC.get_reference_number()

        self.assertEqual(new_ref_number, result)

        self.assertEqual(True,expected)

        self.assertIsNot(old_ref_number,result)


 
    def test_remove_document(self):

        print("Test remove a document")

        doc_name = "Spring tube assembly"
        ref_num = "9070-1234"
        issue_num = 1.0

        DOC.set_doc_name(doc_name)
        DOC.set_issue_number(issue_num)
        DOC.set_reference_number(ref_num)

        doc_obj = DOC.get_doc_object()

        result = DOC.remove_document(doc_obj)

        self.assertEqual(result, True)



if __name__ == '__main__':
    unittest.main()