import os
import unittest

from wvflib import read_obj_file


class TestCase(unittest.TestCase):
    __files = {}

    @property
    def f(self):
        name = self.object_name()
        if name not in self.__files:
            root = os.path.dirname(os.path.realpath(__file__))
            path = os.path.join(root, 'data', name, '{}.obj'.format(name))
            TestCase.__files[name] = read_obj_file(path)
        return TestCase.__files[name]

    @staticmethod
    def object_name():
        raise NotImplementedError
