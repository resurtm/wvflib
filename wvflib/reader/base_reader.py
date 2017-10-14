import os
import re


class BaseReader(object):
    __filter_replacements = {(r'\s+', ' '),
                             (r'^\s+', ''),
                             (r'\s+$', '')}

    def __init__(self):
        super(BaseReader, self).__init__()
        self.__file_path = None
        self.__line = None
        self.__params = []
        self.__parsed_token = None
        self.__token_parser = None

    def before_read(self, file_name):
        raise NotImplementedError

    def after_read(self):
        raise NotImplementedError

    @staticmethod
    def parsers():
        raise NotImplementedError

    def read(self, file_name):
        self.__file_path = file_name
        self.before_read(os.path.basename(self.__file_path))
        with open(self.__file_path) as fp:
            for self.__line in fp:
                if self.__filter_line():
                    self.__parse_line()
        return self.after_read()

    @property
    def file_path(self):
        return self.__file_path

    @property
    def params(self):
        return self.__params

    @property
    def token_info(self):
        return self.__parsed_token, self.__token_parser

    def __parse_line(self):
        tokens = self.__line.split(' ')
        self.__params = tokens[1:]
        self.__parsed_token = tokens[:1][0]
        self.__token_parser = self.parsers().get(self.__parsed_token, None)
        if self.__token_parser is not None:
            getattr(self, self.__token_parser)()

    def __filter_line(self):
        for k, v in self.__filter_replacements:
            self.__line = re.sub(k, v, self.__line)
        if self.__line[:1] == '#' or self.__line == '':
            self.__line = None
        return self.__line is not None
