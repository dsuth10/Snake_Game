import pygame
import random

pygame.init()

# Game window dimensions
width, height = 600, 400
win = pygame.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True
score = 0

# Game speed
clock = pygame.time.Clock()
speed = 15

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Changing direction of the snake
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        run = False
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        run = False

    for block in snake_body[1:]:
        if snake_pos == block:
            run = False

    # Displaying the score and updating the game
    win.fill(black)
    for pos in snake_body:
        pygame.draw.rect(win, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(win, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Displaying the score
    font = pygame.font.SysFont(None, 35)
    score_text = font.render('Score: ' + str(score), True, white)
    win.blit(score_text, [0, 0])

    pygame.display.update()

    # Check for game over
    if not run:
        win.fill(black)
        over_text = font.render('Game Over! Score: ' + str(score), True, white)
        win.blit(over_text, [width//4, height//3])
        pygame.display.update()
        pygame.time.wait(2000)

    clock.tick(speed)

pygame.quit()
