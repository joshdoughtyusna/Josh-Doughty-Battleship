import sys
from classic import CLASSIC
import time
import pygame


def Menu():
    import sys
    from power_up import POWER
    from classic import CLASSIC
    import time
    import pygame
    from instructions import Instructions
    from ship import Ship
    from random import randrange
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
    bbx = 100
    bby = 0
    bcx = 150
    bcy = 250
    bmx = 150
    bmy = 400
    bpx = 150
    bpy = 325
    rx = 250
    ry = 250
    font = pygame.font.SysFont('Corbel', 50)
    bfont = pygame.font.SysFont('impact', 60)
    battleship = bfont.render("BATTLESHIP", True, GREEN)
    classic = font.render('CLASSIC', True, GREEN)
    multiplayer = font.render('MULTI', True, GREEN)
    power = font.render('POWER', True, GREEN)
    rectc = pygame.Rect(bcx, bcy, 200, 50)
    rectm = pygame.Rect(bmx, bmy, 200, 50)
    rectp = pygame.Rect(bpx, bpy, 200, 50)
    angle = 0
    pradar = pygame.image.load("radar.png")
    while True: #PRESTON HELPED WITH MENU
        angle += 1
        # SCREEN.fill(BLACK)
        # block = 50  # Set the size of the grid block
        # for x in range(0, WINDOW_WIDTH, block):
        #     for y in range(0, WINDOW_HEIGHT, block):
        #         rect = pygame.Rect(x, y, block, block)
        #         pygame.draw.rect(SCREEN, GREEN, rect, 1)
        bbattleship = (bbx, bby, 300, 75)
        bclassic = (bcx, bcy, 200, 50)
        bmultiplayer = (bmx, bmy, 200, 50)
        bpower_up = (bpx, bpy, 200, 50)
        radar = (rx, ry, 250, 20)
        # rotate= pygame.transform.rotate(radar, angle)
        # pygame.draw.rect(SCREEN, BLUE, radar, 0)
        pygame.draw.rect(pradar, BLACK, bbattleship, 0)
        pygame.draw.rect(pradar, BLACK, bpower_up, 0)
        pygame.draw.rect(pradar, BLACK, bmultiplayer, 0)
        pygame.draw.rect(pradar, BLACK, bclassic, 0)

        SCREEN.blit(pradar, (0, 0))
        SCREEN.blit(classic, (bcx + 13, bcy))
        SCREEN.blit(battleship, (bbx + 13, bby))
        SCREEN.blit(multiplayer, (bcx + 20, bmy))
        SCREEN.blit(power, (bpx + 20, bpy))
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN: #BUTTONS FOR GOING TO DIFFERENT GAME MODES

                if rectc.collidepoint(pygame.mouse.get_pos()):
                    CLASSIC()
                elif rectm.collidepoint(pygame.mouse.get_pos()):
                    CLASSIC()
                elif rectp.collidepoint(pygame.mouse.get_pos()):
                    POWER()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()



