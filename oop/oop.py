
# Object-Oriented Programming (OOP) in Python Part-1
class Car:
    def __init__(self, owner, color, brand):
        print("Car is being initialized...")
        self.owner = owner
        self.color = color
        self.brand = brand
        print("Car created")

car1 = Car('Arbin', 'Red', 'Toyota') 
print(f"Owner: {car1.owner}")
print(car1.color)
print(car1.brand)

#👉 Object = instance (car1)
#👉 Attributes = variables inside object (owner, color, brand)

