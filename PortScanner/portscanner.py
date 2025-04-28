import socket
from IPy import IP

ipaddress=input('Enter the Target IP: ')
port=int(input('Enter the Port to be scanned: '))

try:
    sock=socket.socket()
    sock.connect((ipaddress, port))
    print('Port '+str(port)+' is Open, Congratulations!')
except:
    print('Port '+str(port)+' is Closed. Better luck next time.')
