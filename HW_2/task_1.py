# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = 255
test = hex(num)
base: int = 16
base_digits ="0123456789ABCDEF"
res: str = ''
while num > 0:
    remainder = num % base
    res = base_digits[remainder] + res
    num //= base

print(f'Шестнадцатеричное представление числа: {res}')
print(f'Проверка результата: {test}')
