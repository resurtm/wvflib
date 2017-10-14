from wvflib.reader import ObjReader


def read_obj_file(file_name):
    obj_reader = ObjReader()
    return obj_reader.read(file_name)
