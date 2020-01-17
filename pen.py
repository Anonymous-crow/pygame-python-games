import sys
import pygame
import random
import math

screen_x = 1400
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.mouse.set_visible(0)

width = 0

X = 0
Y = 0

Current_x = [X]
Current_y = [Y]

Pen_x = 0
Pen_y = 0

Yspeed = 0
Xspeed = 0
Spinspeed = 0

Wpressed = 0
Spressed = 0
Apressed = 0
Dpressed = 0

red = 0
green = 0
blue = 0

PenDown = 0

circle_radius = 20
circle_angle = 0
exit = 0
while exit == 0:
     for event in pygame.event.get():
             if event.type == pygame.QUIT:  # makes the program mortal
                 exit = 1
                 sys.exit()

             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_s:
                     Yspeed = -5
                     Spinspeed = 1
                     Spressed = 1
                 if event.key == pygame.K_w:
                     Yspeed = 5
                     Spinspeed = -1
                     Wpressed = 1
                 if event.key == pygame.K_d:
                     Xspeed = -5
                     Spinspeed = 1
                     Dpressed = 1
                 if event.key == pygame.K_a:
                     Xspeed = 5
                     Spinspeed = -1
                     Apressed = 1
                 if event.key == pygame.K_SPACE:
                     PenDown = 1

             elif event.type == pygame.KEYUP:
                 if event.key == pygame.K_s:
                     Spressed = 0
                 if event.key == pygame.K_w:
                     Wpressed = 0
                 if event.key == pygame.K_d:
                     Dpressed = 0
                 if event.key == pygame.K_a:
                     Apressed = 0
                 if event.key == pygame.K_SPACE:
                     PenDown = 0

     A_x = circle_radius*math.cos(circle_angle + 0.25*math.pi) + screen_x/2
     A_y = circle_radius*math.sin(circle_angle + 0.25*math.pi) + screen_y/2
     B_x = circle_radius*math.cos(circle_angle + 0.75*math.pi) + screen_x/2
     B_y = circle_radius*math.sin(circle_angle + 0.75*math.pi) + screen_y/2
     C_x = circle_radius*math.cos(circle_angle + 1.75*math.pi) + screen_x/2
     C_y = circle_radius*math.sin(circle_angle + 1.75*math.pi) + screen_y/2
     D_x = circle_radius*math.cos(circle_angle + 1.25*math.pi) + screen_x/2
     D_y = circle_radius*math.sin(circle_angle + 1.25*math.pi) + screen_y/2

     midpoint_x = ((A_x + B_x + C_x + D_x)/4)
     midpoint_y = ((A_y + B_y + C_y + D_y)/4)

     mouse1 = pygame.mouse.get_pressed()[0]
     mouse2 = pygame.mouse.get_pressed()[2]
     mouse3 = pygame.mouse.get_pressed()[1]

     pygame.time.wait(10)

     Current_x.append(X*-1 + midpoint_x - 4)
     Current_y.append(Y + midpoint_y*-1 + 2)

     Y = Y + Yspeed
     X = X + Xspeed
     circle_angle = circle_angle + Spinspeed*0.2
     if Apressed == 0 and Dpressed == 0:
         Xspeed = Xspeed*0.95
     if Wpressed == 0 and Spressed == 0:
         Yspeed = Yspeed*0.95
     if Apressed == 0 and Dpressed == 0 and Wpressed == 0 and Spressed == 0:
         Spinspeed = Spinspeed*0.95



     pygame.draw.rect(screen, (0, 0, 0), (X, Y, 30, 30)) # black
     if midpoint_x >= (X + 0) and midpoint_x <= (X + 30) and midpoint_y >= (Y + 0) and midpoint_y <= (Y + 30):
         red = 0
         green = 0
         blue = 0
         width = 0

     pygame.draw.rect(screen, (0, 0, 255), (X + 90, Y + 90, 30, 30)) # blue
     if midpoint_x >= (X + 0 + 90) and midpoint_x <= (X + 30 + 90) and midpoint_y >= (Y + 0 + 90) and midpoint_y <= (Y + 30 + 90):
         red = 0
         green = 0
         blue = 255
         width = 0

     color = (red, green, blue)
     if PenDown == 1:
         Pen_x = Current_x[len(Current_x) - 1]
         Pen_y = Current_y[len(Current_y) - 1]

     pygame.draw.rect(screen, color, (Pen_x + X, Y - Pen_y, 10, 10))
     pygame.draw.polygon(screen, color, [(A_x, A_y), (B_x, B_y), (D_x, D_y), (C_x, C_y)], width)
     pygame.display.update()
     screen.fill((255, 255, 255))
