#login system static
import pyfiglet

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class LoginSystem:
    def __init__(self):
        self.users = [
            User("admin", "1234"),
            User("arbin","4321")
        ]

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
            else:
                return False
            
    def login(self):
        f = pyfiglet.Figlet(font='slant')
        print(f.renderText('Echo Chat'))
        username = input("Enter username: ")
        password = input("Enter password: ")

        if self.authenticate(username, password):
            print("Login successfull")
        else:
            print('Invalid Credentials')


if __name__ == "__main__":
    system = LoginSystem()
    system.login()

