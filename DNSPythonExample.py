# -*- encoding: utf-8 -*-
import dns
import dns.resolver
import dns.query 
import dns.zone 

'''ansA,ansMX,ansNS,ansAAAA=(dns.resolver.query('www.google.com','A'),
                          dns.resolver.query('www.google.com','MX'),
                          dns.resolver.query('www.google.com', 'NS'), 
                          dns.resolver.query('www.google.com', 'AAAA'))
print ansA.response.to_text() 
print ansMX.response.to_text()
print ansNS.response.to_text()
print ansAAAA.response.to_text()'''

ansA=(dns.resolver.query('www.sh3llcon.es','A'))
print ansA.response.to_text()
ansMX=(dns.resolver.query('www.sh3llcon.es','MX'))
print ansMX.response.to_text() 
ansNS=(dns.resolver.query('www.sh3llcon.es','NS'))
print ansNS.response.to_text() 
ansAAAA=(dns.resolver.query('www.sh3llcon.es','AAAA'))
print ansAAAA.response.to_text()

