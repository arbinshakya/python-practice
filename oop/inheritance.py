#inheritance

#single inhertance
class Car:
    color = "black"

    @staticmethod
    def start():
        print('Car is started')

    @staticmethod
    def stop():
        print('Car stopped')


class Toyota(Car):
    def __init__ (self, name):
        self.name = name

car1 = Toyota("Fortuner")
car2 = Toyota("Yaris")



print(car1.name)
car1.start()
print(car1.color)


