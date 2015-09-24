import socket

def Main(message):
	host = '172.16.204.168'
	port = 5000
	
	s = socket.socket()
	s.connect((host, port))
	
	
	s.send(message)
	s.close()



##############################################
### This is what will be in the sensors    ###
##############################################