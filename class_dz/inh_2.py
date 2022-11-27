class Genius:

    def __init__(self, name):
        self.name = name

    def write_genius(self):
        return f'{self.name} гений'


class learn_poop(Genius):

    def __init__(self, name):
        super().__init__(name)

    def make_object(self):
        who = Genius(self.name)
        return who

    def complete(self):
        print(f'{self.make_object().write_genius()}, go away from ship, dude')


def check():
    test = learn_poop('Jaden')
    test.complete()
