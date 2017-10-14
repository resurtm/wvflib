import os
import re

from wvflib.base import File, Object


class ObjReader(object):
    __filter_replacements = {(r'\s+', ' '),
                             (r'^\s+', ''),
                             (r'\s+$', '')}

    __token_parsers = {'o': '_parse_object',
                       'mtllib': '_parse_material_lib',
                       'v': '_parse_vertex',
                       'vt': '_parse_tex_coord',
                       'vn': '_parse_normal',
                       'g': '_parse_group',
                       'usemtl': '_parse_parse_material',
                       's': '_parse_smooth_group',
                       'f': '_parse_face'}

    def __init__(self):
        self.__line = None
        self.__params = []
        self.__file = None
        self.__object = None

    def read(self, file_name):
        self.__file = File()
        self.__file.name = os.path.basename(file_name)
        with open(file_name) as fp:
            for self.__line in fp:
                if self.__filter_line():
                    self.__parse_line()

        self.__file.objects.append(self.__object)
        self.__object = None

        return self.__file

    def _parse_object(self):
        self.__object = Object()
        self.__object.name = self.__params[0]

    def _parse_material_lib(self):
        pass

    def _parse_vertex(self):
        pass

    def _parse_tex_coord(self):
        pass

    def _parse_normal(self):
        pass

    def _parse_group(self):
        pass

    def _parse_parse_material(self):
        pass

    def _parse_smooth_group(self):
        pass

    def _parse_face(self):
        pass

    def __parse_line(self):
        tokens = self.__line.split(' ')
        self.__params = tokens[1:]
        parser = self.__token_parsers.get(tokens[:1][0], None)
        if parser is not None:
            getattr(self, parser)()

    def __filter_line(self):
        for k, v in self.__filter_replacements:
            self.__line = re.sub(k, v, self.__line)
        if self.__line[:1] == '#' or self.__line == '':
            self.__line = None
        return self.__line is not None
