'''✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.'''

even_gen = (num for num in range(0,101,2) if sum([int(digit) for digit in str(num)]) != 8)
print(list(even_gen))