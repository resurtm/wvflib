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

    def test_vertices(self):
        self.assertEqual(len(self.f.objects[0].vertices), 8)
        self.assertEqual(self.f.objects[0].vertices[0].values,
                         (-0.5, -0.5, 0.5, 1.0))
        self.assertEqual(self.f.objects[0].vertices[7].values,
                         (0.5, -0.5, -0.5, 1.0))

    def test_tex_coords(self):
        self.assertEqual(len(self.f.objects[0].tex_coords), 4)
        self.assertEqual(self.f.objects[0].tex_coords[0].values, (0.0, 0.0))
        self.assertEqual(self.f.objects[0].tex_coords[3].values, (1.0, 1.0))

    def test_normals(self):
        self.assertEqual(len(self.f.objects[0].normals), 6)
        self.assertEqual(self.f.objects[0].normals[0].values,
                         (0.0, 0.0, 1.0, 1.0))
        self.assertEqual(self.f.objects[0].normals[5].values,
                         (-1.0, 0.0, 0.0, 1.0))

    def test_groups(self):
        self.assertEqual(len(self.f.objects[0].groups), 1)
        self.assertEqual(self.f.objects[0].groups[0].name, 'cube')

    def test_faces(self):
        self.assertEqual(len(self.f.objects[0].groups[0].faces), 12)
        self.assertEqual(self.f.objects[0].groups[0].faces[0],
                         ((1, 1, 1), (2, 2, 1), (3, 3, 1)))
        self.assertEqual(self.f.objects[0].groups[0].faces[11],
                         ((5, 3, 6), (1, 2, 6), (3, 4, 6)))

    @staticmethod
    def object_name():
        return 'cube'


if __name__ == '__main__':
    unittest.main()
