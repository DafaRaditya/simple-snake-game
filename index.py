import pygame
import time
import random

# Inisialisasi pygame
pygame.init()

# Ukuran layar
dis_width = 400
dis_height = 300

# Warna
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Setup tampilan
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Game Ular Sederhana')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 30)

def Your_score(score):
    value = score_font.render("Skor: " + str(score), True, white)
    dis.blit(value, [10, 10])

def High_score(high_score):
    value = score_font.render("Skor Tertinggi: " + str(high_score), True, white)
    dis.blit(value, [dis_width - 200, 10])

def message(msg, color):
    messages = msg.split('\n')
    y_offset = dis_height / 2 - len(messages) * 20 / 2  # Center vertically
    for i, line in enumerate(messages):
        mesg = font_style.render(line, True, color)
        dis.blit(mesg, [dis_width / 2 - mesg.get_width() / 2, y_offset + i * 35])

def gameLoop():
    global high_score
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    current_score = 0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Game Over!\nTekan Q untuk Keluar\natau C untuk Bermain Lagi", red)
            Your_score(current_score)
            High_score(high_score)
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
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(dis, black, [segment[0], segment[1], snake_block, snake_block])

        Your_score(current_score)
        High_score(high_score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            current_score += 10
            if current_score > high_score:
                high_score = current_score

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Inisialisasi skor tertinggi
high_score = 0

gameLoop()
