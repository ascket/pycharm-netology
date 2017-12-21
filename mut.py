class Animals_on_farm:
    def __init__(self, name, age, weight):
        self.name = name
        self.kind = "домашнее животное"
        self.age = age
        self.weight = weight

    def info(self):
        print("{} - это {}.".format(self.name, self.kind))
        print("{} имеет продолжительность жизни (лет): {}.".format(self.name, self.age))
        print("Максимальный вес, которого достигает {} равен {} кг.".format(self.name.lower(), self.weight))

class Mammals_birds(Animals_on_farm):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def give(self, milk, animal_type = '"млекопитающие"'):
        self.milk = milk
        self.animal_type = animal_type
        print("{} относится к типу {} и даёт в среднем {} литров молока в месяц.".format(self.name, self.animal_type, self.milk))

    def give_pork(self, pork, animal_type = '"млекопитающие"'):
        self.pork = pork
        self.animal_type = animal_type
        print("{} относится к типу {} и даёт в среднем {} кг мяса.".format(self.name, self.animal_type, self.pork))

    def give_bird(self, pork, animal_type = '"птицы"'):
        self.pork = pork
        self.animal_type = animal_type
        print("{} относится к типу {} и даёт в среднем {} кг мяса.".format(self.name, self.animal_type, self.pork))

animal_1 = Mammals_birds("Корова", 20, 1200)
animal_1.info()
animal_1.give(300)
animal_2 = Mammals_birds("Коза", 15, 70)
animal_2.info()
animal_2.give(50)
animal_3 = Mammals_birds("Овца", 14, 55)
animal_3.info()
animal_3.give(35)
animal_4 = Mammals_birds("Свинья", 13, 300)
animal_4.info()
animal_4.give_pork(150)
animal_5 = Mammals_birds("Утка", 20, "3,5")
animal_5.info()
animal_5.give_bird("1,5")
animal_6 = Mammals_birds("Курица", 13, 5)
animal_6.info()
animal_6.give_bird("0,5")
animal_7 = Mammals_birds("Гусь", 20, 12)
animal_7.info()
animal_7.give_bird("4-5")