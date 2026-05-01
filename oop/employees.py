class Employee:
    def __init__(self,role, dept, salary=int):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role = ",self.role)
        print("dept = ",self.dept)
        print("salary = ",self.salary)


class Engineer(Employee):
    def __init__(self, name, age=int):
       self.name = name
       self.age = age
       super().__init__('Engineer', 'IT', '7000000')

    def showDetails(self):
        print('name= ', self.name)
        print('age= ', self.age)
        super().showDetails()


e1 = Engineer('Shakya', 23)
e1.showDetails()


# e1 = Employee('Arbin','Software Engineer', 'DATA', 3,00,000)
# e1.showDetails()
