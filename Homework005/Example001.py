'''Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''


import random
num = random.randint(0,10)
num1 = random.randint(0,5)
def sqrt(num,num1):
    if num1 == 0:
        return 1
    elif num1 == 1:
        return num
    return num*sqrt(num,num1-1)

print(f'{num} в степени {num1} равно: {sqrt(num,num1)}') 