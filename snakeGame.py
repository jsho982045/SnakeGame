import pygame
import random

# initialize pygame
pygame.init()

# set up game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# set up font
font = pygame.font.SysFont(None, 30)

# set up clock
clock = pygame.time.Clock()

# set up snake
snake_block_size = 10
snake_speed = 10
snake_list = []
snake_length = 1
snake_direction = 'right'

def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])

# set up food
food_block_size = 10
food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0
food = pygame.Rect(food_x, food_y, food_block_size, food_block_size)

def draw_food():
    pygame.draw.rect(window, red, food)

# set up score
score = 0

def show_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, [0, 0])

# set up game over message
def game_over_message():
    message = font.render("Game Over!", True, white)
    message_rect = message.get_rect(center=(window_width/2, window_height/2))
    window.blit(message, message_rect)
    pygame.display.update()
    pygame.time.wait(2000)

# set up all-time high score
all_time_high_score = 0

# game loop
game_over = False
while not game_over:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == pygame.K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'
            elif event.key == pygame.K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == pygame.K_DOWN and snake_direction != 'up':
                snake_direction = 'down'
    
    # update snake position
    if len(snake_list) > 0:
        if snake_direction == 'right':
            snake_head = [snake_list[-1][0] + snake_block_size, snake_list[-1][1]]
        elif snake_direction == 'left':
            snake_head = [snake_list[-1][0] - snake_block_size, snake_list[-1][1]]
        elif snake_direction == 'up':
            snake_head = [snake_list[-1][0], snake_list[-1][1] - snake_block_size]
        elif snake_direction == 'down':
            snake_head = [snake_list[-1][0], snake_list[-1][1] + snake_block_size]
    else:
        snake_head = [0, 0]

    # check for collision with walls
    if snake_head[0] >= window_width or snake_head[0] < 0 or snake_head[1] >= window_height or snake_head[1] < 0:
        game_over = True
    
    # check for collision with food
    if snake_head[0] == food.x and snake_head[1] == food.y:
        food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0
        food = pygame.Rect(food_x, food_y, food_block_size, food_block_size)
        snake_length += 1
        score += 1
    
    # update snake list
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    
    # draw game elements
    window.fill(black)
    draw_snake(snake_block_size, snake_list)
    draw_food()
    show_score(score)
    pygame.display.update()
    
    # set game speed
    clock.tick(snake_speed)

# display game over message
game_over_message()

# check for all-time high score
if score > all_time_high_score:
    all_time_high_score = score

# display scores and options
while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #reset game variables
                snake_list = []
                snake_length = 1
                snake_direction = 'right'
                food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
                food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0
                food = pygame.Rect(food_x, food_y, food_block_size, food_block_size)
                score = 0
                game_over = False

                #restart game loop
                while not game_over:
                    # event handling
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_over = True
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                game_over = True
                            elif event.key == pygame.K_LEFT and snake_direction != 'right':
                                snake_direction = 'left'
                            elif event.key == pygame.K_RIGHT and snake_direction != 'left':
                                snake_direction = 'right'
                            elif event.key == pygame.K_UP and snake_direction != 'down':
                                snake_direction = 'up'
                            elif event.key == pygame.K_DOWN and snake_direction != 'up':
                                snake_direction = 'down'
                # update snake position
                    if len(snake_list) > 0:
                        if snake_direction == 'right':
                            snake_head = [snake_list[-1][0] + snake_block_size, snake_list[-1][1]]
                        elif snake_direction == 'left':
                            snake_head = [snake_list[-1][0] - snake_block_size, snake_list[-1][1]]
                        elif snake_direction == 'up':
                            snake_head = [snake_list[-1][0], snake_list[-1][1] - snake_block_size]
                        elif snake_direction == 'down':
                            snake_head = [snake_list[-1][0], snake_list[-1][1] + snake_block_size]
                    else:
                        snake_head = [0, 0]  
    
                    # check for collision with walls
                    if snake_head[0] >= window_width or snake_head[0] < 0 or snake_head[1] >= window_height or snake_head[1] < 0:
                        game_over = True

                    # check for collision with food
                    if snake_head[0] == food.x and snake_head[1] == food.y:
                        food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
                        food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0
                        food = pygame.Rect(food_x, food_y, food_block_size, food_block_size)
                        snake_length += 1
                        score += 1
                    # update snake list
                    snake_list.append(snake_head)
                    if len(snake_list) > snake_length:
                        del snake_list[0]
                    # draw game elements
                    window.fill(black)
                    draw_snake(snake_block_size, snake_list)
                    draw_food()
                    show_score(score)
                    pygame.display.update()
                    
    # set up options text 
    options_text = font.render("Press SPACE to play again or ESCAPE to quit", True, white)
    options_rect = options_text.get_rect(center=(window_width/2, window_height - 50))

    # display all time high score
    all_time_high_score_text = font.render("All-Time High Score: " + str(all_time_high_score), True, white)
    all_time_high_score_rect = all_time_high_score_text.get_rect(center=(window_width/2, window_height - 100)) 
    window.blit(all_time_high_score_text, all_time_high_score_rect)

    # display current score 
    current_score_text = font.render("Your Score: " + str(score), True, white)   
    current_score_rect = current_score_text.get_rect(center=(window_width/2, window_height - 150))
    window.blit(current_score_text, current_score_rect)

    # display options text 
    window.blit(options_text, options_rect)

    # update display
    pygame.display.update()

    # check for key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game_over = False
        snake_list.clear()
        snake_length = 1
        score = 0
        snake_direction = 'right'
        food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0
        food = pygame.Rect(food_x, food_y, food_block_size, food_block_size)
        continue
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()






