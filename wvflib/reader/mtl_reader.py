from wvflib.material import MaterialLib, Material
from wvflib.reader.base_reader import BaseReader


class MtlReader(BaseReader):
    def __init__(self):
        super(MtlReader, self).__init__()
        self.__mat_lib = None
        self.__mat = None

    def _parse_material(self):
        self.__ensure_mat_pushed()
        self.__mat = Material()
        self.__mat.name = self.params[0]

    def _parse_int(self):
        attr = self.token_info[0]
        self.__mat._attributes[attr] = int(self.params[0])

    def _parse_float(self):
        attr = self.token_info[0]
        self.__mat._attributes[attr] = float(self.params[0])

    def _parse_trio_float(self):
        attr = self.token_info[0]
        self.__mat._attributes[attr] = (float(self.params[0]),
                                        float(self.params[1]),
                                        float(self.params[2]))

    def _parse_str(self):
        attr = self.token_info[0]
        self.__mat._attributes[attr] = str(self.params[0])

    def before_read(self, file_name):
        self.__mat_lib = MaterialLib()
        self.__mat_lib.name = file_name

    def after_read(self):
        self.__ensure_mat_pushed()
        return self.__mat_lib

    @staticmethod
    def parsers():
        return {'newmtl': '_parse_material',
                'Ns': '_parse_float',
                'Ni': '_parse_float',
                'd': '_parse_float',
                'Tr': '_parse_float',
                'Tf': '_parse_trio_float',
                'illum': '_parse_int',
                'Ka': '_parse_trio_float',
                'Kd': '_parse_trio_float',
                'Ks': '_parse_trio_float',
                'Ke': '_parse_trio_float',
                'map_Ka': '_parse_str',
                'map_Kd': '_parse_str'}

    def __ensure_mat_pushed(self):
        if self.__mat is None:
            return
        self.__mat.material_lib = self.__mat_lib
        self.__mat_lib.materials[self.__mat.name] = self.__mat
        self.__mat = None
