from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)
clientPort = 80
print('Client socket has been created')

try:
    clientSocket.connect(('', clientPort))
except:
    print('Could not complete connection')

clientSocket.sendall('simple_webpage.html'.encode())
data = clientSocket.recv(1024)

clientSocket.close()
print('Recieved', repr(data))
