#multi level inheritance

class Car:
    @staticmethod
    def start():
        print('Car started')

    @staticmethod
    def stop():
        print('Car stopped')


class Toyota(Car):
    def __init__ (self, brand):
        self.brand = brand

class Fortuner(Toyota):
    def __init__ (self,brand, type):
        super(). __init__(brand)
        self.type = type



car1 = Fortuner('Toyota','Diesel')
car1.start()

print(f"Brand: {car1.brand}\nType: {car1.type}")

