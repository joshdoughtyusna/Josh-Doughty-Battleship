import sys
import time
import pygame
from random import randrange
import time
BLACK = (0, 0, 0)
GREY= (100,100,100)
GREEN = (0, 223, 0)
RED= (223,0,0)
BLUE=(0,0,223)
PURPLE= (123,45,233)
WHITE= (233,233,233)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
# pygame.SYSTEM_CURSOR_CROSSHAIR
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BG = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("BATTLESHIP")

def main():
    pygame.init()
    SCREEN.fill(BLACK)

    ship1x = randrange(0,500,50)
    ship1y = randrange(0,500,50)
    ship1 = (ship1x, ship1y, 200, 50)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, RED, ship1, 0)
    ship2x = randrange(0, 500, 50)
    ship2y = randrange(0, 500, 50)
    ship2 = (ship2x, ship2y, 150, 50)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, BLUE, ship2, 0)
    ship3x = randrange(0, 500, 50)
    ship3y = randrange(0, 500, 50)
    ship3 = (ship3x, ship3y, 50, 200)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, PURPLE, ship3, 0)
    ship4x = randrange(0, 500, 50)
    ship4y = randrange(0, 500, 50)
    ship4 = (ship4x, ship4y, 50, 100)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, GREEN, ship4, 0)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound("can.mp3").play()
                mousex, mousey = pygame.mouse.get_pos()
                print(mousex, mousey)
                if mousex == ship1x and mousey == ship1y:
                    pygame.draw.rect(SCREEN, WHITE, ship1, 0)

                else:

                    hit = (mousex, mousey, 50, 50)
                    pygame.draw.rect(SCREEN, WHITE, hit, 0)


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # hitx = 0
        # hity = 0
        # for x in range(0,500,50):
        #     if x == ship1x:
        #         hitx = ship1x
        #         hity = ship1y
        #         hit = (hitx, hity, 50, 50)
        #         pygame.draw.rect(SCREEN, WHITE, hit, 0)
        #         time.sleep(0.5)
        #     elif x == ship2x:
        #         hitx = ship2x
        #         hity = ship2y
        #         hit = (hitx, hity, 50, 50)
        #         pygame.draw.rect(SCREEN, WHITE, hit, 0)
        #         time.sleep(0.5)
        #     elif x == ship3x:
        #         hitx = ship3x
        #         hity = ship3y
        #         hit = (hitx, hity, 50, 50)
        #         pygame.draw.rect(SCREEN, WHITE, hit, 0)
        #         time.sleep(0.5)
        #     elif x == ship4x:
        #         hitx = ship4x
        #         hity = ship4y
        #         hit = (hitx, hity, 50, 50)
        #         pygame.draw.rect(SCREEN, WHITE, hit, 0)
        #         time.sleep(0.5)
        #     else:
        #         miss=(randrange(0,500,50),randrange(0,500,50),50,50)
        #         pygame.draw.rect(SCREEN, GREY, miss, 0)



            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    block = 50 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, block):
        for y in range(0, WINDOW_HEIGHT, block):
            rect = pygame.Rect(x, y, block, block)
            pygame.draw.rect(SCREEN, GREEN, rect, 1)
    # ship1x = randint(0,400)
    # ship1y = randint(0,400)
    # ship1= (ship1x,ship1y,50,200) #x placement, y placment, dimension
    # pygame.draw.rect(SCREEN, RED, ship1, 0)
    # ship2 = (400, 200, 100, 50)  # x placement, y placment, dimension
    # pygame.draw.rect(SCREEN, RED, ship2, 0)
    # ship3 = (100, 400, 300, 50)  # x placement, y placment, dimension
    # pygame.draw.rect(SCREEN, RED, ship3, 0)
    # ship4 = (0, 0, 50, 50)  # x placement, y placment, dimension
    # pygame.draw.rect(SCREEN, RED, ship4, 0)
main()