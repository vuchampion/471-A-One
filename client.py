from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)
clientRequest = str(sys.argv[1])
clientPort = int(sys.argv[3])
serverAddress = str(sys.argv[2])
print('Client socket has been created')

try:
    clientSocket.connect((serverAddress, clientPort))
except:
    print('Could not complete connection')
    sys.exit()
print('Connected with the server')

clientSocket.send(clientRequest.encode())
data = clientSocket.recv(1024).decode()

print('Recieved from server: \n' + data)
print('Connection: close')
clientSocket.close()
