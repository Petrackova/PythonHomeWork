# Часть 1
"""Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai . Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""
# Часть 2
"""Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai . Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
"""
import random
#Часть 1
list_1 = list()
n = int(input('Введите число элементов в списке: '))
k = int(input('Введите число для подсчета повторений: '))     
n = range(n)
for i in n: 
    i = random.randint(0,20)
    list_1.append(i)
print(list_1)
print(f'Число содержиться в массиве: {list_1.count(k)} раз')
# Часть 2
m = int(input('Введите число: ')) 
found = list_1[0]
for i in list_1:
    if abs(i - m) < abs(found - m):
        found = i
print(f'Ближайшее число к {m} в списке является: {found}')