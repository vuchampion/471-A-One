from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)
clientPort = 80
print('Client socket has been created')

request = input()
try:
    clientSocket.connect(('', clientPort))
except:
    print('Could not complete connection')

while request.lower().strip() != 'exit':
    clientSocket.send(request.encode())
    data = clientSocket.recv(1024).decode()

    print('Recieved from server: ' + data)
    request = input()

clientSocket.close()
