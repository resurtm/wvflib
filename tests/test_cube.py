import unittest

from tests.base import TestCase


class TestCube(TestCase):
    def test_common(self):
        self.assertEqual(self.f.name, 'cube.obj')
        self.assertTrue(len(self.f.objects) == 1)

    def test_materials(self):
        libs = self.f.material_libs
        self.assertTrue(len(libs) == 1)
        self.assertEqual(libs['cube.mtl'].name, 'cube.mtl')
        self.assertTrue(len(libs['cube.mtl'].materials) == 1)

        mat = libs['cube.mtl'].materials['cube']
        self.assertEqual(mat.name, 'cube')
        self.assertEqual(mat.material_lib, libs['cube.mtl'])

    @staticmethod
    def object_name():
        return 'cube'


if __name__ == '__main__':
    unittest.main()
