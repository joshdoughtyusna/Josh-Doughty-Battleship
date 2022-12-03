import pygame
import sys
# from menu import Menu
from classic import CLASSIC
def Instructions():
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
    pygame.init()
    pygame.font.init()

    while True:
        SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        BG = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        SCREEN.fill(BLACK)

        for event in pygame.event.get():

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     CLASSIC()
                    # if rectc.collidepoint(pygame.mouse.get_pos()):
                #     CLASSIC()
                # if rectm.collidepoint(pygame.mouse.get_pos()):
                #     CLASSIC()
                # if rectp.collidepoint(pygame.mouse.get_pos()):
                #     CLASSIC()


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

