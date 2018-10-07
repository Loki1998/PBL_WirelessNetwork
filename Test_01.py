#!/usr/bin/env python
# coding=utf-8
#The host is the next node
#And the host_relay is the node itself
#We use this way to name all the variables
import socket
import time
import sys

#The next node ip
host="192.168.100.41"           
port=8080

#This node ip
host_relay="10.206.38.117"
port_relay=8080

serversock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversock.bind((host_relay,port_relay))
serversock.listen(10)

print 'Waiting for connection to client 192.168.100.00'
connection,address=serversock.accept()

clientsock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsock.connect((host,port))

try:
    while True:
        serversock.send("OK")
        response=connection.recv(4096)
        print response

        recvmsg=clientsock.recv(1024)
        print'Received->%s'%(recvmag)

        clientsock.sendall(response)
finally:
    print 'END'
