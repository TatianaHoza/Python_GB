class Animal:
    def __init__(self,name):
        self.name = name

class Bird(Animal):
    def __init__(self,name, wingspan,wing_length):
        super.__init__(name)
        self.wingspan = wingspan
        self.wing_length = wing_length



class Fish(Animal):
    def __init__(self,name, max_depth):
        super.__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        else:
            return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, name, weight):
        super.__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        else:
            return 'Обычный'

class AnimalFactory(Animal):
    def create_animal(self, animal_type,*args):
        super.__init__(*args)
        self.animal_type = animal_type
        def show_info(self):
            print(f'Тип')




animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())

