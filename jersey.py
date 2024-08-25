import pygame
import sys

pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Real Madrid Jersey Animation')

WHITE = (255, 255, 255)
jersey_img = pygame.image.load('real_madrid_jersey.png')
jersey_img = pygame.transform.scale(jersey_img, (200, 200))

x, y = 0, (height // 2) - 100
speed_x = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += speed_x

    if x + 200 > width or x < 0:
        speed_x = -speed_x


    window.fill(WHITE)
    window.blit(jersey_img, (x, y))
    pygame.display.update()
    pygame.time.Clock().tick(30)
