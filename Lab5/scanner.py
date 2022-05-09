import socket
import datetime

print(datetime.datetime.now())

from local_machine_info import print_machine_info

print_machine_info()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

inputHost = input("Unesi adresu hosta: ")
print("Skeniranje porta za adresu: ", inputHost)

print("Unesite broj pocetnog i zavrsnog porta.")

startPort = input("Start port=> ")
endPort = input("End port => ")

startPort = int(startPort)
endPort = int(endPort)

def scanner(port):
    try:
        sock.connect((inputHost,port))
        return True
    except:
        return False

for portNumber in range(startPort,endPort):
    print("Skeniranje: ", portNumber)
    if scanner(portNumber):
        print('Port: ',portNumber,'/tcp',' je otvoren')