class Car:
    def __init__(self, owner):
        print("Car is being initialized...")
        self.owmer = owner
        self.color = "red"
        self.brand = "Toyota"
        print("Car created")

car1 = Car('Arbin')
print(f"Owner: {car1.owmer}")
print(car1.color)
print(car1.brand)

car2 = Car('John')
print(f"Owner: {car2.owmer}")
print(car2.color)
print(car2.brand)

