# Server.py
# Client asks for current date
# Server responds with current date

import socket
import threading
import datetime

serverPort = 10000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen()

def connSocketController(connectionSocket, addr):
    while True:
        try:
            msgFromClient = connectionSocket.recv(2048).decode()
            print("Message from client:", msgFromClient)
            if msgFromClient.lower().find('date') == -1:
                msgForClient = 'Enter \'date\' to receive today\'s date!'
                connectionSocket.send(msgForClient.encode())
            else:
                msgForClient = str(datetime.date.today())
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

