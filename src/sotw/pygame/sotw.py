import pygame
import random
#import time

width = 640
height = 480
radius = 50
stroke = 5

fps = 5
FPSCLOCK = pygame.time.Clock()

colours = ((255, 0, 0), (0, 255, 0), (0, 0, 255))

pygame.init()

window = pygame.display.set_mode((width, height))
window.fill(pygame.Color(255, 255, 255))

done = True
while done:
    # event handling
    for event in pygame.event.get(): # if we click something ...
        if event.type == pygame.QUIT: # if we click close ...
            done=False # this will cause the loop to finish.

    centerX = random.randint(1, 640)
    centerY = random.randint(1, 480)

    color = random.randint(0, 2)
    
    pygame.draw.circle(window,
                       colours[color],
                       (centerX, centerY),
                       radius, stroke)

    pygame.display.update()

    FPSCLOCK.tick(fps)

pygame.quit()
