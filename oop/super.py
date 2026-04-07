#super method

class Car:
    def __init__ (self, type):
        self.type = type

    @staticmethod
    def start():
        print('Car started')

    @staticmethod
    def stop():
        print('Car stopped')


class ToyotaCar(Car):
    def __init__ (self, name, type):
        super().__init__(type)
        super().start()
        self.name = name


c1 = ToyotaCar("Yaris", "Petrol")
print(c1.type)
c1.start()