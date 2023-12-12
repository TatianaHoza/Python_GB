# Посчитайте сумму четных элементов от 0 до n исключая кратные e

n = int(input('Введите n:'))
e = int(input('Введите e:'))
number = 0
sum = 0
while number <= n:
    number += 1
    if number % 2 == 0 and number % e != 0:
        sum += number

print(sum)


