'''� Создайте файл, в котором вы импортируете встроенные в
модуль функции под псевдонимами. (3-7 строк импорта).'''

from math import sin as f_1
from random import randint as rnd

print(f_1(60))
print(rnd(1, 50))