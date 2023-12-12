'''Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег'''

sum_ = 0
count_add = 0
count_out = 0

while True:
    if sum_>5000000:
        sum_ -= (0.1*sum_)
        print(sum_)
    action = input("введите тип действия")
    if action == 'q':
        print('выход из банкомата')
        print(sum_)
        break
    elif action == 'a':
        sum_add = int(input("введите сумму пополнения: "))
        if sum_add % 50 == 0:
            sum_ += sum_add
            count_add += 1
            if count_add % 3 == 0:
                sum_ += sum_ * 0.03
        else:
            print("некорретная сумма")
        print(sum_)
    elif action == '0':
        sum_out = int(input("введите сумму снятия: "))

        if sum_out % 50 == 0:
            commision = sum_out * 0.015
            if commision < 30:
                commision = 3
            elif commision > 600:
                commision = 600

        if sum_out + commision > sum_:
            print("средств не достаточно")

        else:
            if sum_out % 50 == 0:
                sum_ -= (sum_out+commision)
                count_out += 1
            if count_out % 3 == 0:
                sum_ += sum_ * 0.03
            else:
                print("некорретная сумма")

    print(sum_)
