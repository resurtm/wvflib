import unittest

from wvflib.material import Material
from wvflib.reader.mtl_reader import MtlReader

class TestMaterial(unittest.TestCase):
    def test_material_attributes_equal_to_parsers(self):
        s1 = {v for v in Material.attributes}
        s2 = {k for k, _ in MtlReader.parsers(True).items()}
        self.assertEqual(s1, s2)


if __name__ == '__main__':
    unittest.main()
