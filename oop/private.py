#private key 
#example1
class Account():
    def __init__ (self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)
    

a1 = Account('1231231','ASSD')
print(a1.acc_no)
print(a1.__acc_pass)

print(a1.reset_pass())

