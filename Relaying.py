#!/usr/bin/env python
# coding=utf-8
import socket
import time
import sys

host_relay="192.168.100.41"
port_relay=8080

host="192.168.100.46"
poet=8080

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host.port))

serversock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversock.bind((host_relay.port_relay))
server.listen(10)

print 'Waiting for connection'
clientsock.client_address=serversock.accept()

try:
    while True:
        sock.send("OK")
        response=sock.recv(4096)
        print response

        recvmsg=clientsock.recv(1024)
        print'Received->%s'%(recvmag)

        clientsock.sendall(response)
finally:
    print response
