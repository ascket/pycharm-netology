class AnimalsOnFarm:
    def __init__(self, name, age, weight):
        self.name = name
        self.kind = "домашнее животное"
        self.age = age
        self.weight = weight

    def info(self):
        print("{} живёт {} лет, весит {} кг."
              .format(self.name, self.age, self.weight))


class Cows(AnimalsOnFarm):
    def horns(self):
        self.horns = 4
        self.hooves = 4
        print("{} имеет {} рога и {} копыта."
              .format(self.name, self.horns, self.hooves))

    def give(self, milk):
        self.milk = milk
        print("{} даёт в среднем {} литров молока "
              "в месяц.".format(self.name, self.milk))

class Goats(AnimalsOnFarm):
    def horns(self):
        self.horns = "90-100 см"
        print("{} имеет рога длиной {} и копыта."
              .format(self.name, self.horns))

    def give(self, milk):
        self.milk = milk
        self.animal_type = '"млекопитающие"'
        print("{} относится к типу {} и даёт в среднем {} литров молока "
              "в месяц.".format(self.name, self.animal_type, self.milk))

class Shepps(AnimalsOnFarm):
    def give(self, milk):
        self.milk = milk
        self.animal_type = '"млекопитающие"'
        print("{} относится к типу {} и даёт в среднем {} литров молока "
              "в месяц.".format(self.name, self.animal_type, self.milk))

class Pigs(AnimalsOnFarm):
    def give_pork(self, pork):
        self.pork = pork
        print("{} даёт в среднем {} кг мяса.".format
              (self.name, self.pork))

class Ducks(AnimalsOnFarm):
    def give_bird(self, pork):
        self.pork = pork
        print("{} даёт в среднем {} кг мяса."
              .format(self.name, self.pork))

    def wings(self):
        self.wings = 2
        print("Кроме того, {} имеет {} крыла."
              .format(self.name.lower(), self.wings))

class Chickens(AnimalsOnFarm):
    def give_bird(self, pork):
        self.pork = pork
        print("{} даёт в среднем {} кг мяса."
              .format(self.name, self.pork))

    def eggs(self):
        self.wings = 2
        self.eggs = "1-2"
        print("Кроме того, {} имеет {} крыла и нёсёт по {} яйца в день."
              .format(self.name.lower(), self.wings, self.eggs))

class Geese(AnimalsOnFarm):
    def give_bird(self, pork):
        self.pork = pork
        self.animal_type = '"птицы"'
        print("{} относится к типу {} и даёт в среднем {} кг мяса."
              .format(self.name, self.animal_type, self.pork))

    def paws(self):
        self.paws = 2
        self.beak = 1
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
