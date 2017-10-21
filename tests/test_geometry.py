import unittest

from wvflib.geometry import Face


class TestGeometry(unittest.TestCase):
    def test_constructor(self):
        f = Face()
        self.assertTrue(len(f.vertices) == 0)


if __name__ == '__main__':
    unittest.main()
