import socket
import pyfiglet

f = pyfiglet.Figlet(font='SLANT')
print(f.renderText('ECHO CHAT'))


c = socket.socket()

c.connect(('localhost', 8888))
name = input("Enter you name: ")
print("Sending name...")
c.send(bytes(name, 'utf-8'))
print(c.recv(1024).decode()) #buffer size





