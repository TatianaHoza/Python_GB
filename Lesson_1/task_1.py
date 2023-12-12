# Решить квадратное уравнение 5х 2 -10х -400 = 0
from math import sqrt

a = 5
b = -10
c = -400

D = b**2 - 4*a*c

if D < 0:
    print("Корней нет")

elif D == 0:
    x_1 = (-b + sqrt(D))/(2*a)
    print("x = " + x_1)

else:
    x_1 = (-b + sqrt(D)) / (2 * a)
    x_2 = (-b - sqrt(D)) / (2 * a)
    print("x1 = " + str(x_1))
    print("x2 = " + str(x_2))