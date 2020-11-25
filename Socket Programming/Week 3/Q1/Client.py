# Client.py
# Client sends strings to the server.
# If client sends "Bye", server responds with "Bye"
# Else, server capitalizes received string, and sends the result.
# The client closes when it receives "Bye" from the server.

import socket
import threading
import os

serverName = 'localhost'
serverPort = 10000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def receiveMessage():
    while True:
        try:
            msgFromServer = clientSocket.recv(1024).decode()
            print("Message from server:", msgFromServer)
            if msgFromServer == 'Bye':
                clientSocket.close()
                os._exit(0)
                break
        except:
            clientSocket.close()
            break

def sendMessage():
    while True:
        try:
            msgForServer = input()
            clientSocket.send(msgForServer.encode())
        except:
            socketIsOpen = 0
            clientSocket.close()
            break

receiveMessageThread = threading.Thread(target=receiveMessage)
receiveMessageThread.start()

sendMessageThread = threading.Thread(target=sendMessage)
sendMessageThread.start()