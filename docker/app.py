import time

class Car:
    def __init__(self, wheels=int, color=str):
        self.wheels = wheels
        self.color = color

    
class Mercedes(Car):
    def __init__(self, wheels, color, model = str):
        self.model = model
        super().__init__(wheels, color)

    def info(self):
        print(f"\nMercedes info: ")
        time.sleep(1)
        print(f"Wheels: {self.wheels}")
        print(f"Wheels: {self.color}")
        print(f"Wheels: {self.model}")


c1 = Mercedes(4, 'Black', 'g-series')
c1.info()




