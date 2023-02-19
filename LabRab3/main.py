import csv
import datetime
import operator
import os

import pandas as pd
from tabulate import tabulate


def create_directory(path):
    os.mkdir(path)
    print("!папка создана!")


def set_directory():
    path = input("Введите название папки: ")
    if os.path.exists(path):
        text = "!папка найдена!"
        print("\033[31m{}\033[0m".format(text))
        return path
    else:
        print("Ошибка: такой папки не существует.\n"
              "1 - попробовать ещё раз\n"
              "2 - создать папку\n"
              "0 - выход")
        operation = input("введите команду: ")
        if operation.isdigit():
            operation = int(operation)
            if operation == 1:
                set_directory()
            if operation == 2:
                create_directory(path)
                return path
            if operation == 0:
                return


def set_file(path):
    file_name = input("Введите название файла: ")
    file = f"{path}/{file_name}"
    if os.path.exists(file):
        text = "!файл найден!"
        print("\033[31m{}\033[0m".format(text))
        return file
    else:
        print("Ошибка: такой файл не существует.\n"
              "1 - попробовать ещё раз\n"
              "2 - создать файл\n"
              "0 - выход")
        operation = input("введите команду: ")
        if operation.isdigit():
            operation = int(operation)
            if operation == 1:
                set_file(path)
            if operation == 2:
                create_file(file)
                return file
            if operation == 0:
                return


def create_file(file):
    open(file, "w+")
    print("!файл создан!")


def print_information(arr):
    print(f"всего файлов в папке: {len(arr)}")
    s = " "
    k = 1
    for i in arr:
        print(f"{s:>5}{k}: {i}")
        k += 1


def show_files(path):
    flag = True
    while flag:
        if os.path.exists(path):
            print_information(os.listdir(path))
            return
        else:
            print("Ошибка: папки по этому пути не существует.\n"
                  "попробовать ещё раз - 1\n"
                  "выход - 0\n")
            operation = input("введите команду: ")
            if operation.isdigit():
                operation = int(operation)
                if operation == 0:
                    flag = False
                if operation > 1:
                    print("Ожидалось число (1, 0)\n"
                          f"вы ввели: {operation}")
            else:
                print("Ожидалось число (1, 0)\n"
                      f"вы ввели: {operation}")


def get_data(file):
    data, keys = [], []
    with open(file, "r") as file:
        reader = csv.DictReader(file)
        keys = reader.fieldnames
        for row in reader:
            data.append(row)
        file.close()

    return data, keys


def update_data(data, keys):
    n = int(input("сколько данных вы хотите записать: "))

    if n == 1:
        print(f"введите {n} строку данных в формате: номер и марка автомобиля\n"
              f"(номер проезда, дата и время заполнятся автоматически)")
    if 1 < n < 5:
        print(f"введите {n} строки данных в формате: номер и марка автомобиля\n"
              f"(номер проезда, дата и время заполнятся автоматически)")
    if n >= 5:
        print(f"введите {n} строк данных в формате: номер и марка автомобиля\n"
              f"(номер проезда, дата и время заполнятся автоматически)")

    for i in range(len(data), len(data) + n):
        row = input().split()
        new_row = {
            keys[0]: str(len(data) + 1),
            keys[1]: str(datetime.datetime.now()),
            keys[2]: row[0],
            keys[3]: row[1],
        }
        data.append(new_row)


def write_data_to_file(data, keys, file):
    data.sort(key=operator.itemgetter(keys[0]))
    with open(file, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
        file.close()


def print_data(data, keys, file):
    flag = True
    while flag:
        if len(data) != 0:
            print(tabulate(pd.DataFrame(data), headers=keys, tablefmt='grid', showindex=False))
            flag = False
        else:
            print("В файле нет данных. хотите внести первые данные?\n"
                  "1 - внести данные\n"
                  "2 - пропустить")
            operation = input("введите команду: ")
            if operation.isdigit():
                operation = int(operation)
                keys = ['№', 'дата_и_время', 'номерной_знак', 'марка_автомобиля']
                if operation == 1:
                    update_data(data, keys)
                    write_data_to_file(data, keys, file)
                if operation == 0:
                    update_data(data, keys)
                    write_data_to_file(data, keys, file)
                if operation > 1:
                    print("Ожидалось число (1, 0)\n"
                          f"вы ввели: {operation}")
            else:
                print("Ожидалось число (1, 0)\n"
                      f"вы ввели: {operation}")


def sort(data, keys):
    while True:
        sort_type = input("выберете способ сортировки: \n"
                          "1 - по id поездки\n"
                          "2 - по времени проезда\n"
                          "3 - по номеру автомобиля\n"
                          "4 - по марке автомобиля\n"
                          "0 - отмена\n")
        if sort_type.isdigit():
            sort_type = int(sort_type)
            if sort_type == 1:
                text = "сортировка по номеру проезда"
                print("\033[31m{}\033[0m".format(text))
                return data.sort(key=operator.itemgetter(keys[0]))
            if sort_type == 2:
                text = "сортировка по времени проезда"
                print("\033[31m{}\033[0m".format(text))
                return data.sort(key=operator.itemgetter(keys[1]))
            if sort_type == 3:
                text = "сортировка номеру автомобиля"
                print("\033[31m{}\033[0m".format(text))
                return data.sort(key=operator.itemgetter(keys[2]))
            if sort_type == 4:
                text = "сортировка по марке автомобиля"
                print("\033[31m{}\033[0m".format(text))
                return data.sort(key=operator.itemgetter(keys[3]))
            if sort_type == 0:
                return data
            if sort_type > 4:
                print(f"Ошибка: неверная команда. Вы ввели {sort_type}. Ожидалось число(0-2)")
        else:
            print(f"Ошибка: неверная команда. Вы ввели {sort_type}. Ожидалось число(0-2)")


def main():
    path, file = '', ''
    flag = True
    data, keys = [], []

    while flag:
        operation = input("Выберете операцию:\n"
                          "1 - просмотр файлов\n"
                          "2 - вывод таблицы данных\n"
                          "3 - запись новых данных\n"
                          "4 - отсортировать данные\n"
                          "0 - выход\n")
        if operation.isdigit():
            operation = int(operation)
            match operation:
                case 1:
                    path = set_directory()
                    show_files(path)
                case 2:
                    now = True
                    while now:
                        if path == '':
                            path = set_directory()
                        else:
                            if file == '':
                                file = set_file(path)
                            else:
                                if len(data) == 0:
                                    data, keys = get_data(file)
                                else:
                                    print_data(data, keys, file)
                                    now = False

                case 3:
                    update_data(data, keys)
                    write_data_to_file(data, keys, file)
                case 4:
                    if len(data) > 0:
                        sort(data, keys)
                    else:
                        print("Ошибка: вы не выбрали папку и файл")
                case 0:
                    flag = False
        else:
            print(f"Ошибка: неверная команда. Вы ввели {operation}. Ожидалось число(0-4)")


if __name__ == "__main__":
    main()
