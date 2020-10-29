# TCP-Server.py
# A TCP client connects to a TCP server.
# Server responds with a greeting.

from socket import *
serverPort = 10000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Server is ready!')
while 1:
    connectionSocket, addr = serverSocket.accept()
    msgFromClient = connectionSocket.recv(1024).decode()
    print('Message from client:', msgFromClient)
    msgForClient = 'Hello Client!'
    connectionSocket.send(msgForClient.encode())