import socket
import pyfiglet

f = pyfiglet.Figlet(font='slant')
print(f.renderText('ECHO SERVER'))


s = socket.socket()
print('Socket created')

s.bind(('localhost', 8888))

s.listen(3)
print('waiting for connections...')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Name received")
    print(f'Connected with {addr}, {name}')
   

    c.send(bytes(f"Welcome {name} to Echo Chat", 'utf-8'))
    c.close()