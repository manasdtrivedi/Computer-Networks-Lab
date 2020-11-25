# UDP-Client.py
# A UDP client connects to a UDP server.
# Server responds with a greeting.

from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
msgForServer = 'Hello Server!'
clientSocket.sendto(msgForServer.encode(),(serverName, serverPort))
msgFromServer, serverAddress = clientSocket.recvfrom(2048)
print('Message from server:', msgFromServer.decode())
clientSocket.close()