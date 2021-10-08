import pygame
import math
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders (1).png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load('ufo (1).png'))
    EnemyX.append(random.randint(64, 736))
    EnemyY.append(random.randint(50, 150))
    EnemyX_change.append(2.5)
    EnemyY_change.append(20)

# Bullet

# Ready- you can't see the bullet on the screen

# Fire- The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def Enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def move_bullet(x, y):
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(EnemyX, EnemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(EnemyX - bulletX, 2)) + (math.pow(EnemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Background image
screen.blit(background, (0, 0))
player(playerX, playerY)

# Game Loop
running = True
while running:
    screen.blit(background, (0, 0))
    # Find out when User quits game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Find out what keys are pressed
    keys = pygame.key.get_pressed()

    # Managing player movements
    if keys[pygame.K_LEFT]:
        playerX_change = -3.5
    elif keys[pygame.K_RIGHT]:
        playerX_change = 3.5
    else:
        playerX_change = 0

    # Ensuring that player stays within the game's window
    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735
    else:
        playerX += playerX_change

    # Enemy Movement
    for i in range(num_of_enemies):
        EnemyX[i] += EnemyX_change[i]
        if EnemyX[i] <= 0:
            EnemyX_change[i] = 2.5
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -2.5
            EnemyY[i] += EnemyY_change[i]

            # Collision
        collision = isCollision(EnemyX[i], EnemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            EnemyX[i] = random.randint(64, 735)
            EnemyY[i] = random.randint(50, 150)

        Enemy(EnemyX[i], EnemyY[i], i)

    # Update the position of the player (Note that changes are not reflected on the window until window updates)
    player(playerX, playerY)

    # Managing bullet firing
    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            bulletX = playerX
            fire_bullet(bulletX, bulletY)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bulletY -= bulletY_change
        move_bullet(bulletX, bulletY)




    playerX += playerX_change


    player(playerX, playerY)

    pygame.display.update()
