from playsound import playsound

class Human:
    def cracking(self):
        playsound('duck.wav')

    def get_clothes(self):
        print('I wear only Prada')

class Duck:
    def cracking(self):
        playsound('duck.wav')

    def get_clothes(self):
        print('I wear only Dior')

def main():
    que_exp = [Human(), Duck()]
    for object in que_exp:
        object.cracking()
        object.get_clothes()
