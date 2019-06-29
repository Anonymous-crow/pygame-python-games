import pygame
import sys
import random

##initialise pygame
pygame.init()

##screen height and legnth
canvasw = 1000
canvasl = 1000

##snek starting positioin
snake_x = (canvasw/2)
snake_y = (canvasl/2)

##where the snake will move
move_x = 0
move_y = 0

##this makes the screen
screen = pygame.display.set_mode((canvasw, canvasl))
##all of this stuff happens while game_over = false
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if move_x == 5:
                    move_x = 0
                elif move_x != 5:
                    move_x = 5
            elif event.key == pygame.K_LEFT:
                if move_x == -5:
                    move_x = 0
                elif move_x != -5:
                    move_x = -5
            elif event.key == pygame.K_UP:
                if move_y == 5:
                    move_y = 0
                elif move_y != 5:
                    move_y = 5
            elif event.key == pygame.K_DOWN:
                if move_y == -5:
                    move_y = 0
                elif move_y != -5:
                    move_y = -5
        elif event.type != pygame.KEYDOWN:
            snake_x = snake_x + move_x
            snake_y = snake_y + move_y

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 180, 0), (snake_x, snake_y, 100, 100))
    pygame.display.update()
