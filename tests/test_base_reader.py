import unittest

from wvflib.reader.base_reader import BaseReader


class TestBaseReader(unittest.TestCase):
    def test_constructor(self):
        baseReader = BaseReader()
        with self.assertRaises(NotImplementedError):
            baseReader.before_read('')
        with self.assertRaises(NotImplementedError):
            baseReader.after_read()
        with self.assertRaises(NotImplementedError):
            baseReader.parsers()


if __name__ == '__main__':
    unittest.main()
