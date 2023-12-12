''' Пользователь вводит число от 1 до 999
Нужно сообщить, что введено Ж одно- двух, трехзначное число
Для цифры верните ее квадрат
для дву - произведение цифр
тля трех - зеркальное отображение
если число не из диапазона запросить новое'''


while True:
    number = int(input('enter number 1 - 999'))

    if number < 1 or number > 999:
        continue
    elif number < 10:
        result = number ** 2
    elif number >= 10 and number <= 99:
        result = (number // 10) * (number % 10)
    elif number >= 100:
            result = str(number % 10) + str((number // 10) % 10) + str(number // 100)



print(result)