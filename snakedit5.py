import pygame 
import time
import random
pygame.init()
white = (255, 255, 255)
darkblue = (17, 76, 140) 
maroon = (143, 29, 53)
violet = (49, 0, 133)
darkgreen = (147,150,45)
lightgreen = (210,218,109)
magenta = (155, 2, 163)
green = (0, 87, 14)
red = (209, 0, 0)
orange = (214, 89, 0)
dis_width = 750
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('AirPollution Snake Game')
clock = pygame.time.Clock()
snake_block = 25
snake_speed = 7
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
carbon_font = pygame.font.SysFont("bahnschrift", 35)
carbon_clicks = 0
def Your_score(score):
    value = score_font.render("Number of Trees Collected: " + str(score), True, darkblue)
    dis.blit(value, [0, 0])
def Your_carbon(carbon):
    value = carbon_font.render("Number of Carbons Produced: " + str(carbon), True, magenta)
    dis.blit(value, [0, 40])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, maroon, [x[0], x[1], snake_block, snake_block])
# Messages for your final tree + carbon score, and exit panel (when the game ends)
def message(msg, color, width, height):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / width, dis_height / height])
def gameLoop(carbon_clicks=0):
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    click_thrice = 0
    treex = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
    treey = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0

    while not game_over:
        while game_close == True:
            dis.fill(lightgreen)
            #End of game message (general)
            message("Game Over! You had " + str(Length_of_snake - 1) + " trees and " + str(carbon_clicks) + " carbon pollutants.", violet, 8, 3.5)
            #Beginning of if condition for WINNER or LOSER
            if carbon_clicks > (Length_of_snake - 1):
                message("You Lose! You had too much carbon in the air, try again!", red, 8, 2.5)
            else:
                message("You Win! Your trees eliminated the carbon,", green, 4.7, 2.5)
                message("saving the environment!", green, 3.2, 2.1)
            message("Press C-Play Again or Q-Quit", violet, 3.6, 1.75)
            Your_score(Length_of_snake - 1)
            Your_carbon(carbon_clicks)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    click_thrice += 1
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    click_thrice += 1
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    click_thrice += 1
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    click_thrice += 1
                    y1_change = snake_block
                    x1_change = 0
            if click_thrice == 3:
                carbon_clicks += 1
                click_thrice = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(lightgreen)
        pygame.draw.rect(dis, darkgreen, [treex, treey, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        Your_carbon(carbon_clicks)
        pygame.display.update()
        if x1 == treex and y1 == treey:
            treex = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
            treey = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0
            Length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop(carbon_clicks)