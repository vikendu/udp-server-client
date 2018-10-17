import socket  
from _thread import *
import threading 
  
print_lock = threading.Lock() 
def threaded(c): 
    data = ''
    buf = b''
    while True: 
        data = str(c.recv(1024).decode('ascii')) 
        if not data: 
            print('Bye') 
            print_lock.release() 
            break
        num = int(data)
        num *= num
        data = str(num)
        #buf += data
        #data = data[::-1] 

        c.send(data.encode('ascii')) 
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
    port = 12358
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
  
    s.listen(5) 
    print("socket is listening") 
   
    while True: 
        c, addr = s.accept() 

        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 

        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 