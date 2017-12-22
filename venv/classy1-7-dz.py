class Animals_on_farm:
    def __init__(self, name, age, weight):
        self.name = name
        self.kind = "домашнее животное"
        self.age = age
        self.weight = weight

    def info(self):
        print("{} - это {}.".format(self.name, self.kind))
        print("{} имеет продолжительность жизни (лет): {}."
              .format(self.name, self.age))
        print("Максимальный вес, которого достигает {} равен {} кг."
              .format(self.name.lower(), self.weight))

    def give(self, milk, animal_type='"млекопитающие"'):
        self.milk = milk
        self.animal_type = animal_type
        print("{} относится к типу {} и даёт в среднем {} литров молока "
              "в месяц.".format(self.name, self.animal_type, self.milk))

    def give_bird(self, pork, animal_type='"птицы"'):
        self.pork = pork
        self.animal_type = animal_type
        print("{} относится к типу {} и даёт в среднем {} кг мяса."
              .format(self.name, self.animal_type, self.pork))


class Cows(Animals_on_farm):
    def __init__(self, name, weight, age, hooves=4):
        super().__init__(name, weight, age)
        self.hooves = hooves

    def horns(self, horns=4):
        self.horns = horns
        print("{} имеет {} рога и {} копыта."
              .format(self.name, self.horns, self.hooves))

class Goats(Animals_on_farm):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def horns(self):
        self.horns = "90-100 см"
        print("{} имеет рога длиной {} и копыта."
              .format(self.name, self.horns))

class Shepps(Animals_on_farm):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def latain(self, latain='"Ovis aries"'):
        self.latain = latain
        print("{} по латыни {}."
              .format(self.name, self.latain))

class Pigs(Animals_on_farm):
    def __init__(self, name, weight, age, animal_type='"млекопитающие"'):
        super().__init__(name, weight, age)
        self.animal_type = animal_type

    def give_pork(self, pork):
        self.pork = pork
        print("{} относится к типу {} и даёт в среднем {} кг мяса.".format
              (self.name, self.animal_type, self.pork))

class Ducks(Animals_on_farm):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def wings(self, wings=2):
        self.wings = wings
        print("Кроме того, {} имеет {} крыла."
              .format(self.name.lower(), self.wings))

class Chickens(Animals_on_farm):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def eggs(self, wings=2, eggs="1-2"):
        self.wings = wings
        self.eggs = eggs
        print("Кроме того, {} имеет {} крыла и нёсёт по {} яйца в день."
              .format(self.name.lower(), self.wings, self.eggs))

class Geese(Animals_on_farm):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def paws(self, paws=2, beak=1):
        self.paws = paws
        self.beak = beak
        print("{} отличается {} лапами и {} клювом."
              .format(self.name, self.paws, self.beak))


animal_1 = Cows("Корова", 20, 1200)
animal_1.info()
animal_1.give(300)
animal_1.horns()
animal_2 = Goats("Коза", 15, 70)
animal_2.info()
animal_2.give(50)
animal_2.horns()
animal_3 = Shepps("Овца", 14, 55)
animal_3.info()
animal_3.give(35)
animal_3.latain()
animal_4 = Pigs("Свинья", 13, 300)
animal_4.info()
animal_4.give_pork(150)
animal_5 = Ducks("Утка", 20, "3,5")
animal_5.info()
animal_5.give_bird("1,5")
animal_5.wings()
animal_6 = Chickens("Курица", 13, 5)
animal_6.info()
animal_6.give_bird("0,5")
animal_6.eggs()
animal_7 = Geese("Гусь", 20, 12)
animal_7.info()
animal_7.give_bird("4-5")
animal_7.paws()
