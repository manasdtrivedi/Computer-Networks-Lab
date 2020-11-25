# UDP-Client.py
# Clients can send messages to a server, which broadcasts it to other clients.
# Clients can receive messages from the server.
# Chat room application.

import socket
import threading

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))

def receiveMessage():
    while True:
        try:
            msgFromServer, serverAddress = clientSocket.recvfrom(2048)
            print(msgFromServer.decode())
        except:
            clientSocket.close()
            break

def sendMessage():
    while True:
        msgForServer = input()
        clientSocket.sendto(msgForServer.encode(), (serverName, serverPort))

receiveMessageThread = threading.Thread(target=receiveMessage)
receiveMessageThread.start()

sendMessageThread = threading.Thread(target=sendMessage)
sendMessageThread.start()
