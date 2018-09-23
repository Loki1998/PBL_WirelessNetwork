#!/usr/bin/env python
# coding=utf-8
import socket

host="192.168.100.xx"
port=8080

while True:
    serversock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    serversock.bind((host,port))
    server.listen(10)

    print 'Waitting for connections ...'
    clientsock.client_address=serversock.accept()

    recvmsg=clientsock.recv(1024)
    print 'Received -> %s'%(recvmsg)

    print 'Type command for Rx'
    s_msg=raw_input()

    clientsock.sendall(s_msg)
clientsock.close()

