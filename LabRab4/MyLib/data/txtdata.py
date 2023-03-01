import constants


class TXTData:
    def __init__(self):
        self._data = []

    def get_data(self):
        return self._data

    def print_data(self):
        s = ""
        print(f"{s:>10}{constants.Const.textfile.get_name()}")
        for row in self._data:
            print(f"{s:>5}{row}", end='')
        print()

    @staticmethod
    def write_data():
        data = []
        flag = True
        print("Ведите текст. Конец ввода обозначается командой EOI. Отмена ввода обозначается COI")
        while flag:
            text = input()
            if text == "EOI":
                flag = False
            elif text == "COI":
                return
            else:
                data.append(text)
        return data

    def set_data(self, arr):
        self._data = arr

    def clear_data(self):
        self._data = []

    def data_is_exist(self):
        if len(self._data) != 0:
            return True
        return False
