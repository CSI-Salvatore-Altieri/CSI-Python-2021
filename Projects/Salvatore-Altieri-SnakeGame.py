from random import random, randrange
import time
from tkinter import Y
import pygame
import random
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

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameRestart():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    lenght_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) *10 
    foody = round(random.randrange(0, dis_width - snake_block) / 10) *10 

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("Game over, you're a Loser Press Q-Quit or P-Play Again")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameRestart()

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
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #makes food
        # pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block]) #crea el snake y lo ubica en la pantalla
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > lenght_of_snake:
            del snake_list[0]

        for x in snake_list[: -1]:
            if x == snake_head:
                game_close = True
        
        our_snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) *10 
            foody = round(random.randrange(0, dis_width - snake_block) / 10) *10
            lenght_of_snake += 1 

        clock.tick(snake_speed)

# pygame.display.update()
# time.sleep(5)
    pygame.quit()
    quit()

gameRestart()