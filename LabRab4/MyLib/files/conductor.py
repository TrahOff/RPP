import constants
from MyLib import errors
from MyLib.files import file


class Conductor:
    @staticmethod
    def close_object(object_type, object_name):
        if object_type == "folder":
            if object_name in constants.Const.fold.get_path():
                constants.Const.fold.close_folder()
            else:
                errors.Errors.folder_error()
        elif object_type == "file":
            f = file.File()
            expansion = f.get_expansion(object_name)
            if expansion == ".txt":
                if constants.Const.textfile.is_open():
                    constants.Const.txtData.clear_data()
                    constants.Const.textfile.close_file()
                else:
                    errors.Errors.file_not_open_error()
            elif expansion == ".csv":
                if constants.Const.csvfile.is_open():
                    constants.Const.csvfile.close_file()
                    constants.Const.csvData.clear_data()
                else:
                    errors.Errors.file_not_open_error()
        else:
            errors.Errors.object_error()

    @staticmethod
    def delete_object(object_type, object_name):
        if object_type == "folder":
            if object_name not in constants.Const.fold.get_path():
                constants.Const.fold.delete_folder(object_name)
            else:
                errors.Errors.deleting_folder_error()
        elif object_type == "file":
            constants.Const.file.delete_file(object_name)
        else:
            errors.Errors.object_error()

    @staticmethod
    def create_object(object_type, object_name):
        if object_type == "folder":
            constants.Const.fold.create_folder(object_name)
        elif object_type == "file":
            constants.Const.file.create_file(constants.Const.fold.get_path(), object_name)
        else:
            errors.Errors.object_error()

    @staticmethod
    def open_object(object_type, object_name):
        if object_type == "folder":
            constants.Const.fold.open_folder(object_name)
        elif object_type == "file":
            f = file.File()
            expansion = f.get_expansion(object_name)
            if expansion == ".txt":
                if constants.Const.textfile.is_exist(
                    constants.Const.fold.get_path(), object_name
                ):
                    constants.Const.textfile.open_file()
                    constants.Const.textfile.get_data()
                else:
                    errors.Errors.existing_file_error()
            elif expansion == ".csv":
                if constants.Const.csvfile.is_exist(
                    constants.Const.fold.get_path(), object_name
                ):
                    constants.Const.csvfile.open_file()
                    constants.Const.csvfile.get_data()
                else:
                    errors.Errors.existing_file_error()
            else:
                errors.Errors.expansion_error()
        else:
            errors.Errors.object_error()

    @staticmethod
    def print_data():
        if constants.Const.textfile.is_open():
            if constants.Const.txtData.data_is_exist():
                constants.Const.txtData.print_data()
            else:
                errors.Errors.data_is_not_exist_error()
        elif constants.Const.csvfile.is_open():
            if constants.Const.csvData.data_is_exist():
                constants.Const.csvData.print_data()
            else:
                errors.Errors.data_is_not_exist_error()
        else:
            errors.Errors.print_data_error()

    @staticmethod
    def write_data():
        if constants.Const.textfile.is_open():
            data = constants.Const.txtData.write_data()
            constants.Const.textfile.set_data(data)
            constants.Const.textfile.get_data()
        elif constants.Const.csvfile.is_open():
            data, keys = constants.Const.csvData.write_data()
            constants.Const.csvfile.set_data(data, keys)
            constants.Const.csvfile.get_data()
        else:
            errors.Errors.file_is_not_open_error()

    @staticmethod
    def add_data():
        if constants.Const.textfile.is_open():
            errors.Errors.add_data_to_txt_error()
        elif constants.Const.csvfile.is_open():
            constants.Const.csvData.add_data()
            data, keys = constants.Const.csvData.get_data()
            constants.Const.csvfile.set_data(data, keys)
        else:
            errors.Errors.file_is_not_open_error()

    @staticmethod
    def delete_data():
        if constants.Const.textfile.is_open():
            if constants.Const.txtData.data_is_exist():
                constants.Const.txtData.clear_data()
                constants.Const.textfile.set_data(constants.Const.txtData.get_data())
            else:
                errors.Errors.data_is_not_exist_error()
        elif constants.Const.csvfile.is_open():
            if constants.Const.csvData.data_is_exist():
                constants.Const.csvData.delete_data()
                data, keys = constants.Const.csvData.get_data()
                constants.Const.csvfile.set_data(data, keys)
            else:
                errors.Errors.data_is_not_exist_error()
        else:
            errors.Errors.file_is_not_open_error()
