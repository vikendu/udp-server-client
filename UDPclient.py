import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
Message = ""

while(True):
	print('enter no to be squared:')
	input_msg = input("")
	Message = input_msg.encode('ascii')
	if(input_msg == 'q'):
		break

	clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
	data, server = clientSock.recvfrom(1024)
	print(data.decode('ascii'))

