# Client.py
# Client sends groups of strings to the server.
# Server responds with strings in lexicographically increasing order and increasing order by length.

import socket
import threading

serverName = 'localhost'
serverPort = 10000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def receiveMessage():
    while True:
        try:
            msgFromServer = clientSocket.recv(1024).decode()
            print('Lexicographically increasing order:', msgFromServer)
            msgFromServer = clientSocket.recv(1024).decode()
            print('Increasing order by length:', msgFromServer)
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