#Author: Abheek Gulati
#This TCP Server can handle two connections

import socket 

TCP_IP = '127.0.1.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(2)

conn1, addr1 = s.accept()
print 'Connection address: ', addr1
while 1:
	data1 = conn1.recv(BUFFER_SIZE)
	if not data1: break
	print "recieved data: ", data1
	data1 = data1.upper()
	conn1.send(data1)
conn1.close()

conn2, addr2 = s.accept()
print 'Connection address: ', addr2
while 2:
	data2 = conn2.recv(BUFFER_SIZE)
	if not data2: break
	print "recieved data: ", data2
	data2 = data2.upper()
	conn2.send(data2)
conn2.close()