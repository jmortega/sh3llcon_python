#!/usr/bin/python
# tcpserver.py
 
import socket

host = 'localhost'
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1337
sock.bind((host, port))

sock.listen(10)
print 'Listening in port '+str(port)

while 1:
        cli,addr = sock.accept()
        print "Connection from", addr
        buf = cli.recv(1024)
        print "Received", buf
        if buf == "Hello\n":
                cli.send("Server ID 1\n")
        cli.close()