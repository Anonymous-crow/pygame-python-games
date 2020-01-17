import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import math

pygame.display.set_caption('battle squares')

screen_x = 1400
screen_y = 800
Yspeed = 0
Xspeed = 0
width = 5

pos_x = screen_x/4
pos_y = screen_y/2

pos2_x = (screen_x*3)/4
pos2_y = screen_y/2

move_x = 0
move_y = 0
move2_x = 0
move2_y = 0
speed = 2

Spinspeed = 0
Spinspeed2 = 0

Apressed = 0
Dpressed = 0
Wpressed = 0
Spressed = 0
right_pressed = 0
left_pressed = 0
up_pressed = 0
down_pressed = 0

centre_size = 4
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

def player_1_win():
    font = pygame.font.Font('times-new-roman.ttf', 32)
    text = font.render('player 1 win', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    display_surface.blit(text, textRect)

def player_2_win():
    font = pygame.font.Font('times-new-roman.ttf', 32)
    text = font.render('player 2 win', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    display_surface.blit(text, textRect)


circle_radius = 20
circle_angle = 0
circle_angle2 = 0
screen = pygame.display.set_mode((screen_x, screen_y))
go = True
while go:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:  # makes the program mortal
                exit = 1
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    Spressed = 1
                    Spinspeed = -1
                    move_y = speed
                if event.key == pygame.K_w:
                    Wpressed = 1
                    Spinspeed = 1
                    move_y = -speed
                if event.key == pygame.K_d:
                    Dpressed = 1
                    Spinspeed = 1
                    move_x = speed
                if event.key == pygame.K_a:
                    Apressed = 1
                    Spinspeed = -1
                    move_x = -speed
                if event.key == pygame.K_RIGHT:
                    right_pressed = 1
                    Spinspeed2 = 1
                    move2_x = speed
                elif event.key == pygame.K_LEFT:
                    left_pressed = 1
                    Spinspeed2 = -1
                    move2_x = -speed
                elif event.key == pygame.K_UP:
                    up_pressed = 1
                    Spinspeed2 = 1
                    move2_y = -speed
                elif event.key == pygame.K_DOWN:
                    down_pressed = 1
                    Spinspeed2 = -1
                    move2_y = speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    Spressed = 0
                if event.key == pygame.K_w:
                    Wpressed = 0
                if event.key == pygame.K_d:
                    Dpressed = 0
                if event.key == pygame.K_a:
                    Apressed = 0
                if event.key == pygame.K_RIGHT:
                    right_pressed = 0
                if event.key == pygame.K_LEFT:
                    left_pressed = 0
                if event.key == pygame.K_UP:
                    up_pressed = 0
                if event.key == pygame.K_DOWN:
                    down_pressed = 0

    A_x = circle_radius*math.cos(circle_angle + 0.25*math.pi) + pos_x
    A_y = circle_radius*math.sin(circle_angle + 0.25*math.pi) + pos_y
    B_x = circle_radius*math.cos(circle_angle + 0.75*math.pi) + pos_x
    B_y = circle_radius*math.sin(circle_angle + 0.75*math.pi) + pos_y
    C_x = circle_radius*math.cos(circle_angle + 1.75*math.pi) + pos_x
    C_y = circle_radius*math.sin(circle_angle + 1.75*math.pi) + pos_y
    D_x = circle_radius*math.cos(circle_angle + 1.25*math.pi) + pos_x
    D_y = circle_radius*math.sin(circle_angle + 1.25*math.pi) + pos_y

    E_x = circle_radius*math.cos(circle_angle2 + 0.25*math.pi) + pos2_x
    E_y = circle_radius*math.sin(circle_angle2 + 0.25*math.pi) + pos2_y
    F_x = circle_radius*math.cos(circle_angle2 + 0.75*math.pi) + pos2_x
    F_y = circle_radius*math.sin(circle_angle2 + 0.75*math.pi) + pos2_y
    G_x = circle_radius*math.cos(circle_angle2 + 1.75*math.pi) + pos2_x
    G_y = circle_radius*math.sin(circle_angle2 + 1.75*math.pi) + pos2_y
    H_x = circle_radius*math.cos(circle_angle2 + 1.25*math.pi) + pos2_x
    H_y = circle_radius*math.sin(circle_angle2 + 1.25*math.pi) + pos2_y

    dorito2_y = circle_radius*math.sin(circle_angle2 + 2*math.pi) + pos2_y
    dorito2_x = circle_radius*math.sin(circle_angle2 + 2*math.pi) + pos2_x

    if pos_x - centre_size > screen_x:
        pos_x = 0 - centre_size
    if pos_x + centre_size < 0:
        pos_x = screen_x + centre_size
    if pos_y - centre_size > screen_y:
        pos_y = 0 - centre_size
    if pos_y + centre_size < 0:
        pos_y = screen_y + centre_size

    if pos2_x - centre_size > screen_x:
        pos2_x = 0 - centre_size
    if pos2_x + centre_size < 0:
        pos2_x = screen_x + centre_size
    if pos2_y - centre_size > screen_y:
        pos2_y = 0 - centre_size
    if pos2_y + centre_size < 0:
        pos2_y = screen_y + centre_size

    screen.fill((75, 75, 75))
    pygame.draw.polygon(screen, (255, 0, 0), [(B_x, B_y), (pos_x-centre_size/2,pos_y-centre_size/2), (circle_radius*math.cos(circle_angle + 0.75*math.pi)*5 + pos_x, circle_radius*math.sin(circle_angle + 0.75*math.pi)*5 + pos_y)])
    pygame.draw.polygon(screen, (0, 255, 0), [(F_x, F_y), (pos2_x-centre_size/2,pos2_y-centre_size/2), (circle_radius*math.cos(circle_angle2 + 0.75*math.pi)*5 + pos2_x, circle_radius*math.sin(circle_angle2 + 0.75*math.pi)*5 + pos2_y)])
    pygame.draw.polygon(screen, (150,0,0), [(A_x, A_y), (B_x, B_y), (D_x, D_y), (C_x, C_y)], width)
    pygame.draw.polygon(screen, (0,150,0), [(E_x, E_y), (F_x, F_y), (H_x, H_y), (G_x, G_y)], width)
    pygame.draw.rect(screen, (255,0,0), (pos_x-centre_size/2,pos_y-centre_size/2,centre_size,centre_size))
    pygame.draw.rect(screen, (0,255,0), (pos2_x-centre_size/2,pos2_y-centre_size/2,centre_size,centre_size))
    pygame.display.update()
    circle_angle = circle_angle + Spinspeed/48
    circle_angle2 = circle_angle2 - Spinspeed2/48
    pos_x = pos_x + move_x
    pos_y = pos_y + move_y
    pos2_x = pos2_x + move2_x
    pos2_y = pos2_y + move2_y
    if Apressed == 0 and Dpressed == 0:
        move_x = move_x * 0.95
    if Wpressed == 0 and Spressed == 0:
        move_y = move_y * 0.95
    if left_pressed == 0 and right_pressed == 0:
        move2_x = move2_x * 0.95
    if up_pressed == 0 and down_pressed == 0:
        move2_y = move2_y * 0.95
    if pos_x+circle_radius<pos_x-circle_radius == circle_radius*math.cos(circle_angle2 + 0.75*math.pi)*5 + pos2_x and pos_y+circle_radius<pos_y-circle_radius == circle_radius*math.sin(circle_angle2 + 0.75*math.pi)*5 + pos2_y:
        player_2_win()
    if pos2_x-centre_size/2 == circle_radius*math.cos(circle_angle + 0.75*math.pi)*5 + pos_x and pos2_y-centre_size/2 == circle_radius*math.sin(circle_angle + 0.75*math.pi)*5 + pos_y:
        player_1_win()
