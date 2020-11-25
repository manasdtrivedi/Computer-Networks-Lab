# TCP-Client.py
# A TCP client connects to a TCP server.
# Server responds with a greeting.

from socket import *
serverName = 'localhost'
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
msgForServer = 'Hello Server!'
clientSocket.send(msgForServer.encode())
msgFromServer = clientSocket.recv(1024).decode()
print('Message from server:', msgFromServer)
clientSocket.close()