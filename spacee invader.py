import pygame

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
EnemyImg = pygame.image.load('ufo (1).png')
EnemyX = random.randint(64, 736)
EnemyY = random.randint(50, 150)
EnemyX_change = 2.5
EnemyY_change = 40

# Bullet
# Ready- you can't see the bullet on the screen
# Fire- The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def Enemy(x, y):
    screen.blit(EnemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop
running = True
while running:
    # RGB = Red, green, blue
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 3.5

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Checking boundaries of spaceship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    EnemyX += EnemyX_change

    if EnemyX <= 0:
        EnemyX_change = 2.5
        EnemyY += EnemyY_change
    elif EnemyX >= 736:
        EnemyX_change = -2.5
        EnemyY += EnemyY_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    Enemy(EnemyX, EnemyY)
    pygame.display.update()
