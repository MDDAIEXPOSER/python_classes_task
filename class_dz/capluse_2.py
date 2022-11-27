class Hero:
    def __init__(self, health, power, rank):
        self.health = health
        self.power = power
        self.__rank = rank

    def option_rank(self, rank):
        self.__rank = rank

    def get_rank(self):
        return self.__rank

    def del_rank(self):
        del self.__rank

    def fight(self, character):
        while self.power > 0:
            character.health -= 2
            self.power -= 10
        if character.health < 0:
            self.option_rank('One of all the best')
            print(self.get_rank())
        else:
            self.del_rank()
            print('Go away, loser')


def check():
    character_1 = Hero(300, 800, 'Newbie')
    hero2 = Hero(100, 1000, 'пушечное мясо')
    hero1.fight(hero2)


check()
