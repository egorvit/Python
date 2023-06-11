import random


class Home:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0
        self.fur_coat = 0

    def act(self, family):
        for family_member in family:
            family_member.act()
            if self.dirt > 90 and not isinstance(family_member, Cat):
                family_member.happiness -= 10
            if family_member.satiety < 0:
                raise Warning(f'{family_member.name} погиб от голода!')
            elif not isinstance(family_member, Cat) and family_member.happiness < 10:
                raise Warning(f'{family_member.name} погиб от депрессии')
            print(family_member)
            print(self)

    def __str__(self):
        return """Деньги: {money}, Еда: {food}, Еда для кота: {cat_food}, Грязь: {dirt}, Шубы: {fur_coat}""".\
            format(money=self.money, food=self.food, cat_food=self.cat_food, dirt=self.dirt, fur_coat=self.fur_coat)


class Family:
    def __init__(self, name, home):
        self.name = name
        self.satiety = 30
        self.home = home

    def eating(self):
        if 10 < self.home.food <= 30:
            food_amount = random.randrange(10, self.home.food)
        else:
            food_amount = random.randrange(10, 30)
        self.satiety += food_amount
        self.home.food -= food_amount
        print(f'{self.name}, Ест еду')

    def act(self):
        if self.satiety < 30 and self.home.food != 0:
            self.eating()

    def __str__(self):
        return '{name}, Сытость {satiety}'.format(name=self.name, satiety=self.satiety)


class Human(Family):
    def __init__(self, name, home):
        super().__init__(name, home)
        self.happiness = 100

    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def act(self):
        super().act()
        if self.happiness < 20:
            self.pet_the_cat()


class Husband(Human):

    def playing(self):
        self.satiety -= 10
        self.happiness += 20
        print(f'{self.name}, Играет')

    def work(self):
        self.satiety -= 10
        self.home.money += 150
        print(f'{self.name}, Работает')

    def act(self):
        super().act()
        if self.home.money < 100:
            self.work()
        else:
            self.playing()


class Wife(Human):
    def buy_food(self):
        self.home.food += 30
        self.home.money -= 40
        self.home.cat_food += 10
        self.satiety -= 10
        print(f'{self.name}, Пошла за покупками')

    def buy_coat(self):
        self.home.money -= 50
        self.happiness += 60
        self.satiety -= 10
        self.home.fur_coat += 1
        print(f'{self.name}, Купила шубу')

    def clean_house(self):
        self.home.dirt -= random.randrange(1, 100)
        self.satiety -= 10
        print(f'{self.name}, Убирает дом')

    def act(self):
        super().act()
        if self.home.food < 30 or self.home.cat_food < 30:
            self.buy_food()
        elif self.home.dirt > 60:
            self.clean_house()
        else:
            self.buy_coat()


class Cat(Family):

    def eating(self):
        if self.home.cat_food <= 30:
            food_amount = random.randrange(10, self.home.cat_food)
        else:
            food_amount = random.randrange(10, 30)
        self.home.cat_food -= food_amount
        self.satiety += 2 * food_amount

    def tear_wallpaper(self):
        self.home.dirt += 5
        self.satiety -= 10
        print(f'{self.name}, Дерёт обои')

    def act(self):
        super().act()
        self.tear_wallpaper()


family_home = Home()

husband = Husband('Олег', family_home)
wife = Wife('Аксана', family_home)
cat = Cat('Мяу', family_home)
family_list = [husband, wife, cat]
for day in range(1, 366):
    print('День,', day)
    family_home.act(family_list)
    print('------------')
    if day == 365:
        print()
