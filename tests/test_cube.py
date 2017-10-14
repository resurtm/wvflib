import unittest

from tests.base import TestCase


class TestCube(TestCase):
    def test_common(self):
        self.assertEqual(self.f.name, 'cube.obj')
        self.assertTrue(len(self.f.objects) == 1)
        self.assertEqual(self.f.objects[0].name, 'cube')

    def test_material_libs(self):
        libs = self.f.material_libs

        self.assertTrue(len(libs) == 1)
        self.assertEqual(libs['cube.mtl'].name, 'cube.mtl')
        self.assertTrue(len(libs['cube.mtl'].materials) == 1)
        self.assertEqual(self.f.objects[0].material_lib, libs['cube.mtl'])

    def test_materials(self):
        lib = self.f.material_libs['cube.mtl']
        mat = lib.materials['cube']

        self.assertEqual(mat.name, 'cube')
        self.assertEqual(mat.material_lib, lib)

        self.assertEqual(mat.Ns, 10.0)
        self.assertEqual(mat.Ni, 1.5)
        self.assertEqual(mat.d, 1.0)
        self.assertEqual(mat.Tr, 0.0)
        self.assertEqual(mat.Tf, (1.0, 1.0, 1.0))
        self.assertEqual(mat.illum, 2)
        self.assertEqual(mat.Ka, (0.0, 0.0, 0.0))
        self.assertEqual(mat.Kd, (0.588, 0.588, 0.588))
        self.assertEqual(mat.Ks, (0.0, 0.0, 0.0))
        self.assertEqual(mat.Ke, (0.0, 0.0, 0.0))
        self.assertEqual(mat.map_Ka, 'cube.png')
        self.assertEqual(mat.map_Kd, 'cube.png')

    @staticmethod
    def object_name():
        return 'cube'


if __name__ == '__main__':
    unittest.main()
