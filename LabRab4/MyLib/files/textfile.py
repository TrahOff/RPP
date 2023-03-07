import constants
from MyLib.files import file


class TextFile(file.File):
    def get_data(self):
        arr = []
        with open(self.get_path(), "r", newline="\n") as f:
            reader = f.readlines()
            for row in reader:
                arr.append(row)
            constants.Const.txtData.set_data(arr)
            f.close()

    def set_data(self, data):
        with open(self.get_path(), "w") as f:
            f.writelines("%s\n" % row for row in data)
            f.close()
