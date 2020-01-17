import pygame
import sys

##initialise pygame
pygame.init()

##screen height and legnth
canvasw = 960
canvasl = 720

##init ufo position
ufo_x = (canvasw/2) - 50
ufo_y = (canvasl/2) - 25 - 60

turn = 0
##import ufo
ufo_sprite = pygame.image.load('ufo_purple.png')

screen = pygame.display.set_mode((canvasw, canvasl))
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ufo_x += 5
            elif event.key == pygame.K_LEFT:
                ufo_x -= 5
            elif event.key == pygame.K_UP:
                ufo_y -= 5
            elif event.key == pygame.K_DOWN:
                ufo_y += 5
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 180, 0), (ufo_x, ufo_y, 100, 50))
    pygame.display.update()
