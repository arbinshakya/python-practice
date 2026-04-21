import socket

s = socket.socket()
print('Socket created')

s.bind(('localhost', 8888))

s.listen(3)
print('waiting for connections...')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print(f'Connected with {addr}, {name}')
   

    c.send(bytes('Welcome to my server', 'utf-8'))
    c.close()