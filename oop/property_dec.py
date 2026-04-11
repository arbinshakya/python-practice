#property decorator
#note: we use @property decorator on any method in the calss to sue the method as a property

class Student:
    def __init__ (self, phy, che, math):
        self.phy = phy
        self.chem = che
        self.math = math
        #self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    @property
    def percentage(self):
        return  str(round((self.phy + self.chem + self.math)/3)) + "%"
    
    def result(self):
        if float(self.percentage.strip('%')) >=40:
            print("PASS")
        else:
            print("FAIL")


        
stu1 = Student(90,81,90)
print(stu1.percentage)
print(stu1.result())


stu1.chem = 1
stu1.math = 0
print(stu1.percentage)
print(stu1.result())