from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)
clientPort = 84
print('Client socket has been created')

request = input()
try:
    clientSocket.connect(('', clientPort))
except:
    print('Could not complete connection')
print('Connected with the server')

clientSocket.send(request.encode())
data = clientSocket.recv(1024).decode()

print('Recieved from server: ' + data)
clientSocket.close()
