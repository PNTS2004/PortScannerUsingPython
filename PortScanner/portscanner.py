import socket
from IPy import IP

def scan(target):
    converted_ip=check_ip(target)
    print('\n', 'Scanning Ports:-')
    for port in range(a,b+1):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress,port):
    try:
        sock=socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
         banner=get_banner(sock)
         print('Port '+str(port)+' is Open. Service running: '+str(banner))
        except:
            print('Port ' + str(port) + ' is Open.')
    except:
        print('No Open Ports found.')

def get_banner(s):
    return s.recv(1024)

targets = input('Enter the Target/s IP (split different targets using ,): ')
a = int(input('Enter the starting port of the range: '))
b = int(input('Enter the sending port of the range: '))

if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip())
else:
    scan(targets)
