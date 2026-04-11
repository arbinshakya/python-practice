# class methods

class Person:
    name = 'anonymous'

    # def change_name(self, name):
    #     self.__class__.name = name

    @classmethod
    def change_name(cls, name):
        cls.name = name


p1 = Person()  
p1.change_name('Arbin')  
print(p1.name)
print(Person.name)
