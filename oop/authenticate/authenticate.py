#login system
from getpass import getpass
import pwinput

class User:
    def __init__ (self, username, password):
        self.username = username
        self.password = password


    
class Login_System:
    def __init__(self):
        self.users = []

    def signup(self):
        username = input("Create Username: ")
        password = pwinput.pwinput(prompt="Enter password: ", mask="*")
        confirm_password = pwinput.pwinput(prompt="Enter password: ", mask="*")


        for user in self.users:
            if user.username == username:
                print('Username already taken')
                return
            
        if password != confirm_password:
            print("Passwords not matched")
            return
            
        self.users.append(User(username,password))
        print('signup successful')

                       


    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
            return False
            
    def login(self):
        username = input("Enter Username: ")
        password = pwinput.pwinput(prompt="Enter password: ", mask="*")

        if self.authenticate(username, password):
            print('Login Successful')
        else:
            print("Login unsuccessful")

    def menu(self):
        while True:
            print('\n1. SignUp')
            print('2. Login')
            print('3. Exit')

            choice = input('Choose option: ')
            if choice == '1':
                self.signup()
            elif choice == '2':
                self.login()
            elif choice == '3':
                print('Good bye')
                break
            else:
                print('Invalid choice')






if __name__ == "__main__":
    system = Login_System()
    system.menu()

            

