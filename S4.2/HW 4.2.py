"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. 
n — кол-во элементов первого множества.
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""

n = int(input('Ведите кол-во элементов первого массива: '))
m = int(input('Ведите кол-во элементов второго массива: '))

array = []

for i in range(n):
    array.append(int(input("Введите элемент первого массива: ")))
for i in range(m):
    array.append(int(input("Введите элемент второго массива: ")))

print(set(sorted(array)))


"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
"""

import random

n = random.randint(3, 10)       # создаём грядку с рандомным количеством кустов от 3 до 10

garden_bed = [random.randrange(1, 50) for i in range(n)]        # заполняем рандомно кусты ягодами


def make_kust_array(array: list) -> list:
    """создаёт масив из рядом стоящих кустов"""
    three_bushes = []
    for i in range(len(array)):
        if i != len(array)-1:
            three_bushes.append([array[i-1], array[i], array[i+1]])
        else:
            three_bushes.append([array[i-1], array[i], array[0]])
    return three_bushes

def find_max_kust (func) -> int: 
    """Находим максимальное количество ягод, которое можно собрать с 3 кустов"""
    sort_kust = []
    for k in func:
        sort_kust.append(sum(k))
    return max(sort_kust)

print(f"""
      В этом сезоне урадилось {n} кустов черники.
      Количество ягод по кустам {garden_bed}.
      Максимально с 3-х рядомстоящих кустов, можно собрать {find_max_kust(make_kust_array(garden_bed))} ягод.""")
