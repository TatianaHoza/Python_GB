# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
#
# Напишите программу, которая должна возвращать сумму и произведение дробей.
#
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

x1s, y1s = frac1.split('/')
x2s, y2s = frac2.split('/')
x1 = int(x1s)
x2 = int(x2s)
y1 = int(y1s)
y2= int(y2s)
common_y = y1 * y2
new_x1 = x1 * y2
new_x2 = x2 * y1

sum_ = new_x1 + new_x2
multi_x = x1 * x2

print(f'Сумма дробей: {sum_}/{common_y}')
print(f'Произведение дробей: {multi_x}/{common_y}')

fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

sum__ = fraction1 + fraction2
pr = fraction1 * fraction2

print(f'Сумма дробей: {sum__}')
print(f'Произведение дробей: {pr}')