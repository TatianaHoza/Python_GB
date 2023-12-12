num = 100000


if 1 < num and num < 100001:
    if num // num == 1 and num % num == 0 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3):
        print(f'{num} является простым числом')
    else:
        print(f'{num} является составным числом')

else:
    print('Число должно быть больше 1 и меньше 100000')