import unittest

from app.extract.reader import *


class TestReader(unittest.TestCase):

    def test_filename_without_extension(self):
        self.assertEqual("file", filename_without_extension("file.txt"))


if __name__ == '__main__':
    unittest.main()