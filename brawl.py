import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time

hahahaha = False

attack_list = ["swift attack", "heavy attack", "roshambo attack", "almost a shark"]
strategize_list = ["screw you", "thorns", "cursed", "horning"]
recovery_list = ["buffer", "heal up", "investment", "theres no 'L' in stingray"]
concentration_list = ["breathe", "planning", "technique", "drag queen eggs"]

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

P1_strikes = 3 # Max of five
P2_strikes = 3 # Max of five

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

arbitraryinput = input("\nPress enter to begin... \n")

loading()

clear()
print("FIGHT!\n\n")
exit = 0
while exit == 0:
    if Order == "P1":
        nonarbitraryinput = input("\n What first move type do you make? \n ('Attack', 'Strategize', 'Recovery', 'Concentration')\n")
        Order = "P2"
    if Order == "P2":
        nonarbitraryinput = input("\n What first move type do you make? \n ('Attack', 'Strategize', 'Recovery', 'Concentration')\n")
        if nonarbitraryinput == "attack":
            if P2_house == "barracuda":
                nonarbitraryinput = input("\n What first move do you make? \n" + attack_list(0, 3) + "\n")
            elif P2_house != "barracuda":
                nonarbitraryinput = input("\n What first move do you make? \n" + attack_list(0, 2) + "\n")
        elif nonarbitraryinput == "strategize":
            if P2_house == "narwhal":
                nonarbitraryinput = input("\n What first move do you make? \n" + strategize_list(0, 3) + "\n")
            elif P2_house != "narwhal":
                nonarbitraryinput = input("\n What first move do you make? \n" + strategize_list(0, 2) + "\n")
        elif nonarbitraryinput == "recovery":
            if P2_house == "stingray":
                nonarbitraryinput = input("\n What first move do you make? \n" + recovery_list(0, 3) + "\n")
            elif P2_house != "stingray":
                nonarbitraryinput = input("\n What first move do you make? \n" + recovery_list(0, 2) + "\n")
        elif nonarbitraryinput == "concentration":
            if P2_house == "sea dragon":
                nonarbitraryinput = input("\n What first move do you make? \n" + concentration_list(0, 3) + "\n")
            elif P2_house != "sea dragon":
                nonarbitraryinput = input("\n What first move do you make? \n" + concentration_lis(0, 2) + "\n")
        elif nonarbitraryinput == "secret fifth move":
            hahahaha = True
            while hahahaha:
                print("hahahahahahahahahaha very funny")
        nonarbitraryinput = input("\n What second move type do you make? \n ('Attack', 'Strategize', 'Recovery', 'Concentration')\n")
        if nonarbitraryinput == "attack":
            if P2_house == "barracuda":
                nonarbitraryinput = input("\n What second move do you make? \n" + attack_list(0, 3) + "\n")
            elif P2_house != "barracuda":
                nonarbitraryinput = input("\n What second move do you make? \n" + attack_list(0, 2) + "\n")
        elif nonarbitraryinput == "strategize":
            if P2_house == "narwhal":
                nonarbitraryinput = input("\n What second move do you make? \n" + strategize_list(0, 3) + "\n")
            elif P2_house != "narwhal":
                nonarbitraryinput = input("\n What second move do you make? \n" + strategize_list(0, 2) + "\n")
        elif nonarbitraryinput == "recovery":
            if P2_house == "stingray":
                nonarbitraryinput = input("\n What second move do you make? \n" + recovery_list(0, 3) + "\n")
            elif P2_house != "stingray":
                nonarbitraryinput = input("\n What second move do you make? \n" + recovery_list(0, 2) + "\n")
        elif nonarbitraryinput == "concentration":
            if P2_house == "sea dragon":
                nonarbitraryinput = input("\n What second move do you make? \n" + concentration_list(0, 3) + "\n")
            elif P2_house != "sea dragon":
                nonarbitraryinput = input("\n What second move do you make? \n" + concentration_list(0, 2) + "\n")
        elif nonarbitraryinput == "secret fifth move":
            hahahaha = True
            while hahahaha:
                print("hahahahahahahahahaha very funny")
        Order = "P1"
