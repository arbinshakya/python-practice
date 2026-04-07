#Method practice example

class Student:
    def __init__ (self):
        pass

    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    
    def  average(self):
        sum = 0
        for val in self.marks:
            sum += val
        
        return sum/len(self.marks)


        # return sum(self.marks) / len(self.marks)
    
    def result(self):
        if self.average() > 40:
            return 'pass'
        else:
            return 'fail'

    

s1 = Student('Arbin', [85, 90, 78, 99, 2,2])
print(round(s1.average(),2))
print(s1.result())
    