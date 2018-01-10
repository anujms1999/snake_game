# snake game by Anuj Shah

import pygame
import sys
import random
import time

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!)had {0} initializing errors detected,exiting........".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully initialized")

# playing surface
playsurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game!!!")

# colors
red = pygame.Color(255, 0, 0)  # game over
green = pygame.Color(0, 255, 0)  # snake
blue = pygame.Color(0, 0, 255)  # fruits
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # fruits

# FPS controller
fpscontoller = pygame.time.Clock()

# important variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction
score = 0

# game over functuion
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    Gosurf = myFont.render('Game Over !', True, red)
    Gorect = Gosurf.get_rect()
    Gorect.midtop = (360, 15)
    playsurface.blit(Gosurf, Gorect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()

# SCORE FUNCTION
def showScore(choice =1):
    sFont = pygame.font.SysFont('monaco', 24)
    ssurf = sFont.render('SCORE:'+ str(score), True, black)
    srect = ssurf.get_rect()
    if choice == 1:
       srect.midtop= (80,10)
    else:
        srect.midtop = (360,120)
    playsurface.blit(ssurf,srect)
    pygame.display.flip()
 #   showScore(0)
 #   time.sleep(4)
#    pygame.quit()
#    sys.exit()



# MAIN LOGIC OF THE GAME

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeTo = 'LEFT'
            if event.key == pygame.K_UP:
                changeTo = 'UP'
            if event.key == pygame.K_DOWN:
                changeTo = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    # validation of direction
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # main body
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    playsurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playsurface, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(playsurface, blue, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    if snakePos[0] > 750 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
    pygame.display.flip()
    showScore()
    fpscontoller.tick(25)


















