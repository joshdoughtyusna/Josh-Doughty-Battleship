import time

import pygame
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
GREEN = (0, 223, 0)
RED = (223, 0, 0)
BLUE = (0, 0, 223)
PURPLE = (123, 45, 233)
WHITE = (233, 233, 233)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
# pygame.SYSTEM_CURSOR_CROSSHAIR
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BG = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("BATTLESHIP")
end = (100, 100, 300, 200)
pygame.init()

def P1():
    SCREEN.fill(BLACK)
def P2():
    SCREEN.fill(WHITE)
while True:
    while (1):
        P1()
    while (1):
        P2()
        time.sleep(2)


    pygame.display.update()