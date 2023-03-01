class Errors:
    @staticmethod
    def command_error():
        print("\033[31m{}\033[0m".format("Ошибка: неверный ввод команды!"))

    @staticmethod
    def folder_error():
        print("\033[31m{}\033[0m".format("Ошибка: неверный ввод названия папки!"))

    @staticmethod
    def object_error():
        print("\033[31m{}\033[0m".format("Ошибка: указано неверное название объекта!"))

    @staticmethod
    def deleting_folder_error():
        print("\033[31m{}\033[0m".format("Ошибка: перед удалением папки, нужно закрыть её!"))

    @staticmethod
    def deleting_file_error():
        print("\033[31m{}\033[0m".format("Ошибка: перед удалением файла, нужно закрыть его!"))

    @staticmethod
    def existing_file_error():
        print("\033[31m{}\033[0m".format("Ошибка: файла с таким названием не существует в данной папке!"))

    @staticmethod
    def disc_close_error():
        print("\033[31m{}\033[0m".format("Ошибка: невозможно закрыть корневую папку!"))

    @staticmethod
    def expansion_error():
        print("\033[31m{}\033[0m".format("Ошибка: неверно указано расширение файла! "
                                         "программа работает с csv и txt файлами"))

    @staticmethod
    def file_not_open_error():
        print("\033[31m{}\033[0m".format(f"Ошибка: файл не был открыт!"))

    @staticmethod
    def print_data_error():
        print("\033[31m{}\033[0m".format(f"Ошибка: сначала нужно открыть файл!"))

    @staticmethod
    def data_is_not_exist_error():
        print("\033[31m{}\033[0m".format(f"Ошибка: файл пуст!"))

    @staticmethod
    def key_mismatch_error():
        print("\033[31m{}\033[0m".format(f"Ошибка: данные не соответствуют ключам!"))

    @staticmethod
    def file_is_not_open_error():
        print("\033[31m{}\033[0m".format(f"Ошибка: файл не открыт для записи данных!"))

    @staticmethod
    def wrong_input_error():
        print("\033[31m{}\033[0m".format(f"Ошибка: неверный ввод!"))

    @staticmethod
    def data_volume_error():
        print("\033[31m{}\033[0m".format(f"Ошибка: неверно указан объём удаляемых данных!"))

    @staticmethod
    def add_data_to_txt_error():
        print("\033[31m{}\033[0m".format(f"Ошибка: текстовые файлы можно только перезаписать!"))
