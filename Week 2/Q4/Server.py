# Server.py
# Client sends simple arithmetic expression like "1 + 2" to the server.
# Server evaluates the received expression and sends the result to the client.
# Server is concurrent, and can hence can handle multiple clients simultaneously.
# "Concurrent Math Server"

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
            print("Message from " + str(addr) + ": " + msgFromClient)
            connectionSocket.send(str(eval(msgFromClient)).encode())
        except:
            connectionSocket.close()
            break

def welcomeClients():
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(addr, 'has connected with the server.')
        thread = threading.Thread(target=connSocketController, args=(connectionSocket, addr))
        thread.start()

print('Server is ready to welcome clients.')
welcomeClients()