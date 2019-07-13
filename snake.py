import pygame
import sys
import random

##initialise pygame
pygame.init()

##screen height and legnth
canvasw = 1400
canvasl = 700

##snake starting position
snake_x = (canvasw/2)
snake_y = (canvasl/2)

##where the snake will move
move_x = 0
move_y = 0
speed = 1
snake_size = 50

##this makes the screen
screen = pygame.display.set_mode((canvasw, canvasl))

screen.fill((0, 0, 0))
myrect = pygame.draw.rect(screen, (0, 180, 0), (canvasw/2, canvasl/2, snake_size, snake_size))
##myrect = myrect.move(0,0)
pygame.display.update()
##all of this stuff happens while game_over = false
game_over = False
while not game_over:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:  ##makes the program mortal
           sys.exit()
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
               if move_x == speed:
                   move_x = 0
                   move_y = 0
               elif move_x != speed:
                   move_x = speed
                   move_y = 0
           elif event.key == pygame.K_LEFT:
               if move_x == -speed:
                   move_x = 0
               elif move_x != -speed:
                   move_x = -speed
                   move_y = 0
           elif event.key == pygame.K_UP:
               if move_y == -speed:
                   move_y = 0
                   move_x = 0
               elif move_y != -speed:
                   move_y = -speed
                   move_x = 0
           elif event.key == pygame.K_DOWN:
               if move_y == speed:
                   move_y = 0
                   move_x = 0
               elif move_y != speed:
                   move_y = speed
                   move_x = 0
   pygame.draw.rect(screen, (0, 180, 0), (snake_x, snake_y, snake_size, snake_size))
   ##pygame.myrect.move(move_x,move_y)
   pygame.display.update()
   snake_x = snake_x + move_x
   snake_y = snake_y + move_y

   if snake_x >= canvasw - snake_size + speed:
       snake_x = canvasw - snake_size
   elif snake_x <= -speed:
       snake_x = 0

   if snake_y >= canvasl - snake_size + speed:
       snake_y = canvasl - snake_size
   elif snake_y <= -speed:
       snake_y = 0
