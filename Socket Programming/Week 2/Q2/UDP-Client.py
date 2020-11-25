# UDP-Client.py
# Client and server can send and receive messages.
# Chat application.

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
            print("Message from server:", msgFromServer.decode())
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
