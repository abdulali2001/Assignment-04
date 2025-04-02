import pygame

import time

pygame.init()

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

BLUE = (0, 0, 225)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

screen = pygame.display.set_mode((CANVAS_WIDTH,CANVAS_HEIGHT))
pygame.display.set_caption("Enter effect in pygame")

grid = []
for row in range(0, CANVAS_HEIGHT,CELL_SIZE):
    for col in range(0,CANVAS_WIDTH,CELL_SIZE):
        react = pygame.Rect(col,row,CELL_SIZE,CELL_SIZE)
        grid.append(react)

eraser = pygame.Rect(200,200,ERASER_SIZE,ERASER_SIZE)

running = True
while running:
    screen.fill(WHITE)

    for react in grid:
        pygame.draw.rect(screen,BLUE,react)

    mouse_x , mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x,mouse_y)

    new_grid = []
    for react in grid:
        if not eraser.colliderect(react):
            new_grid.append(react)
    grid = new_grid

    pygame.draw.rect(screen,PINK,eraser)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()