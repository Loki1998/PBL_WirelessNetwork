#!/usr/bin/env python
# coding=utf-8
import socket
import RPi.GPIO as GPIO
import time 
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

try:
    while True:
        host="192.168.100.xx"
        port=8080

        socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connet((host,port))
        sock.send("From Rx 192.168.100.xx: please message(1 or 2 or 3 or 4)")

        response=sock.recv(4096)
        print response

        if response == '1':
            GPIO.output(12,True)
            GPIO.output(13,False)
            GPIO.output(18,True)
            GPIO.output(19,False)
            print 'forward'
            time.sleep(0.5)
        elif response == '2':
            GPIO.output(12,True)
            GPIO.output(13,True)
            GPIO.output(18,True)
            GPIO.output(19,False)
            print 'turn right'
            time.sleep(0.5)
        elif response == '3':
            GPIO.output(12,True)
            GPIO.output(13,False)
            GPIO.output(18,True)
            GPIO.output(19,True)
            print 'turn left'
            time.sleep(0.5)
        elif response == '4':
            GPIO.output(12,False)
            GPIO.output(13,True)
            GPIO.output(18,False)
            GPIO.output(19,True)
            print 'backward'
            time.sleep(0.5)
        elif response == '5':
            GPIO.output(12,False)
            GPIO.output(13,True)
            GPIO.output(18,True)
            GPIO.output(19,False)
            print 'turn right plus'
            time.sleep(0.5)
        elif response == '6':
            GPIO.output(12,True)
            GPIO.output(13,False)
            GPIO.output(18,False)
            GPIO.output(19,True)
            print 'turn left plus'
            time.sleep(0.5)
        else:
            GPIO.output(12,False)
            GPIO.output(13,False)
            GPIO.output(18,False)
            GPIO.output(19,False)
            print 'stop'
            time.sleep(0.5)
finally:
    GPIO.cleanup()

