import unittest

from tests.base import TestCase


class TestCube(TestCase):
    def test_common(self):
        self.assertTrue(self.f.name == 'cube.obj')
        self.assertTrue(len(self.f.objects) == 1)

    @staticmethod
    def object_name():
        return 'cube'


if __name__ == '__main__':
    unittest.main()
