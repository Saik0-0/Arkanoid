import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

ball_1 = pygame.Rect(0, 0, 20, 20)
rect = pygame.Rect(0, 250, 50, 10)
# ball_2 = pygame.Rect(100, 100, 20, 20)

dx_1 = 4
dy_1 = 10

dx_2 = 3
dy_2 = 12

done = False


clock = pygame.time.Clock()

while not done:
    screen.fill((0, 0, 0))

    pygame.draw.ellipse(screen, 'Red', ball_1)
    pygame.draw.rect(screen, 'Blue', rect)
    # pygame.draw.ellipse(screen, 'Blue', ball_2)
    ball_1.x += dx_1
    ball_1.y += dy_1
    # ball_2.x += dx_2
    # ball_2.y += dy_2

    # if ball_2.y >= 300:
    #     dy_2 = -dy_2
    # if ball_2.y <= 0:
    #     dy_2 = abs(dy_2)
    # if ball_2.x >= 400:
    #     dx_2 = -dx_2
    # if ball_2.x <= 0:
    #     dx_2 = abs(dx_2)

    if ball_1.y >= 300:
        dy_1 = -dy_1
    if ball_1.y <= 0:
        dy_1 = abs(dy_1)
    if ball_1.x >= 400:
        dx_1 = -dx_1
    if ball_1.x <= 0:
        dx_1 = abs(dx_1)

    # if ball_1.colliderect(ball_2):
    #     dy_1 = -dy_1
    #     dx_1 = -dx_1
    #     dy_2 = -dy_2
    #     dx_2 = -dx_2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                screen.fill((0, 0, 0))


    pygame.display.flip()
    clock.tick(60)

    pygame.display.flip()


# colliderect
