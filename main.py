# //////////////////////////////////// DOCS ////////////////////////////////////
# snake Speed = if we need to increase level then we need to increase snake speed
# snake_x = it containg snake x coordinate
# snake_y = it containg snake y coordinate
# **extra is ka kwars veriable in this we pass two values font_conroler or font_data whis is an fornt rendering obeject
import pygame
import sys
import random
import os

# //// iitalinging pygame
pygame.init()
pygame.mixer.init()
size = weidth, height = 970, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

fps = 30  # initilizing Frame rate
clock = pygame.time.Clock()
background = pygame.image.load("data\photos\s_back2.jpg")

# colors
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (165, 54, 146)

# fonts
font = pygame.font.SysFont('cooper black', 25)

# game controlers
exit_game = False
game_over = False

# sanke Food data
food_size = 20

# functions////////////////////////
score = 0
snake_speed = 3

# sound objects
soundObj = pygame.mixer.Sound('data\music\qback_play.mp3')


def snake_len_maker(screen, blue, snake_coordinates_list, snake_size):
    for x, y in snake_coordinates_list:
        pygame.draw.rect(screen, blue, [x, y, snake_size, snake_size])


def screen_text(text, color, x, y, **extra):
    try:
        if extra['font_conroler'] == 1:
            data = extra['font_data'].render(text, True, color)
            # print('data')
    except:
        data = font.render(text, True, color)
        # print(extra['font_conroler'])

    screen.blit(data, [x, y])


def game_over_function():

    extra_font = pygame.font.SysFont("Algerian", 90)
    screen_text("GAME OVER", white, 250, 250,
                font_data=extra_font, font_conroler=1)
    extra_font = pygame.font.SysFont("Arial Rounded MT Bold", 50)
    screen_text("Press Enter To Continue !", black, 290,
                350, font_data=extra_font, font_conroler=1)
    # print(game_over)d
    # print(exit_game)

    global exit_game
    global game_over
    global score
    global soundObj
    # print(game_over)
    if not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    print("handled")
                    soundObj.play()
                    game_over = False
                    score = 0
                    main_loop()

# MAIN GAME FUNCTION


def main_loop():
    global score
    global exit_game
    global game_over
    global food_size
    global snake_speed
    global high_score
    global soundObj
    # font_conroler = 0
    # snake coordinates
    snake_x = 80
    snake_y = 65
    # snake_velocity
    snake_velocity_x = 0
    snake_velocity_y = 0
    # snake_size_handler
    snake_size = 20
    # pause_controler
    pause_controler = 0
    pygame.draw.rect(screen, purple, [75, 160, food_size, food_size])

    # default food coodintes
    food_x = 300
    food_y = 210
    # game level
    level = 1

    # snake coordinartes holder
    snake_coordinates_list = []
    snake_length = 1

    # food COLOR random
    # redish=random.randrange(0,255)
    # grenish=random.randrange(0,255)
    # blueish=random.randrange(0,255)
    # print(type(food_color))
    # print(high_score.read())
    food_color = random.randrange(0, 255), random.randrange(
        0, 255), random.randrange(0, 255)
    while not exit_game:  # creating Game loop
        # print(food_x,food_y)
        if game_over:  # OVER HANDELER
            game_over_function()

        if not game_over:
            food_size = 20
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # exit controlling key
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        snake_velocity_x = + snake_speed
                        snake_velocity_y = 0
                        pause_controler = 0

                    if event.key == pygame.K_a:
                        snake_velocity_x = - snake_speed
                        snake_velocity_y = 0
                        pause_controler = 0

                    if event.key == pygame.K_w:
                        snake_velocity_y = - snake_speed
                        snake_velocity_x = 0
                        pause_controler = 0
                    if event.key == pygame.K_s:
                        snake_velocity_y = + snake_speed
                        snake_velocity_x = 0
                        pause_controler = 0
                    if event.key == pygame.K_p:
                        pause_controler = 1
                        snake_velocity_x = 0
                        snake_velocity_y = 0
                        # print(snake_x,snake_y)

            # handeling snake velocity

            snake_x += snake_velocity_x
            snake_y += snake_velocity_y

            if abs(snake_x-food_x) < 7 and abs(snake_y-food_y) < 7:
                # food coordinates handler or creater
                food_color = random.randrange(0, 255), random.randrange(
                    0, 255), random.randrange(0, 255)
                score += 1
                level = level+5
                snake_length += 3
                food_x = random.randrange(70, 320, 5)
                food_y = random.randrange(70, 490, 5)

            # if level%6==0:
            #     snake_speed=snake_speed+1
            # creating snake field area

            screen.blit(background, [0, 0])
            pygame.draw.rect(screen, red, [snake_x, snake_y, snake_size, snake_size])
            # pygame.draw.rect(screen, red, [50, 50, 340, 510], 1, border_radius=40)

            # food draw
            pygame.draw.rect(screen, food_color, [
                             food_x, food_y, food_size, food_size])
            # bola toh main control hai bhai nake lenngth
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_coordinates_list.append(head)
            snake_len_maker(screen, blue, snake_coordinates_list, snake_size)
            if(len(snake_coordinates_list)) > snake_length:
                del snake_coordinates_list[0]

            # if( not os.path.exist('high_score.txt')):
            #     f= open('high_score.txt','w')
            #     f.write("0")

            high_score = open('data\high_score.txt', "r")
            high_score_val = high_score.read()
            high_score_val = int(high_score_val)
            high_score.close()

            # checknig any kind of conditoins
            if(snake_x < 50 or snake_x > 371 or snake_y > 550 or snake_y < 53):
                if(score > high_score_val):

                    # opening file
                    high_score_update = open('data\high_score.txt', 'w')
                    score_save = str(score)
                    high_score_update.write(score_save)
                    high_score_update.close()
                    # closing file after dealling with data and savin some extra stuff in it

                soundObj.stop()
                game_over = True
                # game_over_function()
            extra_font = pygame.font.SysFont('Clarendon Blk BT', 55)
            screen_text("score: "+str(score), red, 450, 150,
                        font_conroler=1, font_data=extra_font)
            screen_text("High Score: "+str(high_score_val), purple,
                        650, 150, font_conroler=1, font_data=extra_font)
            if(high_score_val < score):
                extra_font = pygame.font.SysFont('Freehand521 BT', 55)
                screen_text("You Created A high Score !!", purple,
                            450, 200, font_conroler=1, font_data=extra_font)
            # callig pause function
            if (pause_controler == 1):
                screen_text('PAUSED', blue, 450, 500)
        pygame.display.update()
        clock.tick(fps)


def main():
    global soundObj
    # back=pygame.mixer.music.load('music\qback_play.mp3')
    # pygame.mixer.music.play()
    soundObj.play()
    main_loop()


main()
