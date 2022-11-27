class SpaceObject:

    def __init__(self, size):
        self.size = size


class Star(SpaceObject):

    def __init__(self, size, brightness):
        super().__init__(size)
        self.brightness = brightness

    def shine(self):
        print(f'Star brightness: {self.brightness}')


class Planet(SpaceObject):

    def __init__(self, size, population, increasement):
        super().__init__(size)
        self.population = population
        self.increasement = increasement

    def population_in_years(self, years):
        print(f'Through {years} y.e population will consist {self.population + self.increasement * years} creatures')


def check():
    star = Star(340, 456)
    star.shine()

    planet = Planet(400, 1300, 80)
    planet.population_in_years(6)


check()
