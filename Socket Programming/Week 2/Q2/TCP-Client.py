# TCP-Client.py
# Client and server can send and receive messages.
# Chat application.

import socket
import threading

serverName = 'localhost'
serverPort = 10000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('Message from server:', clientSocket.recv(1024).decode())

def receiveMessage():
    while True:
        try:
            msgFromServer = clientSocket.recv(1024).decode()
            print("Message from server:", msgFromServer)
        except:
            clientSocket.close()
            break

def sendMessage():
    while True:
        try:
            msgForServer = input()
            clientSocket.send(msgForServer.encode())
        except:
            clientSocket.close()
            break

receiveMessageThread = threading.Thread(target=receiveMessage)
receiveMessageThread.start()

sendMessageThread = threading.Thread(target=sendMessage)
sendMessageThread.start()