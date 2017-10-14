import os

from wvflib.base import File, Object
from wvflib.geometry import Vector, TexCoord
from wvflib.reader.base_reader import BaseReader
from wvflib.reader.mtl_reader import MtlReader


class ObjReader(BaseReader):
    def __init__(self):
        super(ObjReader, self).__init__()
        self.__file = None
        self.__object = None

    def _parse_object(self):
        self.__ensure_object_pushed()
        self.__object = Object()
        self.__object.name = self.params[0]

    def _parse_material_lib(self):
        mtl_reader = MtlReader()
        path = os.path.join(os.path.dirname(self.file_path), self.params[0])
        material_lib = mtl_reader.read(path)
        self.__file.material_libs[material_lib.name] = material_lib
        self.obj.material_lib = material_lib

    def _parse_vertex(self):
        self.obj.vertices.append(self.__parse_vector())

    def _parse_tex_coord(self):
        uv = TexCoord()
        uv.u = float(self.params[0])
        uv.v = float(self.params[1])
        return uv

    def _parse_normal(self):
        self.obj.normals.append(self.__parse_vector())

    def _parse_group(self):
        pass

    def _parse_parse_material(self):
        pass

    def _parse_smooth_group(self):
        pass

    def _parse_face(self):
        pass

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
        self.__ensure_object_pushed()
        return self.__file

    @property
    def obj(self):
        if self.__object is None:
            self.__object = Object()
        return self.__object

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
