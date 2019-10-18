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
#connectionSocket, addr = serverSocket.accept()
while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        print('Source Address: ' + str(addr))
        message = connectionSocket.recv(1024).decode()
        #filename = message.split()[1]
        filename = message
        print('\nRequest: ')
        print(message)

        f = open(filename)
        outputdata = f.read()

        connectionSocket.send(b'HTTP 200 OK ' + outputdata.encode())
        connectionSocket.close() #THIS IS GOOD
    except IOError:
        connectionSocket.send("HTTP ERROR 404 NOT FOUND".encode())
        connectionSocket.close()
        #continue

#connectionSocket.close()
serverSocket.close()
sys.exit()
