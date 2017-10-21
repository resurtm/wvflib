from wvflib.reader import ObjReader

version = '0.0.2'


def read_obj_file(file_name):
    obj_reader = ObjReader()
    return obj_reader.read(file_name)
