#note: __ represents private attrtibute
#Private attributes & methods are meant to be used only within the class and not accessible fro outside the class

class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello World")

    def hi(self):
        self.__hello()

p1 = Person()
p1.hi()