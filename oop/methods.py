#METHODS IN PYTHON

class Student:

    College = "ABC University"
    def __init__ (self):
        pass

    def __init__ (self, name, age, grade):
        print('Student is beinig intialized...')
        self.name = name
        self.age = age
        self.grade = grade


    def Welcome(self):
        print(f"Welcome, {self.name}!")

    
    def get_grade(self):
        return self.grade 
        
s1 = Student('Arbin', 20, 'A')
s1.Welcome()
print(f"Name: {s1.name}")
print(f"Age: {s1.age}")
print(f"College: {s1.College}")
print(f"Grade: {s1.get_grade()}")


