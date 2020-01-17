import pygame
import sys
import random

red = 200
blue = 200
green = 200

pygame.init()

canvas_x = 1400
canvas_y = 800

ball_size = 25
ball_x = canvas_x/2 - ball_size/2
ball_y = canvas_y/2 + ball_size/2

square_x = canvas_x/2
square_y = canvas_y/2
square_size = 25
other_x = canvas_x/2
other_y = canvas_y/2
other_size = 25

ballspeed = 2
# 2 is casual, 3 is competitive

balldirection = random.randint(0,3)
if balldirection == 0:
   ball_xspeed = -ballspeed
   ball_yspeed = -ballspeed
elif balldirection == 1:
   ball_xspeed = -ballspeed
   ball_yspeed = ballspeed
elif balldirection == 2:
   ball_xspeed = ballspeed
   ball_yspeed = -ballspeed
elif balldirection == 3:
   ball_xspeed = ballspeed
   ball_yspeed = ballspeed

x_speed = 0
y_speed = 0
x_other = 0
y_other = 0

leftpressed = 0
rightpressed = 0
uppressed = 0
downpressed = 0
leftothered = 0
rightothered = 0
upothered = 0
downothered = 0

screen = pygame.display.set_mode((canvas_x, canvas_y))
screen.fill((red, green, blue))

gamepaused = 1

exit = 0
while exit == 0:
   screen.fill((red, green, blue))
   for event in pygame.event.get():
      if event.type == pygame.QUIT:  # makes the program mortal
          exit = 1
          sys.exit()

      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              leftpressed = 1
              x_speed = -2
          if event.key == pygame.K_RIGHT:
              rightpressed = 1
              x_speed = 2
          if event.key == pygame.K_UP:
              uppressed = 1
              y_speed = -2
          if event.key == pygame.K_DOWN:
              downpressed = 1
              y_speed = 2

          if event.key == pygame.K_a:
              leftothered = 1
              x_other = -2
          if event.key == pygame.K_d:
              rightothered = 1
              x_other = 2
          if event.key == pygame.K_w:
              upothered = 1
              y_other = -2
          if event.key == pygame.K_s:
              downothered = 1
              y_other = 2

          if event.key == pygame.K_SPACE:
              if gamepaused == 1:
                  gamepaused = 0
              elif gamepaused == 0:
                  gamepaused = 1

      elif event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
              if rightpressed == 0:
                  x_speed = 0
                  leftpressed = 0
              elif rightpressed == 1:
                  leftpressed = 0
          if event.key == pygame.K_RIGHT:
              if leftpressed == 0:
                  x_speed = 0
                  rightpressed = 0
              elif leftpressed == 1:
                  rightpressed = 0
          if event.key == pygame.K_UP:
              if downpressed == 0:
                  y_speed = 0
                  uppressed = 0
              elif downpressed == 1:
                  uppressed = 0
          if event.key == pygame.K_DOWN:
              if uppressed == 0:
                  y_speed = 0
                  downpressed = 0
              elif uppressed == 1:
                  downpressed = 0

          if event.key == pygame.K_a:
              if rightothered == 0:
                  x_other = 0
                  leftothered = 0
              elif rightothered == 1:
                  leftothered = 0
          if event.key == pygame.K_d:
              if leftothered == 0:
                  x_other = 0
                  rightothered = 0
              elif leftothered == 1:
                  rightothered = 0
          if event.key == pygame.K_w:
              if downothered == 0:
                  y_other = 0
                  upothered = 0
              elif downothered == 1:
                  upothered = 0
          if event.key == pygame.K_s:
              if upothered == 0:
                  y_other = 0
                  downothered = 0
              elif upothered == 1:
                  downothered = 0

   if square_x <= canvas_x/4 + canvas_x/2 - square_size:
       square_x = canvas_x/4 + canvas_x/2 - square_size

   if other_x > canvas_x/4:
       other_x = canvas_x/4

   if ball_x + ball_size >= canvas_x or ball_x <= 0:
        exit = 1
        sys.exit()
   if ball_y + ball_size >= canvas_y or ball_y <= 0:
       ball_yspeed = ball_yspeed*-1

   if ball_x + ball_size >= square_x and ball_x - ball_size <= square_x and ball_y >= square_y - (square_size*2) and ball_y <= square_y + (square_size*4):
       ball_xspeed = abs(ball_xspeed)*-1
   if ball_x + ball_size >= other_x and ball_x - ball_size <= other_x and ball_y >= other_y - (other_size*2) and ball_y <= other_y + (other_size*4):
       ball_xspeed = abs(ball_xspeed)*1

   if gamepaused == 0:
       square_y = square_y + y_speed
       square_x = square_x + x_speed
       other_y = other_y + y_other
       other_x = other_x + x_other
       ball_x = ball_xspeed + ball_x
       ball_y = ball_yspeed + ball_y
       pygame.time.wait(5)

   pygame.draw.rect(screen, (0, 0, 0), (other_x, other_y, other_size, other_size*4))
   pygame.draw.rect(screen, (0, 0, 0), (square_x, square_y, square_size, square_size*4))
   pygame.draw.rect(screen, (0, 0, 0), (ball_x, ball_y, ball_size, ball_size))
   pygame.display.update()
