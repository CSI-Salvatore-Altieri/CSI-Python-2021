import time
from tkinter import Y
import pygame
pygame.init()

yellow = (251, 230, 70) #score
green = (107, 250, 158) #food
black = (0, 0, 0) #background
blue = (91, 57, 250) #snake
red = (250, 76, 70) #game over

dis_width = 1000
dis_height = 500
dis=pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Snake Game by SAAM")
game_over = False

x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0

snake_block = 10
snake_speed = 1000000

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(black)
    pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block]) #crea el snake y lo ubica en la pantalla
    pygame.display.update()

    clock.tick(snake_speed)

message("You're a Loser take the L", red)
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()