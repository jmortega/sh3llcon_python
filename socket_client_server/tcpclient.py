#!/usr/bin/python
# tcpclient.py
 
import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostport = ("127.0.0.1", 1337)
s.connect(hostport)
s.send("Hello\n")
buf = s.recv(1024)
print "Received", buf