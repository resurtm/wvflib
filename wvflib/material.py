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


class MaterialLib(object):
    def __init__(self):
        self.name = ''
        self.materials = {}
