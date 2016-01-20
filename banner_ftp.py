import ftplib
import sys
import socket

def scan(ip_host):
         
	try:
		users=["anonymous","anonymous"+"@"+ip_host]
		passwords=["guest","anonymous","","anonymous"+"@"+ip_host]
		
		print "[*]IP "+ ip_host
		print "[*]Port "+ str("21")+ "\n"

		for user in users:
			for password in passwords:
				try:
					print "[*] Trying to connect"
					connect=ftplib.FTP(ip_host)
					response=connect.login(user,password)
					print response
					if "230" in response:
						print "Anonymous login allowed"
						print "User:",user
						print "Password:",password
					else:
						print "Anonymous login disallowed with credentials User: " +user + " Password:" + password

				except ftplib.error_perm:
					print "Cant Brute Force with user"+user+ "and password "+password
					connect.close

		socket.setdefaulttimeout(2)
		s=socket.socket()
		try:
			s.connect((ip_host,21))
			ans_socket = s.recv(1024)
			print "\n[*]FTP Banner"+  ans_socket
			s.close()
		except(socket.error):
			print "Error"

	except(KeyboardInterrupt):
		print "Interrupted!"
		sys.exit() 		 	 		 

ip=raw_input("Introduce IP:")
scan(ip)
