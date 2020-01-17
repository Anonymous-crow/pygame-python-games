
import pygame
import sys
import random

canvas_x = 1400
canvas_y = 800

screen = pygame.display.set_mode((canvas_x, canvas_y))
screen.fill((0, 0, 0))

# JM = JumpMan
JM_x = canvas_x/4
JM_y = canvas_y/4*3
JM_size = 25

JM_yspeed = 0

JM_Grounded = 0
JM_Gravity = 0

Pipe_x = canvas_x
Pipe_y = canvas_y/2

LeftPressed = 0
RightPressed = 0
UpPressed = 0

GamePaused = 1

exit = 0
while exit == 0:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:  # makes the program mortal
          exit = 1
          sys.exit()

   if event.type == pygame.KEYDOWN:
       GamePaused = 0
       if event.key == pygame.K_SPACE:
           if JM_Grounded == 1:
               JM_yspeed = -15
               UpPressed = 1

   if event.type == pygame.KEYUP:
       if event.key == pygame.K_SPACE:
           UpPressed = 0

   if LeftPressed == 0 and RightPressed == 0:
       JM_xspeed = 0

   if JM_y < canvas_y/4*3:
       JM_Grounded = 0
       if UpPressed == 1:
           JM_Gravity = JM_Gravity + 0.25
       elif UpPressed == 0:
           JM_Gravity = JM_Gravity + 0.75
   elif JM_y >= canvas_y/4*3:
       JM_Grounded = 1
       JM_Gravity = 0
       JM_y = canvas_y/4*3
       if UpPressed == 0:
           JM_yspeed = 0

   if GamePaused == 0:
      Pipe_x = Pipe_x - 7
      if Pipe_x <= 0 - JM_size*4:
          Pipe_x = canvas_x
          Pipe_y = random.randint(-100 , 50) + canvas_y/2

   if JM_x > Pipe_x and JM_x < Pipe_x + JM_size*4:
       if JM_y + JM_size > Pipe_y or JM_y < Pipe_y - JM_size*4:
           exit = 1
           sys.exit()

   JM_y = JM_y + JM_yspeed + JM_Gravity
   pygame.time.wait(7)

   screen.fill((0, 0, 0))
   pygame.draw.rect(screen, (150, 100, 25), (Pipe_x, Pipe_y - JM_size*4 - canvas_y/2, JM_size*4, canvas_y/2))
   pygame.draw.rect(screen, (150, 100, 25), (Pipe_x, Pipe_y, JM_size*4, canvas_y/2))
   pygame.draw.rect(screen, (25, 50, 75), (0, canvas_y/4*3+JM_size, canvas_x, canvas_y/4))
   pygame.draw.rect(screen, (200, 200, 200), (JM_x, JM_y, JM_size, JM_size))
   pygame.display.update()
