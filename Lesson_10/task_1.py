'''Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''


class Circul:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def circul_len(self):
        return 2 * self.pi * self.radius

    def circul_area(self):
        return self.pi * (self.radius ** 2)

circul1 = Circul(5)
print(circul1.circul_len())
print(circul1.circul_area())
