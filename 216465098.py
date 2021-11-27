# first the client and server need to handshake and establish tcp connection 
# when creating TCP connection we associate it with the client socket address (IP address and port number)
#   -> find out how to get client/host socket address, do same for www.google.com (or the web address user enters)
# when client creates its TCP socket, it specifies the address of the welcoming socket in the server (IP address of server host and port number of the socket)
# after this, client then initiates three-way handshake and etablishes TCP connection with the server 

# serverSocket is the socket created by the server that is dedicated to the client specifically (initial point of contact for all clients wanting to 
#                                                                                                communicate with the server) 
# connectionSocket is the newly creted socket dedicated to the client making the connection (each connection socket is subsequently created for communicating 
#                                                                                               with each client)

import socket 
webAddress = input('Enter a web address and press Enter: ')
serverName = socket.gethostbyname(webAddress)
# print('IP address of '+webAddress+' is '+serverName)
serverPort = 80
# create client socket (param1: using IPv4; param2: socket type TCP)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
request = "GET / HTTP/1.1\r\n\r\nHost:%s\r\n\r\n" % webAddress
clientSocket.send(request.encode())
print('Your webpage content is:')
print(clientSocket.recv(4096))
clientSocket.close() 