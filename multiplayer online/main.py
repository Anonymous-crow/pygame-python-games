import socket
import time
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

servermode = 0

lhost = 'sashimi.port0.org'
port = 6969

canvas_x = 1400
canvas_y = 800

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def message_display(text, position, size):
    smallText = pygame.font.Font('C:/windows/fonts/times.ttf',size)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = position
    screen.blit(TextSurf, TextRect)

def loop_legality():
    pygame.display.flip()
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # makes the loop mortal
            start = 0
            sys.exit()

def client_send(msg):
    s.send(msg.encode("UTF-8"))

def server_input(msgsnd):
    msgsnd = msgsnd.encode("UTF-8")
    clientsocket.send(msgsnd)
    msgrcv = clientsocket.recv(4096)
    msgrcv = msgrcv.decode("UTF-8")
    return msgrcv

def server_send(msgsnd):
    msgsnd = msgsnd.encode("UTF-8")
    clientsocket.send(msgsnd)



hostcliundefined = True
while hostcliundefined:
    ans = input("\nAre you the host or the client?\n1: host\n2: client\n\n" )
    if int(ans) == 1:
        hostcliundefined = False
        servermode = 1
    if int(ans) == 2:
        hostcliundefined = False
        servermode = 2

if servermode == 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    remote_ip = socket.gethostbyname( host )
    clear()
    ans = input("\nEnter Port(enter 0 for default):\n\n" )
    if ans != "0":
        port = int(ans)
    s.bind(('0.0.0.0', port))
    clear()
    print("hosting on " + remote_ip + " on port " + str(port))
    s.listen(1)
    clientsocket, addr = s.accept()
    print("Connection from: " + str(addr))
    msgrcv = server_input("ipreq")
    forign_host , forign_ip = msgrcv.split(',', 1)
    print("host name of the connector is " + forign_host + ", and ip of connector is " + forign_ip)
    pygame.init()
    screen = pygame.display.set_mode((canvas_x, canvas_y))
    screen.fill((255, 255, 255))
    start = 1
    while start == 1:
        loop_legality()
        mouse_pos = pygame.mouse.get_pos()
        message_display("made by Jonny B. and Jake N.",(125, 750),15)
        message_display("host",(canvas_x/2, 20),15)
        mouse1 = pygame.mouse.get_pressed()[0]
        mouse2 = pygame.mouse.get_pressed()[2]
        mouse3 = pygame.mouse.get_pressed()[1]
        server_send("%s,%s,%s,%s"% (mouse1, mouse2, mouse3, mouse_pos))



if servermode == 2:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clear()
    ans = input("\nEnter ip adress(enter 0 for default):\n\n" )
    if ans != "0":
        port = lhost
    host = socket.gethostbyname(lhost)
    lip = socket.gethostname()
    remote_ip = socket.gethostbyname( lip )
    port = 1235
    clear()
    ans = input("\nEnter Port(enter 0 for default):\n\n" )
    if ans != "0":
        port = int(ans)
    clear()
    print("connecting")
    connected = False
    while connected == False:
        try:
            s.connect((host, port))
            clear()
            print('Socket Connected to ' + lhost + ' on ip ' + host)
            connected = True
        except:
            sleepTime = random.randint(1, 2)
            time.sleep(sleepTime)
            print("error: timed out, retrying")
        msg = s.recv(4096)
        inst = msg.decode("UTF-8")
        if inst == "ipreq":
            client_send("%s,%s"% (lip, remote_ip))
    pygame.init()
    screen = pygame.display.set_mode((canvas_x, canvas_y))
    screen.fill((255, 255, 255))
    start = 1
    while start == 1: #bigger loop that will contain everything, an embedded while loop will be the game
        loop_legality()
        mouse_pos = pygame.mouse.get_pos()
        message_display("made by Jonny B. and Jake N.",(125, 750),15)
        message_display("client",(canvas_x/2, 20),15)
        msg = s.recv(10)
        maus = msg.decode("UTF-8")
        maus = maus.split(',', 3)
        mouse1,mouse2,mouse3,mouse_pos = maus
        print("%s\n\n"%(mouse_pos))
        pygame.draw.rect(screen, (0, 0, 0), (canvas_x/2, canvas_y/2, 30, 30))
