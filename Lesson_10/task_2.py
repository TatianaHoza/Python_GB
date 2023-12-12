'''Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''


class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        if self.length == 0:
            return self.width ** 2
        elif self.width == 0:
            return self.length ** 2
        else:
            return self.width * self.length

    def perimetr(self):
        if self.length == 0:
            return self.width * 4
        elif self.width == 0:
            return self.length * 4
        else:
            return (2 * self.width + 2 * self.length)


fig1 = Rectangle(10, 5)
print(fig1.area(), fig1.perimetr())

fig2 = Rectangle(2)
print(fig2.area(), fig2.perimetr())
