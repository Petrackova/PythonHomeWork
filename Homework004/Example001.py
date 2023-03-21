"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""
import random

list_1 = list()
n = int(input('Введите число элементов в списке: '))
n = range(n)
for i in n: 
    i = random.randint(-5,20)
    list_1.append(i)
my_set = set(list_1)
print(my_set)
list_2 = list()
n = int(input('Введите число элементов в списке: '))
n = range(n)
for i in n: 
    i = random.randint(-5,20)
    list_2.append(i)
my_set1 = set(list_2)
print(my_set1)
i = my_set.intersection(my_set1) 
i = sorted(i)
print(i)