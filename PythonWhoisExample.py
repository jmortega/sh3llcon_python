# -*- encoding: utf-8 -*-
'''
Notas:
Lib: https://pypi.python.org/pypi/pythonwhois
'''
import pythonwhois
import sys
import socket
import dns
from ipwhois import IPWhois

if len(sys.argv) != 2:
    print "[-] usage python PythonWhoisExample.py <domain_name>"
    sys.exit()

print sys.argv[1]
whois = pythonwhois.get_whois(sys.argv[1])
for key in whois.keys():
    print "[+] %s : %s \n" %(key, whois[key])
	

host = socket.gethostbyname(sys.argv[1])
print host

#whois2 = IPWhois(host).lookup()
#print whois2

addr = dns.reversename.from_address(host)
print addr