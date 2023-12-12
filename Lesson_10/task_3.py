'''Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
'''


class Person:

    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 100:
            raise ValueError('old')
        self.__age = value

    def birthday(self):
        return (self.age + 1)

    def full_name(self):
        full_all_name = self.first_name + ' ' + self.second_name
        return full_all_name


person_1 = Person('Anna', 'Petrova', 25)
print(person_1.age)
