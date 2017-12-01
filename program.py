#Andre Le
#CSE 283 - Section A
#Date: October 15 - 2017
#Assignment: Project 1 - Web Server

#import socket module
from socket import *
import sys # In order to terminate the program
import thread

ip = ''
port_number = 1234

def proxy_thread(connectionSocket, addr):
	try:
		#Client send request (message) to proxy
		message = connectionSocket.recv(1024) #Data from the socket, up to 1kB
       	
		# parse the first line
		first_line = message.split('n')[0]

		# get url
		url = first_line.split(' ')[1]
		print "URL:", url
       	
       	# find the webserver and port
		http_pos = url.find("://")          # find pos of ://
		if (http_pos==-1):
			temp = url
  		else:
			temp = url[(http_pos+3):]       # get the rest of url

		port_pos = temp.find(":")           # find the port pos (if any)

		# find end of web server
		webserver_pos = temp.find("/")
		if webserver_pos == -1:
			webserver_pos = len(temp)

		webserver = ""
		port = -1
		if (port_pos==-1 or webserver_pos < port_pos):      # default port
			port = 80
			webserver = temp[:webserver_pos]
		else:       # specific port
			port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
			webserver = temp[:port_pos]

		print "Connect to:", webserver, port

		#Proxy to server
    	# create a socket to connect to the web server
		s = socket(AF_INET, SOCK_STREAM)
		s.connect((webserver, port))
		s.send(message)         # send request to webserver

		while True:
		# proxy receive data from web server
			data = s.recv(1024)
			print "Data: ", data

			if (len(data) > 0):
	        	# send to browser
				connectionSocket.send(data)
			else:
				break
		s.close()
		connectionSocket.close()
	        
	except IOError:
	    #Send response message for file not found
		connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n')
		print 'error in sending'
	   	
	    #Close client socket
		connectionSocket.close()

def main():

	serverSocket = socket(AF_INET, SOCK_STREAM)
	#Prepare a server socket
	serverSocket.bind((ip, port_number))
	serverSocket.listen(5)

	while True:
    	#Establish the connection
		print('Ready to serve...')
		connectionSocket, addr = serverSocket.accept()  #the client socket
    	
    	# create a thread to handle request
		thread.start_new_thread(proxy_thread, (connectionSocket, addr))
	connectionSocket.close()

	serverSocket.close()
	sys.exit()#Terminate the program after sending the corresponding data

if __name__ == '__main__':
	main()