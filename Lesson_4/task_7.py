'''Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь'''

company_dict = {
    "Nocia": [10000, 8000, -1000],
    "Samsung": [15000, 12000],
    "Souz": [2000, 3000]
}


def check_profit(companies):
    res = {k: sum(v) for k, v in companies.items()}
    print(res)
    if all(map(lambda x: x > 0, res.values())):
        return True
    else:
        return False


def task_7(dat:dict):
    for el in dat.values():
        if sum(el) < 0:
            return False
    return True

print(check_profit(company_dict))

print(task_7(company_dict))