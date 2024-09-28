import random
import pygame

pygame.init()
screen = pygame.display.set_mode((300, 400))

lives = 5
font = pygame.font.Font(None, 36)

ball = pygame.Rect(0, 140, 20, 20)
rect = pygame.Rect(0, 350, 50, 12)

bonus_duration = 7000

bonus_ball_1 = pygame.Rect(150, 110, 15, 15)
bonus_1_active_time = 0
bonus_ball_1_active = False

bonus_ball_2 = pygame.Rect(150, 110, 15, 15)
bonus_ball_2_active = False

bonus_ball_3 = pygame.Rect(150, 110, 15, 15)
bonus_ball_3_active = False

bonus_ball_4 = pygame.Rect(150, 110, 15, 15)
bonus_ball_4_active = False

blocks = []
coord = [5, 25]
for i in range(20):
    if i % 5 != 0:
        coord[0] += 60
    elif i != 0:
        coord[0] = 5
        coord[1] += 25
    blocks.append(pygame.Rect(*coord, 50, 20))

dx = 3
dy = 9

done = False
clock = pygame.time.Clock()

while not done:
    screen.fill((255, 144, 0))
    if lives == 0:
        done = True
        print('Вы проиграли')
    if len(blocks) == 0:
        done = True
        print('Вы выиграли')
    text = font.render('Жизни: ' + str(lives), True, 'Black')
    screen.blit(text, (0, 0))

    for block in blocks:
        pygame.draw.rect(screen, 'White', block)

    pygame.draw.ellipse(screen, (0, 0, 0), ball)
    pygame.draw.rect(screen, 'White', rect)

    if pygame.time.get_ticks() - bonus_1_active_time > bonus_duration and rect.width > 50:
        rect.width = 50

    if bonus_ball_1_active:
        pygame.draw.ellipse(screen, (12, 243, 91), bonus_ball_1)
        bonus_ball_1.y += 7
        if rect.colliderect(bonus_ball_1):
            rect.width = 100
            bonus_1_active_time = pygame.time.get_ticks()
            bonus_ball_1_active = False
        elif bonus_ball_1.y > 400:
            bonus_ball_1_active = False

    if bonus_ball_2_active:
        pygame.draw.ellipse(screen, (92, 189, 0), bonus_ball_2)
        bonus_ball_2.y += 7
        if rect.colliderect(bonus_ball_2):
            lives += 1
            bonus_ball_2_active = False
        elif bonus_ball_2.y > 400:
            bonus_ball_2_active = False

    if bonus_ball_3_active:
        pygame.draw.ellipse(screen, (180, 24, 9), bonus_ball_3)
        bonus_ball_3.y += 7
        if rect.colliderect(bonus_ball_3):
            if dy > 0:
                dy += 2
            else:
                dy -= 2
            bonus_ball_3_active = False
        elif bonus_ball_3.y > 400:
            bonus_ball_3_active = False

    if bonus_ball_4_active:
        pygame.draw.ellipse(screen, (180, 24, 9), bonus_ball_4)
        bonus_ball_4.y += 7
        if rect.colliderect(bonus_ball_4):
            ball.width -= 8
            ball.height -= 8
            bonus_ball_4_active = False
        elif bonus_ball_4.y > 400:
            bonus_ball_4_active = False

    ball.x += dx
    ball.y += dy

    if ball.y >= 400:
        ball.x = 0
        ball.y = 140
        lives -= 1
    if ball.y <= 0:
        dy = abs(dy)
    if ball.x >= 300:
        dx = -dx
    if ball.x <= 0:
        dx = abs(dx)

    if ball.colliderect(rect):
        dy = -dy
        ball.y = rect.y - ball.height

    for i in range(len(blocks)):
        if ball.colliderect(blocks[i]):
            rnd = random.randint(1, 10)
            if not bonus_ball_1_active and rnd == 1:
                bonus_ball_1_active = True
                bonus_ball_1.x = ball.x
                bonus_ball_1.y = ball.y
            if not bonus_ball_2_active and rnd == 2:
                bonus_ball_2_active = True
                bonus_ball_2.x = ball.x
                bonus_ball_2.y = ball.y
            if not bonus_ball_3_active and rnd == 3:
                bonus_ball_3_active = True
                bonus_ball_3.x = ball.x
                bonus_ball_3.y = ball.y
            if not bonus_ball_4_active and rnd == 4:
                bonus_ball_4_active = True
                bonus_ball_4.x = ball.x
                bonus_ball_4.y = ball.y
            blocks.pop(i)
            dy = -dy
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