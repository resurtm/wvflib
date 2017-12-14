import unittest

from tests.base import TestCase


class TestCube(TestCase):
    def test_common(self):
        # self.assertTrue(False)

        self.assertTrue(self.f.name == 'capsule.obj')
        self.assertTrue(len(self.f.objects) == 1)
        self.assertEqual(self.f.objects[0].name, '')

    def test_material_libs(self):
        libs = self.f.material_libs

        self.assertTrue(len(libs) == 1)
        self.assertEqual(libs['capsule.mtl'].name, 'capsule.mtl')
        self.assertTrue(len(libs['capsule.mtl'].materials) == 1)
        self.assertEqual(self.f.objects[0].material_lib, libs['capsule.mtl'])

    def test_materials(self):
        lib = self.f.material_libs['capsule.mtl']
        mat = lib.materials['material0']

        self.assertEqual(mat.name, 'material0')
        self.assertEqual(mat.material_lib, lib)

        self.assertEqual(mat.Ns, 0.0)
        self.assertFalse(hasattr(mat, 'Ni'))
        self.assertFalse(hasattr(mat, 'd'))
        self.assertEqual(mat.Tr, 1.0)
        self.assertFalse(hasattr(mat, 'Tf'))
        self.assertEqual(mat.illum, 1)
        self.assertEqual(mat.Ka, (1.0, 1.0, 1.0))
        self.assertEqual(mat.Kd, (1.0, 1.0, 1.0))
        self.assertEqual(mat.Ks, (0.0, 0.0, 0.0))
        self.assertFalse(hasattr(mat, 'Ke'))
        self.assertFalse(hasattr(mat, 'map_Ka'))
        self.assertEqual(mat.map_Kd, 'capsule0.jpg')

    def test_vertices(self):
        self.assertEqual(len(self.f.objects[0].vertices), 5252)

        self.assertEqual(self.f.objects[0].vertices[0].values,
                         (0.0, 0.0, -1.5, 1.0))
        self.assertEqual(self.f.objects[0].vertices[1].values,
                         (0.0, 0.0, -1.5, 1.0))
        self.assertEqual(self.f.objects[0].vertices[2].values,
                         (0.0, 0.0, -1.5, 1.0))

        self.assertEqual(self.f.objects[0].vertices[5249].values,
                         (0.0, 0.0, 1.5, 1.0))
        self.assertEqual(self.f.objects[0].vertices[5250].values,
                         (0.0, 0.0, 1.5, 1.0))
        self.assertEqual(self.f.objects[0].vertices[5251].values,
                         (0.0, 0.0, 1.5, 1.0))

    def test_tex_coords(self):
        self.assertEqual(len(self.f.objects[0].tex_coords), 5252)

        self.assertEqual(self.f.objects[0].tex_coords[0].values, (0.0, 0.0))
        self.assertEqual(self.f.objects[0].tex_coords[1].values, (0.01, 0.0))
        self.assertEqual(self.f.objects[0].tex_coords[2].values, (0.02, 0.0))

        self.assertEqual(self.f.objects[0].tex_coords[5249].values, (0.98, 1.0))
        self.assertEqual(self.f.objects[0].tex_coords[5250].values, (0.99, 1.0))
        self.assertEqual(self.f.objects[0].tex_coords[5251].values, (1.0, 1.0))

    def test_normals(self):
        self.assertEqual(len(self.f.objects[0].normals), 5252)

        self.assertEqual(self.f.objects[0].normals[0].values,
                         (0.0, 0.0, -1.0, 1.0))
        self.assertEqual(self.f.objects[0].normals[1].values,
                         (0.0, 0.0, -1.0, 1.0))
        self.assertEqual(self.f.objects[0].normals[2].values,
                         (0.0, 0.0, -1.0, 1.0))

        self.assertEqual(self.f.objects[0].normals[5249].values,
                         (0.0, 0.0, 1.0, 1.0))
        self.assertEqual(self.f.objects[0].normals[5250].values,
                         (0.0, 0.0, 1.0, 1.0))
        self.assertEqual(self.f.objects[0].normals[5251].values,
                         (0.0, 0.0, 1.0, 1.0))

    def test_groups(self):
        self.assertEqual(len(self.f.objects[0].groups), 1)
        self.assertEqual(self.f.objects[0].groups[0].name, '')

    def test_faces(self):
        self.assertEqual(len(self.f.objects[0].groups[0].faces), 10200)

        self.assertEqual(self.f.objects[0].groups[0].faces[0],
                         ((1, 1, 1), (2, 2, 2), (103, 103, 103)))
        self.assertEqual(self.f.objects[0].groups[0].faces[1],
                         ((1, 1, 1), (103, 103, 103), (102, 102, 102)))
        self.assertEqual(self.f.objects[0].groups[0].faces[2],
                         ((2, 2, 2), (3, 3, 3), (104, 104, 104)))

        self.assertEqual(self.f.objects[0].groups[0].faces[10197],
                         ((5149, 5149, 5149),
                          (5251, 5251, 5251),
                          (5250, 5250, 5250)))
        self.assertEqual(self.f.objects[0].groups[0].faces[10198],
                         ((5150, 5150, 5150),
                          (5151, 5151, 5151),
                          (5252, 5252, 5252)))
        self.assertEqual(self.f.objects[0].groups[0].faces[10199],
                         ((5150, 5150, 5150),
                          (5252, 5252, 5252),
                          (5251, 5251, 5251)))

    @staticmethod
    def object_name():
        return 'capsule'


if __name__ == '__main__':
    unittest.main()
