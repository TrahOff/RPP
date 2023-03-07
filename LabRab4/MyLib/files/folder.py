import os
from MyLib import errors


class Folder:
    _folder = "disc"
    _disk = "disc"
    _prev_folder = ""
    _elements = [_folder]

    def open_folder(self, folder_name):
        tmp_folder = self._folder + f"/{folder_name}"
        if os.path.exists(tmp_folder):
            self._prev_folder = self._folder
            self._folder += f"/{folder_name}"
            self._elements.append(folder_name)
        else:
            errors.Errors.folder_error()

    def close_folder(self):
        if self._folder != self._disk:
            self._folder = self._prev_folder
            self._elements.pop(len(self._elements) - 1)
            self._prev_folder = self._disk
            for element in self._elements:
                self._prev_folder += f"{element}"
        else:
            errors.Errors.disc_close_error()

    def create_folder(self, folder_name):
        new_folder = self._folder + f"/{folder_name}"
        os.mkdir(new_folder)

    def delete_folder(self, folder_name):
        deleting_folder = self._folder + f"/{folder_name}"
        os.rmdir(deleting_folder)

    def get_path(self):
        return self._folder

    def get_elements(self):
        return os.listdir(self._folder)
