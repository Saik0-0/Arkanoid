import random

import pygame

pygame.init()
screen = pygame.display.set_mode((300, 400))


ball_1 = pygame.Rect(0, 140, 20, 20)
rect = pygame.Rect(0, 350, 50, 12)

bonus_active_time = 0
bonus_duration = 7000
bonus_ball_active = False
bonus_ball = pygame.Rect(150, 110, 15, 15)

blocks = []
coord = [5, 25]
for i in range(20):
    if i % 5 != 0:
        coord[0] += 60
    elif i != 0:
        coord[0] = 5
        coord[1] += 25
    blocks.append(pygame.Rect(*coord, 50, 20))

dx_1 = 3
dy_1 = 9

done = False
start_time = pygame.time.get_ticks()
clock = pygame.time.Clock()

while not done:
    screen.fill((255, 144, 0))

    for block in blocks:
        pygame.draw.rect(screen, 'White', block)

    pygame.draw.ellipse(screen, (0, 0, 0), ball_1)
    pygame.draw.rect(screen, 'White', rect)

    curr_time = pygame.time.get_ticks()
    if curr_time - bonus_active_time > bonus_duration and rect.width > 50:
        rect.width = 50

    if bonus_ball_active:
        pygame.draw.ellipse(screen, 'Green', bonus_ball)
        bonus_ball.y += 10
        if rect.colliderect(bonus_ball):
            rect.width = 100
            bonus_active_time = curr_time
            bonus_ball_active = False
        elif bonus_ball.y > 400:
            bonus_ball_active = False

    ball_1.x += dx_1
    ball_1.y += dy_1

    if ball_1.y >= 400:
        ball_1.x = 0
        ball_1.y = 110
    if ball_1.y <= 0:
        dy_1 = abs(dy_1)
    if ball_1.x >= 300:
        dx_1 = -dx_1
    if ball_1.x <= 0:
        dx_1 = abs(dx_1)

    if ball_1.colliderect(rect):
        dy_1 = -dy_1
        ball_1.y = rect.y - ball_1.height

    for i in range(len(blocks)):
        if i < len(blocks) and ball_1.colliderect(blocks[i]):
            if not bonus_ball_active and random.randint(2, 2) == 2:
                bonus_ball_active = True
                bonus_ball.x = ball_1.x
                bonus_ball.y = ball_1.y
            blocks.pop(i)
            dy_1 = -dy_1
            break

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and rect.x - 7 >= 0:
        rect.x -= 7

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and rect.x + rect.width <= 300:
        rect.x += 7

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    clock.tick(40)

    pygame.display.flip()