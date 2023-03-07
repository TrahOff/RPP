import constants
from MyLib.files import file
import csv


class CSVFile(file.File):
    _data, _keys = [], []

    def get_data(self):
        self._data, keys = [], []
        with open(self.get_path(), "r", encoding="cp1251") as f:
            reader = csv.DictReader(f)
            self._keys = reader.fieldnames
            for row in reader:
                self._data.append(row)
            constants.Const.csvData.set_data(self._data, self._keys)
            f.close()

    def set_data(self, data, keys):
        with open(self.get_path(), "w", encoding="cp1251", newline="\n") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
            f.close()
