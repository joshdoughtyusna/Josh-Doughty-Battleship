import math
import sys
from menu import Menu
import time
import pygame


def HOME():
    import sys
    import time
    import pygame
    BLACK = (0, 0, 0)
    GREY = (100, 100, 100)
    GREEN = (0, 223, 0)
    lgreen=(70,243,70)
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

    bmx = 150
    bmy = 400

    font = pygame.font.SysFont('Corbel', 50)
    bfont = pygame.font.SysFont('impact', 60)
    battleship = bfont.render("BATTLESHIP", True, GREEN)
    classic = font.render('CLASSIC', True, GREEN)
    multiplayer = bfont.render('PLAY', True, GREEN)
    power = font.render('POWER', True, GREEN)

    rectm = pygame.Rect(bmx, bmy, 200, 50)

    angle = 0

    PI=3.141592653



    while True: #PRESTON HELPED WITH MENU
        from math import pi
        # angle =0
        #generates the length of the line from angle
        x= 45 * math.sin(angle)* 225
        y= 45 * math.cos(angle)* 225
        #draw angle
        pygame.draw.line(SCREEN, GREEN,(250,250),(x,y),10)
        angle = angle - .01
        #resets angle back to 2pi
        if angle < 2*PI:
            angle = angle + 2*PI
        pygame.display.flip()
        time.sleep(0.03)


        grid = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        block = 50  # Set the size of the grid block
        for x in range(0, WINDOW_WIDTH, block):
            for y in range(0, WINDOW_HEIGHT, block):
                rect = pygame.Rect(x, y, block, block)
                pygame.draw.rect(SCREEN, GREEN, rect, 1)



        pygame.draw.circle(grid,GREEN,(250,250),50,4)

        pygame.draw.circle(grid, GREEN, (250, 250), 150, 4)

        pygame.draw.circle(grid, GREEN, (250, 250), 250, 4)
        if angle <= 11.0 and angle >= 10.6:
            pygame.draw.rect(SCREEN,RED,(50,200,50,50),0)
            pygame.mixer.Sound("Sonar.mp3").play()


        if angle <= 7.9 and angle >= 7.5:
            pygame.draw.rect(SCREEN, RED, (400, 250, 50, 50), 0)
            pygame.mixer.Sound("Sonar.mp3").play()

        if angle <= 12 and angle >= 11.5:
            pygame.draw.rect(SCREEN, RED, (150, 300, 50, 50), 0)
            pygame.mixer.Sound("Sonar.mp3").play()


        if angle <= 9.9 and angle >= 8.7:
            SCREEN.blit(battleship, (bbx + 13, bby+37))

            pygame.mixer.Sound("Sonar.mp3").play()

        # if angle <=13 and angle >=12.2:
        SCREEN.blit(multiplayer, (bcx + 45, bmy-13))


        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN: #BUTTONS FOR GOING TO DIFFERENT GAME MODES

                if rectm.collidepoint(pygame.mouse.get_pos()):

                    Menu()


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


HOME()
