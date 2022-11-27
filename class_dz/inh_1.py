class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power


class Assasin(Hero):
    def __init__(self, health, power):
        super().__init__(health, power)

    def hello(self):
        print('steal your heart..')

    def attack(self, opps):
        opps.health -= self.power * 4
        self.power -= 5

def check():
    hero = Hero(500, 20)
    creed = Assadin(500, 20)
    creed.hello()
    creed.attack(hero)
    print('Хитрость ассасина:', creed.power)
    print(f'hero здоровье:', hero.health)


check()
