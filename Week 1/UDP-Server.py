# UDP-Server.py
# A UDP client connects to a UDP server.
# Server responds with a greeting.

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Server is ready!')
while 1:
    msgFromClient, clientAddress = serverSocket.recvfrom(2048)
    print('Message from client:', msgFromClient.decode())
    msgForClient = 'Hello Client!'
    serverSocket.sendto(msgForClient.encode(), clientAddress)