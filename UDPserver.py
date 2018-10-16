import socket
from _thread import *
import threading 
# Here we define the UDP IP address as well as the port number that we have 
# already defined in the client python script.
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

print_lock = threading.Lock()
print_lock.acquire()

while True:
    data, addr = serverSock.recvfrom(1024)
    data_int = int(data)
    data_int *= data_int
    data = str(data_int)
    sent = serverSock.sendto(data.encode('ascii'), addr)
    print("Squared Output: ", str(data_int))

print_lock.release()