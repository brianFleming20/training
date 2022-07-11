import unittest


import DataStore


DS = DataStore.data_store()



class TestSearchFile(unittest.TestCase):



    def test_search_file(self):
        print("Test search for file path")

        DS.search_path()

        DS.search_data_path()


if __name__ == '__main__':
    unittest.main()