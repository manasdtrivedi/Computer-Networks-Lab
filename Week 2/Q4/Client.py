# Client.py
# Client sends simple arithmetic expression like "1 + 2" to the server.
# Server evaluates the received expression and sends the result to the client.
# Server is concurrent, and can hence can handle multiple clients simultaneously.
# "Concurrent Math Server"

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
            print('Message from server:', msgFromServer)
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