class Animals:
    sound = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self, food_weight):
        self.weight += food_weight
        return print(f'{self.name} eats {food_weight} kilos of food.')

    def talk(self):
        return print(f'{self.name} says \"{self.sound}!\"')


class Birds(Animals):
    def collect_eggs(self, number):
        return print(f'{number} eggs collected')


class Milk(Animals):
    def milk(self, volume):
        self.weight -= volume
        return print(f'{volume} l of milk collected')


class Goose(Birds):
    sound = 'gaaaaa'


class Chicken(Birds):
    sound = 'kokoko'


class Cow(Milk):
    sound = 'muuuuu'


class Sheep(Animals):
    sound = 'beeee'

    def shave(self, wool_mass):
        self.weight -= wool_mass
        return print(f'{wool_weight} g of wool collected.')


class Goat(Milk):
    sound = 'meeee'


class Duck(Birds):
    sound = 'cryaaaa'


def create_farm():
    uncle_joe_farm = []
    uncle_joe_farm.append(Goose('Серый', 10))
    uncle_joe_farm.append(Goose('Белый', 11))
    uncle_joe_farm.append(Chicken('Коко', 3))
    uncle_joe_farm.append(Chicken('Кукареку', 2))
    uncle_joe_farm.append(Sheep('Барашек', 14))
    uncle_joe_farm.append(Sheep('Кудрявый', 16))
    uncle_joe_farm.append(Goat('Рога', 22))
    uncle_joe_farm.append(Goat('Копыта', 21))
    uncle_joe_farm.append(Cow('Манька', 350))
    uncle_joe_farm.append(Duck('Кряква', 5))


    def find_haviest_animal():
        print(f'The haviest animal is {sorted(uncle_joe_farm, key=lambda x: x.weight, reverse=True)[0].name}.')

    def find_total_weight():
        total_weight = 0
        for animal in uncle_joe_farm:
            total_weight += animal.weight
        print(f'Total weight of all the animals in the farm: {total_weight} kgs.')

    def talk_all():
        for animal in uncle_joe_farm:
            animal.talk()

    def feed_all(quantity):
        for animal in uncle_joe_farm:
            animal.feed(quantity)

    find_haviest_animal()
    find_total_weight()
    find_animal_type()
    talk_all()
    feed_all(10)


create_farm()