import pygame
import math
import random
from pygame import mixer

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Back sound
mixer.music.load('background.wav')
mixer.music.play(-1)

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
    EnemyImg.append(pygame.image.load('enemy.png'))
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

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def showscore(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (275, 275))


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

        # Game over
        if EnemyY[i] > 400:
            for j in range(num_of_enemies):
                EnemyY[j] = 2000
            game_over_text()
            break

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
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            EnemyX[i] = random.randint(64, 735)
            EnemyY[i] = random.randint(50, 150)

        Enemy(EnemyX[i], EnemyY[i], i)

    # Update the position of the player (Note that changes are not reflected on the window until window updates)
    player(playerX, playerY)

    # Managing bullet firing
    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            bullet_sound = mixer.Sound('waw.wav')
            bullet_sound.play()
            bulletX = playerX
            fire_bullet(bulletX, bulletY)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bulletY -= bulletY_change
        move_bullet(bulletX, bulletY)

    playerX += playerX_change

    showscore(textX, textY)

    player(playerX, playerY)

    pygame.display.update()

    # Collision
    # collision = isCollision(EnemyX, EnemyY, bulletX, bulletY)
    # if collision:
    #     bulletY = 480
    #     bullet_state = "ready"
    #     score += 1
    #     print(score)
    #     EnemyX = random.randint(64, 735)
    # EnemyY = random.randint(50, 150)
