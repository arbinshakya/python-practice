import socket

c = socket.socket()

c.connect(('localhost', 8888))
name = input("Enter you name: ")
print(c.recv(1024).decode()) #buffer size





