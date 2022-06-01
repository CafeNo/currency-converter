import socket
from http import server
 
HOST = 'localhost'
PORT = 3000
 
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

word = []
word.append(first_currency.get())
word.append(second_currency.get())
word.append(amount.get())

server.connect((HOST, PORT))
server.send(word.encode('utf-8'))
data_server = server.recv(1024).decode('utf-8')

server.close()