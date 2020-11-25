# Server.py
# Client sends strings to the server.
# If client sends "Bye", server responds with "Bye"
# Else, server capitalizes received string, and sends the result.
# The client closes when it receives "Bye" from the server.

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
            if msgFromClient.lower() == 'bye':
                msgForClient = 'Bye'
                connectionSocket.send(msgForClient.encode())
                connectionSocket.close()
                break
            else:
                msgForClient = msgFromClient.upper()
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