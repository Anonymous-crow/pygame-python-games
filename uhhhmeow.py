import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import math

screen_x = 1400
screen_y = 800
black = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.mouse.set_visible(0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text, position, size):
    smallText = pygame.font.Font('C:/windows/fonts/times.ttf',size)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = position
    screen.blit(TextSurf, TextRect)

squaresize = 15

exit = 0
while exit == 0:
    for event in pygame.event.get():
              if event.type == pygame.QUIT:  # makes the program mortal
                  exit = 1
                  pygame.quit()
                  exit()

    A_x = pygame.mouse.get_pos()[0] - squaresize
    A_y = pygame.mouse.get_pos()[1] - squaresize
    B_x = pygame.mouse.get_pos()[0] + squaresize
    B_y = pygame.mouse.get_pos()[1] - squaresize
    C_x = pygame.mouse.get_pos()[0] - squaresize
    C_y = pygame.mouse.get_pos()[1] + squaresize
    D_x = pygame.mouse.get_pos()[0] + squaresize
    D_y = pygame.mouse.get_pos()[1] + squaresize

    mouse1 = pygame.mouse.get_pressed()[0]
    mouse2 = pygame.mouse.get_pressed()[2]
    mouse3 = pygame.mouse.get_pressed()[1]

    if mouse1 == 1:
        squaresize = 10
    elif mouse1 == 0:
        squaresize = 15

    pygame.time.wait(10)
    screen.fill((125, 125, 125))
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.polygon(screen, (0, 0, 0), [(A_x, A_y), ((A_x + B_x) / 2, A_y + ((0 - squaresize) * mouse3)), (B_x, B_y), (D_x, D_y), (C_x, C_y)], mouse2)
    message_display(str(mouse_pos),(100,750),15)
    pygame.display.update()
