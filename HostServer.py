#handling errors in python socket programs, THIS IS THE CLIENT FILE
# Command: hostname -I : returns Pi IP address

import socket   #for sockets
import sys  #for exit
import HtmlChangeTemplatecopy as html

##############################################
### this needs to be the same on both ends ###
### and the ip address should be which	   ###
### ever machine has the server code	   ###
##############################################

def Main():
#	host = '172.16.204.168'
	host='172.16.204.69'
	port = 5000
	
	s= socket.socket()
	s.bind((host,port))
	
	s.listen(1)
	c, addr = s.accept()
	print "Connection from:	" + str(addr)
	
	try:
		while True:
			data = c.recv(1024)
			if not data:
				break
			
			room_start=0
			room_end=data.find(":")
			status_start=room_end + 1
			room=data[room_start:room_end]
			status=data[status_start]
			html.unit_Status(room,status)			
			print 'data received'
		c.close()
		print "Connection Closed"
	except:
		c.close()
		print "Connection Closed"
	
if __name__=='__main__':
	Main()
	
	
	
	
	
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip

##############################################
### I may need to send the 3 sensor 	   ###
### variables separately through this 	   ###
### method								   ###
##############################################



#################################
#### GENERAL SOCKET METHODS  ####
#################################
# object.recv()		-	this method receives TCP message
# object.send()		-	this method transmits TCP message
# object.recvfrom()		-	this method receives UDP message
# object.sendto()		-	this method transmits UDP message
# object.close()		-	this method closes socket
# socket.gethostname()		-	returns the hostname
#
#
# object.bind()		-		this method binds address (hostname, port number pair) to socket
# object.listen()		-	this method sets up and start TCP listener
# object.accept()		-	the passively accept TCP client connection, waiting until connection arrives (blocking)
#
#
# HTTP port 80 Modules: httplib, urllib, xmlrpclib	-	web pages
# FTP port 20 Modules: ftplib, urllib	-	file transfers
# telnet port 23 Modules: telnetlib	-	command lines


def Main():
	host = '172.16.204.168'
	port = 5000
	
	s= socket.socket()
	s.bind((host,port))
	
	s.listen(1)
	c, addr = s.accept()
	print "Connection from:	" + str(addr)
	try:
		while True:
			data = c.recv(1024)
			if not data:
				break

			room_start=1
			room_end=data.find("]")
			action_start=room_end + 1
			action_stop=data.find(":")
			room=data[room_start:room_end]
			action=data[action_start:action_stop]
			input=data[-1]
		
			what_to_return={"Room":room,"Action":action,"Input":input}
			for item in what_to_return:
				print "sending:	" + str(item) + ":	"+ str(what_to_return[item])
				data=what_to_return[item]
				c.send(data)
		c.close()
		print "Connection Closed"
	except:
		c.close()
		print "Connection Closed"
	
if __name__=='__main__':
	Main()
	
	
	

