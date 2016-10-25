#Luan Truong 87855795
#David Loi Diep 17047521

from socket import *
import sys

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
file_name = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = 'GET /' + file_name
clientSocket.send(message.encode())
header = clientSocket.recv(1024).decode()
messageRecv = clientSocket.recv(1024).decode()
finalMessage = ''
while messageRecv:
    finalMessage += messageRecv
    messageRecv = clientSocket.recv(1024).decode()
           
print(finalMessage)
clientSocket.close()
