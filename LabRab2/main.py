import random
import numpy as np


# задание случайных элементов матрицы
def random_mas(n, m):
    return np.random.randint(1, 10, size=(n, m))


# задание случайной величины матрицы
def random_matrix_size():
    return random.randint(3, 6), random.randint(3, 6)


# функция подсчёта сумм элементов каждого столбца и нахождение
# #их доли относительно общей суммы всех элементов матрицы
def colum_sum(mas, summa):
    cs = [0] * len(mas[0])
    k = 0
    for i in range(len(mas)):
        for x in mas[i]:
            cs[k] += x
            if i == len(mas) - 1:
                cs[k] /= summa
            k += 1
        k = 0
    return cs


# функция записи полученных данных в файл output.txt
def save_to_file(arr, n, m):
    file = open("output2.txt", 'w')

    try:
        file.write(f"Общая сумма: {(str(arr.sum()))}\n"
                   f"Полученные данные:\n"
                   f"Размерность массива: {str(n)} x {str(m)}\n"
                   f"Сам массив: \n"
                   "(в последней строке хранится доля суммы элементов столбца\n "
                   "относительно суммы всех элементов матрицы)\n")

        np.savetxt(file, arr, fmt='%.2f')
    finally:
        file.close()


def main():
    n, m = random_matrix_size()
    arr = random_mas(n, m)
    # добавление строчки с отношением суммы столбца к общей сумме всех элементов матрицы
    arr = np.vstack([arr, colum_sum(arr, arr.sum())])
    save_to_file(arr, n, m)


if __name__ == "__main__":
    main()
