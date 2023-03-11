'''Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no '''
#Вариант 1. Рандом + цикл
"""import random
number_bilet = random.randint(100000,999999)
print(f'Номер билета: {number_bilet}')
num = 0
num1 = 0
result = 0
result1 = 0
while number_bilet > 999:
    result = number_bilet % 10
    num = result + num
    number_bilet = number_bilet // 10
while number_bilet > 0:
    result1 = number_bilet % 10
    num1 = result1 + num1
    number_bilet = number_bilet // 10
print(f'Сумма первых трех цифр {num1}')
print(f'Сумма последних трех цифр {num}')
if num == num1:
    print('Ура счастливый билет')
else:
    print('Повезет в другой раз')"""

#Вариант 2. Простой счёт
number_bilet = int(input('Введите шестизначное число: '))
if number_bilet < 100000 or number_bilet > 999999:
    print('Ввеедное число не подходит под условие')
else:
    one = number_bilet//100000
    two = number_bilet//10000%10
    three = number_bilet//1000%10
    four = number_bilet//100%10
    five = number_bilet//10%10
    six = number_bilet%10
    summ = one + two + three
    summ1 = four + five + six
    if summ == summ1:
        print('Билет счастливый')
    else:
        print('Повезет в другой раз')
