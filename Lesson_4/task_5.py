'''Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии. '''

names = ['Борис', 'Иван', 'Петр', "Сергей"]
salaries = [10000, 12000, 16000, 14000]
awards = ['12.35%', '10.25%', '7.75%', '8.85%']


def func(lst_names, lst_bases, lst_bonuses):
    dct = {name: (base * float(award.rstrip("%")) / 100) for name, base, award in
           zip(lst_names, lst_bases, lst_bonuses)}
    return dct


print(func(names, salaries, awards))
