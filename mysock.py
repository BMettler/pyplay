#!/usr/bin/env python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("google.com",80)) ## so the double parens makes it a tuple
sock.send('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n' )

resp = sock.recv(2048)
sock.close

print resp
## this is too coo 
