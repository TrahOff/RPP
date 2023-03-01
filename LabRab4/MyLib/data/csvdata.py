from tabulate import tabulate
import pandas as pd
from MyLib import errors


class CSVData:
    def __init__(self):
        self._data, self._keys = [], []

    def print_data(self):
        print(tabulate(pd.DataFrame(self._data), headers=self._keys, tablefmt='grid', showindex=False))

    @staticmethod
    def write_data():
        data, keys = [], []
        flag = True
        print("Ведите ключи и данные для таблицы.\n"
              "Конец ввода обозначается командой EOI.\n"
              "Отмена ввода обозначается COI")
        keys = input("введите ключи для таблицы (названия столбцов)").split()
        print("введите данные в соответствии с введёнными ключами")

        while flag:
            row = input().split()
            if len(row) == 1:
                if row[0] == "EOI":
                    flag = False
                    break
                elif row[0] == "COI":
                    return
                else:
                    errors.Errors.key_mismatch_error()
            if len(row) == len(keys):
                dictionary = {}
                count = 0
                for key in keys:
                    dictionary[key] = row[count]
                    count += 1
                data.append(dictionary)
            else:
                errors.Errors.key_mismatch_error()

        return data, keys

    def delete_data(self):
        flag = True

        while flag:
            data_volume = input("какой объём данных вы хотите удалить (row or rows or all): ")

            if data_volume == "all":
                self.clear_data()
                flag = False

            elif data_volume == "row":
                row = input("введите номер строки, которую хотите удалить: ")

                if row.isdigit():
                    row = int(row)

                    if 0 < row < len(self._data):
                        self._data.pop(row - 1)
                        flag = False

                    else:
                        errors.Errors.wrong_input_error()

                else:
                    errors.Errors.wrong_input_error()

            elif data_volume == "rows":
                now = True

                while now:
                    rows = input("введите номера строк, которые хотите удалить: ").split()
                    if all(row.isdigit() for row in rows):
                        check = True

                        for row in rows:
                            row = int(row)

                            if row <= 0 or row >= len(self._data):
                                check = False

                        if check:
                            rows.reverse()
                            for index in rows:
                                index = int(index)
                                self._data.pop(index - 1)
                            now = False
                            flag = False

                        else:
                            errors.Errors.wrong_input_error()
                    else:
                        errors.Errors.wrong_input_error()
            else:
                errors.Errors.data_volume_error()

    def add_data(self):
        print("ведите строку в соответствии с ключами")
        for key in self._keys:
            print(key, end=" ")
        print()

        input_row = input().split()

        if len(input_row) == len(self._keys):
            new_row = {}
            for i in range(len(self._keys)):
                new_row[self._keys[i]] = input_row[i]
            self._data.append(new_row)
        else:
            errors.Errors.key_mismatch_error()

    def set_data(self, data, keys):
        self._data = data
        self._keys = keys

    def get_data(self):
        return self._data, self._keys

    def clear_data(self):
        self._data, self._keys = [], []

    def data_is_exist(self):
        if len(self._data) != 0 and len(self._keys) != 0:
            return True
        return False
