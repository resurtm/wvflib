class Material:
    attributes = ('Ns',
                  'Ni',
                  'd',
                  'Tr',
                  'Tf',
                  'illum',
                  'Ka',
                  'Kd',
                  'Ks',
                  'Ke',
                  'map_Ka',
                  'map_Kd')

    def __init__(self):
        self.name = ''
        self.material_lib = None
        self._attributes = {}

    def __getattr__(self, item):
        if item in Material.attributes and item in self._attributes:
            return self._attributes[item]
        else:
            raise AttributeError("There is no '{}' attribute".format(item))


class MaterialLib(object):
    def __init__(self):
        self.name = ''
        self.materials = {}
