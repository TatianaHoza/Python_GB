'''Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь'''

from task_3 import Person
from random import randint


class Employee(Person):

    # def __init__(self, *args):
    #     # super().__init__(*args)
    #     self._id = randint(100000, 999999)
    #     self._level = sum(int(i) for i in str(self._id)) % 7

    def get_id(self):
        self._id = randint(100000, 999999)
        return self._id

    def get_level(self):
        self._level = sum(int(i) for i in str(self._id)) % 7
        return self._level


employee = Employee('Петров', 'Саня', 45)

print(employee.second_name)

print(employee.full_name())
print(employee.get_id())
print(employee.get_level())