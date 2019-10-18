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
    try:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()
        filename = message
        print('\nGET: ' + message + ' HTTP/1.1')
        print('Host: ' + str(addr) + '\n')

        f = open(filename)
        outputdata = f.read()

        connectionSocket.send(b'HTTP/1.1 200 OK ' + outputdata.encode())
        print('Connection: close')
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP ERROR 404 NOT FOUND".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
