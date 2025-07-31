import unittest
import os
from file_not_found_error import load_file_content

class TestLoadFileContent(unittest.TestCase):

    def setUp(self):
        # Create a test file
        self.test_file = "test_file.txt"
        with open(self.test_file, 'w') as f:
            f.write("Hello, test world!")

    def tearDown(self):
        # Remove the test file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_found(self):
        result = load_file_content(self.test_file)
        self.assertIn("Hello, test world!", result)

    def test_file_not_found(self):
        result = load_file_content("non_existent_file.txt")
        self.assertIn("does not exist", result)

if __name__ == "__main__":
    unittest.main()
