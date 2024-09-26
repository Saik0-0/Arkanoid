import pygame

pygame.init()
screen = pygame.display.set_mode((300, 400))

ball_1 = pygame.Rect(0, 110, 20, 20)
rect = pygame.Rect(0, 350, 50, 12)

blocks = []
coord = [5, 5]
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

clock = pygame.time.Clock()

while not done:
    screen.fill((255, 144, 0))

    for block in blocks:
        pygame.draw.rect(screen, 'White', block)

    pygame.draw.ellipse(screen, (0, 0, 0), ball_1)
    pygame.draw.rect(screen, 'White', rect)

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
            blocks.pop(i)
            dy_1 = -dy_1


    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and rect.x - 7 >= 0:
        rect.x -= 7

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and rect.x + 50 <= 300:
        rect.x += 7

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    clock.tick(40)

    pygame.display.flip()