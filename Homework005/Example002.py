'''Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
2 2
4
'''
import random

num = random.randint(0,10)
num1 = random.randint(0,10)
def summ(num,num1):
    if num == 0:
        return num1
    elif num1 == 0:
        return num
    return summ(num-1,num1+1)

print(f'{num} + {num1} равно: {summ(num,num1)}') 