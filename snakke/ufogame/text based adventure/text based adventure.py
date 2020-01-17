import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def loading():
    clear()
    print("loading")
    time.sleep(.2)
    clear()
    print("loading.")
    time.sleep(.2)
    clear()
    print("loading..")
    time.sleep(.2)
    clear()
    print("loading...")
    time.sleep(.2)
    clear()
    print("loading....")
    time.sleep(.2)
    clear()
    print("loading.....")
    time.sleep(.2)
    clear()
    print("loading......")
    time.sleep(.2)
    clear()
    print("loading.......")
    time.sleep(.2)
    clear()
    print("loading........")
    time.sleep(.2)
    clear()
    print("loading.........")
    time.sleep(.2)
    clear()

P1_house = "unhoused"
P2_house = "unhoused"
P1_chance = 10
P2_chance = 10
Order = "P0"

print("ECHS BRAWL \n By Jonathan Binns \n And Jake Nellesen")
print("\n \n PLAYER ONE")
print("\n Enter your house: ")
P1_house = input("('Stingray', 'Narwhal', 'Sea Dragon', 'Barracuda')\n")
print("\n \n PLAYER TWO")
print("\n Enter your house: ")
P2_house = input("('Stingray', 'Narwhal', 'Sea Dragon', 'Barracuda')\n")

print("\n Determining turn order...")
pygame.time.wait(50) #haha hahahaha as if it would take any time to process
while P1_chance == P2_chance:
    P1_chance = random.randint(1, 10)
    P2_chance = random.randint(1, 10)
if P1_chance >= P2_chance:
    Order = "P1"
    print("\n PLAYER ONE GOES FIRST")
if P1_chance <= P2_chance:
    Order = "P2"
    print("\n PLAYER TWO GOES FIRST")

arbitraryinput = input("\npress enter to begin... \n")

loading()

clear()
print("FIGHT!\n\n")
exit = 0
while exit == 0:
    if Order == "P1":
        print("nothing you do matters yet hahah")
        Order = "P2"
    if Order == "P2":
        print("nothing you do matters yet ahaha")
        Order = "P1"
