import unittest

from tests.base import TestCase


class TestCube(TestCase):
    def test_common(self):
        self.assertTrue(self.f.name == 'capsule.obj')
        self.assertTrue(len(self.f.objects) == 1)
        self.assertEqual(self.f.objects[0].name, '')

    @staticmethod
    def object_name():
        return 'capsule'


if __name__ == '__main__':
    unittest.main()
