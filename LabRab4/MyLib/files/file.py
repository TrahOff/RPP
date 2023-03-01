import MyLib.errors
import constants
import os


class File:
    def __init__(self):
        self._name = ""
        self._file_path = ""
        self._expansions = [".txt", ".csv"]
        self._exist = False
        self._isOpen = False

    def create_file(self, path, file_name):
        if self.right_expansion(file_name):
            self._file_path = f"{path}/{file_name}"
            f = open(self._file_path, 'w+')
            f.close()

    def delete_file(self, file_name):
        self._file_path = constants.Const.fold.get_path() + f"/{file_name}"
        if os.path.exists(self._file_path):
            os.remove(self._file_path)
        else:
            MyLib.errors.Errors.existing_file_error()

    def right_expansion(self, file_name):
        for expansion in self._expansions:
            if expansion in file_name:
                return True
        return False

    def get_expansion(self, file_name):
        for expansion in self._expansions:
            if expansion in file_name:
                return expansion

    def get_path(self):
        return self._file_path

    def get_name(self):
        return self._name

    def is_exist(self, path, file_name):
        if os.path.exists(path + f"/{file_name}"):
            self._exist = True
            self._file_path = path + f"/{file_name}"
            self._name = file_name
            return True
        return False

    def open_file(self):
        self._isOpen = True

    def is_open(self):
        return self._isOpen

    def close_file(self):
        self._name = ""
        self._file_path = ""
        self._expansions = []
        self._exist = False
        self._isOpen = False
