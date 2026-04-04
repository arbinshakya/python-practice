
# Object-Oriented Programming (OOP) in Python Part-1
class Car:
    def __init__(self, owner):
        print("Car is being initialized...")
        self.owner = owner
        self.color = "red"
        self.brand = "Toyota"
        print("Car created")

car1 = Car('Arbin') 
print(f"Owner: {car1.owner}")
print(car1.color)
print(car1.brand)

#👉 Object = instance (car1)
#👉 Attributes = variables inside object (owner, color, brand)

