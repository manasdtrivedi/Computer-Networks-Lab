# Server.py
# Client sends groups of strings to the server.
# Server responds with strings in lexicographically increasing order and increasing order by length.

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
            listOfStrings = msgFromClient.split()
            listOfStrings.sort()
            msgForClient = ', '.join(listOfStrings)
            connectionSocket.send(msgForClient.encode())
            listOfStrings.sort(key=len)
            msgForClient = ', '.join(listOfStrings)
            connectionSocket.send(msgForClient.encode())
        except:
            connectionSocket.close()
            break

def welcomeClients():
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(addr, "connected.")
        thread = threading.Thread(target=connSocketController, args=(connectionSocket, addr))
        thread.start()
        
print("Server is ready!")
welcomeClients()