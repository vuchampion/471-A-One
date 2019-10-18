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
connectionSocket, addr = serverSocket.accept()
print('Source Address: ' + str(addr))
while True:
    try:
        message = connectionSocket.recv(1024).decode()
        #filename = message.split()[1]
        filename = message
        print('\nRequest: ')
        print(message)

        f = open(filename)
        outputdata = f.read()

        connectionSocket.send("HTTP 200 OK, press ENTER to show contents".encode())
        connectionSocket.send(outputdata.encode())
        #Send the content of the requested file to the client
        #for i in range(0, len(outputdata)):
        #    connectionSocket.send(outputdata[i].encode())
        #connectionSocket.send("\r\n".encode())
        #connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP ERROR 404 NOT FOUND".encode())
        continue

connectionSocket.close()
serverSocket.close()
sys.exit()
