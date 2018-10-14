import socket 
def Main(): 
    host = '127.0.0.1'
  
    port = 12358
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 

    num = 4
    sep = ''
  
    message = str(num)
    while True: 
  
        # message sent to server 
        s.send(message.encode('ascii')) 
  
        # messaga received from server 
        data = s.recv(1024) 
        print('Received from the server :',str(data.decode('ascii'))) 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    s.close() 
if __name__ == '__main__': 
    Main() 
