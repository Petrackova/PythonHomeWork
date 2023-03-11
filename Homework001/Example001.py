#Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

#Вариант 1. Рандом + цикл
import random
num = random.randint(100,999)
print(f'Трехзначное число равно: {num}')
num_null = 0
result = 0
while num > 0:
    result = num % 10
    num_null = result + num_null
    num = num // 10
print(f'Сумма цифр в числе {num_null}')

# Вариант 2. Просто счёт

num = int(input('Введите трехзначное число: '))
one = num//100
two = num//10%10
three = num%10
print(f'Сумма цифр в числе {one+two+three}')