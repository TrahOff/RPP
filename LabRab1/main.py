import random


# ручной ввод массивов
def handle_input():
    a = list(map(int, input("введите массив а: ").split()))
    b = list(map(int, input("введите массив б: ").split()))

    return a, b


# случайная генерация массивов
def random_input():
    a, b = [], []

    n = random.randint(10, 20)
    for i in range(n):
        a.append(random.randint(0, 10))

    n = random.randint(5, 10)
    for i in range(n):
        b.append(random.randint(0, 10))

    return a, b


# функция удаления элементов из массива А, прошедших по условию
def delete_elem(a, start, end):
    while end >= start:
        if a[end] % 2 == 0:
            a.pop(end)
        end -= 1
    return a, start


# функция проверки вхождения чётного элемента из массива А в массив Б
def check(a, b, start, end):
    for j in a[start:end]:
        if j in b and j % 2 == 0:
            return True
    return False


# функция обновления массива а
def update(a, b):
    start, i = -1, 0

    # цикл проверки элементов массива и удаления цепочек чётных элементов при выполнении условия
    while i < len(a):
        # условие задания начала цепочки чётных элементов
        if a[i] % 2 == 0 and start == -1:
            start = i

        # условие определения конца цепочки чётных элементов и проверки на условие задания
        if i + 1 < len(a) and a[i + 1] % 2 != 0 and start != -1:
            if check(a, b, start, i + 1):
                a, i = delete_elem(a, start, i + 1)
            start = -1

        # условие проверки конца списка на наличие чётных элементов
        if i + 1 == len(a):
            if a[i] % 2 == 0:
                if check(a, b, i, (i + 1)):
                    a, i = delete_elem(a, i, i)

        i += 1

    return a


# основная функция
def main():
    a, b = [], []

    while True:
        print("выберете способ ввода массива:\n"
              "1 - ввод вручную\n"
              "2 - автоматическое создание\n"
              "0 - выход из программы")
        input_type = input()
        if input_type.isdigit():
            input_type = int(input_type)
            if input_type == 1:
                a, b = handle_input()
            if input_type == 2:
                a, b = random_input()
            if input_type == 0:
                exit(0)
            if input_type > 2 or input_type < 0:
                print(f"Ошибка: введена неверная команда. ожидалось число (0-2). Вы ввели {input_type}")
            else:
                print(f"массив А[{len(a)}]: ")
                for el in a:
                    print(el, end=' ')
                print()
                print(f"массив B[{len(b)}]: ")
                for el in b:
                    print(el, end=' ')
                print()
                a = update(a, b)
                print(f"массив а[{len(a)}] после изменений:")
                for el in a:
                    print(el, end=' ')
                print()
        else:
            print(f"Ошибка: введена неверная команда. ожидалось число (0-2). Вы ввели {input_type}")


if __name__ == "__main__":
    main()
