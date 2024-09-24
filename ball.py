import pygame

pygame.init()
screen = pygame.display.set_mode((300, 400))

ball_1 = pygame.Rect(0, 0, 20, 20)
rect = pygame.Rect(0, 350, 50, 12)

dx_1 = 3
dy_1 = 9

done = False

clock = pygame.time.Clock()

while not done:
    screen.fill((255, 144, 0))

    pygame.draw.ellipse(screen, (0, 0, 0), ball_1)
    pygame.draw.rect(screen, 'White', rect)

    ball_1.x += dx_1
    ball_1.y += dy_1

    if ball_1.y >= 400:
        ball_1.x = 0
        ball_1.y = 0
    if ball_1.y <= 0:
        dy_1 = abs(dy_1)
    if ball_1.x >= 300:
        dx_1 = -dx_1
    if ball_1.x <= 0:
        dx_1 = abs(dx_1)

    if ball_1.colliderect(rect):
        dy_1 = -dy_1
        ball_1.y = rect.y - ball_1.height

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and rect.x - 7 >= 0:
        rect.x -= 7

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and rect.x + 50 <= 300:
        rect.x += 7

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    clock.tick(60)

    pygame.display.flip()