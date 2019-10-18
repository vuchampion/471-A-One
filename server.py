#import socket module
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 80
print('Server socket has been created.')

try:
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
except:
    print('Could not complete bind')
    sys.exit()

print('Ready to serve...')

while True:
    connectionSocket, addr = serverSocket.accept()
    print('Source Address: ' + str(addr))
    try:
        message = connectionSocket.recv(1024)
        #filename = message.split()[1]
        filename = message
        print('\nMessage: ')
        print(message)

        f = open(filename)
        outputdata = f.read()
        print(outputdata)

        connectionSocket.send("\nHTTP 200 OK\n")
        #connectionSocket.send(outputdata)

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        connectionSocket.send("\nHTTP ERROR 404 NOT FOUND\n")

serverSocket.close()
sys.exit()
