import os

from wvflib.base import File, Object
from wvflib.geometry import Vector, TexCoord
from wvflib.groups import Group, SmoothGroup
from wvflib.reader.base_reader import BaseReader
from wvflib.reader.mtl_reader import MtlReader


class ObjReader(BaseReader):
    def __init__(self):
        super(ObjReader, self).__init__()
        self.__file = None
        self.__object = None
        self.__group = None
        self.__smooth_group = None

    def _parse_object(self):
        self.__ensure_object_pushed()
        self.__object = Object()
        self.__object.name = self.params[0]

    def _parse_material_lib(self):
        mtl_reader = MtlReader()
        path = os.path.join(os.path.dirname(self.file_path), self.params[0])
        material_lib = mtl_reader.read(path)
        self.__file.material_libs[material_lib.name] = material_lib
        self._obj.material_lib = material_lib

    def _parse_vertex(self):
        self._obj.vertices.append(self.__parse_vector())

    def _parse_tex_coord(self):
        uv = TexCoord()
        uv.u = float(self.params[0])
        uv.v = float(self.params[1])
        self._obj.tex_coords.append(uv)

    def _parse_normal(self):
        self._obj.normals.append(self.__parse_vector())

    def _parse_group(self):
        self.__ensure_group_pushed()
        self._grp.name = self.params[0]

    def _parse_parse_material(self):
        for k, v in self._obj.material_lib.materials.items():
            if k == self.params[0]:
                self._grp.material = v
                break

    def _parse_smooth_group(self):
        self.__ensure_smooth_group_pushed()
        self._sgr.name = self.params[0]

    def _parse_face(self):
        vertices = []
        for vtx in self.params:
            vtx_parts = vtx.split('/')
            vertex = [int(vtx_parts[0])]  # vertex position index
            if len(vtx_parts) > 1 and len(vtx_parts[1]) > 0:
                vertex.append(int(vtx_parts[1]))  # vertex tex coord index
            if len(vtx_parts) > 2 and len(vtx_parts[2]) > 0:
                vertex.append(int(vtx_parts[2]))  # vertex normal index
            vertices.append(tuple(vertex))
        vertices = tuple(vertices)
        self._grp.faces.append(vertices)
        self._sgr.faces.append(vertices)

    def __parse_vector(self):
        vec = Vector()
        vec.x = float(self.params[0])
        vec.y = float(self.params[1])
        vec.z = float(self.params[2])
        if len(self.params) == 4:
            vec.w = float(self.params[3])
        return vec

    def before_read(self, file_name):
        self.__file = File()
        self.__file.name = file_name

    def after_read(self):
        self.__ensure_group_pushed()
        self.__ensure_object_pushed()
        return self.__file

    @property
    def _obj(self):
        if self.__object is None:
            self.__object = Object()
        return self.__object

    @property
    def _grp(self):
        if self.__group is None:
            self.__group = Group()
        return self.__group

    @property
    def _sgr(self):
        if self.__smooth_group is None:
            self.__smooth_group = SmoothGroup()
        return self.__smooth_group

    @staticmethod
    def parsers():
        return {'o': '_parse_object',
                'mtllib': '_parse_material_lib',
                'v': '_parse_vertex',
                'vt': '_parse_tex_coord',
                'vn': '_parse_normal',
                'g': '_parse_group',
                'usemtl': '_parse_parse_material',
                's': '_parse_smooth_group',
                'f': '_parse_face'}

    def __ensure_object_pushed(self):
        if self.__object is None:
            return
        self.__file.objects.append(self.__object)
        self.__object = None

    def __ensure_group_pushed(self):
        if self.__group is None:
            return
        self.__object.groups.append(self.__group)
        self.__group = None

    def __ensure_smooth_group_pushed(self):
        if self.__smooth_group is None:
            return
        self.__group.smooth_groups.append(self.__smooth_group)
        self.__smooth_group = None
