# TCP-Server.py
# Clients can send messages to a server, which broadcasts it to other clients.
# Clients can receive messages from the server.
# Chat room application.

import socket
import threading

serverPort = 10000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen()
connectionSockets = []

def sendToAllClients(message, senderConnSocket):
    for connectionSocket in connectionSockets:
        if connectionSocket is not senderConnSocket:
            connectionSocket.send(message)

def connSocketController(connectionSocket, addr):
    while True:
        try:
            msgForAll = str(addr) + ': ' + connectionSocket.recv(1024).decode()
            sendToAllClients(msgForAll.encode(), connectionSocket)
        except:
            sendToAllClients((str(addr) + ' exited the chatroom.').encode(), connectionSocket)
            connectionSockets.remove(connectionSocket)
            connectionSocket.close()
            break

def welcomeClients():
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(addr, 'has connected with the server.')
        connectionSockets.append(connectionSocket)
        sendToAllClients((str(addr) + ' entered the chatroom.').encode(), connectionSocket)
        thread = threading.Thread(target=connSocketController, args=(connectionSocket, addr))
        thread.start()

print('Server is ready to welcome clients.')
welcomeClients()

