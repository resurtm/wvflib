class Object:
    def __init__(self):
        self.name = ''
        self.material_lib = None
        self.groups = []

        self.vertices = []
        self.tex_coords = []
        self.normals = []

    @property
    def empty(self) -> bool:
        return len(self.vertices) == 0


class File:
    def __init__(self):
        self.name = None
        self.objects = []
        self.material_libs = {}
