import unittest

from app.extract.reader import *


class TestReader(unittest.TestCase):

    def test_filename_without_extension(self):
        self.assertEqual("file", filename_without_extension("file.txt"))

    def test_filepath_without_extension(self):
        self.assertEqual("file", filename_without_extension("/a/b/c/    file.txt"))

    def test_process_file(self):
        filename = '../../data/07-03-2020.pdf'
        process_file(filename)


if __name__ == '__main__':
    unittest.main()