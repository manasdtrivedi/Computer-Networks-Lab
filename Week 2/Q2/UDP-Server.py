# UDP-Server.py
# Client and server can send and receive messages.
# Chat application.

import socket
import threading

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

def receiveMsgFromClient():
    while True:
        msgFromClient, clientAddress = serverSocket.recvfrom(2048)
        print("Message from client:", msgFromClient.decode())

msgFromClient, clientAddress = serverSocket.recvfrom(2048)
print('First message from client ' + str(clientAddress) + ' received: ' + msgFromClient.decode())
thread = threading.Thread(target=receiveMsgFromClient)
thread.start()
msgForClient = 'Hello for the first time!'
serverSocket.sendto(msgForClient.encode(), clientAddress)
while True:
    msgForClient = input()
    serverSocket.sendto(msgForClient.encode(), clientAddress)