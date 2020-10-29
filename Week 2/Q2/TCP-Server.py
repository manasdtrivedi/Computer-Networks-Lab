# TCP-Server.py
# Client and server can send and receive messages.
# Chat application.

import socket
import threading

serverPort = 10000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen()

def connSocketController(connectionSocket, addr):
    while True:
        try:
            msgFromClient = connectionSocket.recv(2048).decode()
            print("Message from client:", msgFromClient)
        except:
            connectionSocket.close()
            break

print("Server is ready!")
connectionSocket, addr = serverSocket.accept()
print(addr, "connected.")
thread = threading.Thread(target=connSocketController, args=(connectionSocket, addr))
thread.start()
msgForClient = "Hello for the first time!"
connectionSocket.send(msgForClient.encode())
while True:
    try:
        msgForClient = input()
        connectionSocket.send(msgForClient.encode())
    except:
        clientSocket.close()
        break