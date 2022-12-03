import time
import sys
import time
import pygame
from ship import Ship
from random import randrange

def MULTIPLAYER():
    import time
    import sys
    import time
    import pygame
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
    end = (100, 100, 300, 200)
    pygame.init()
    YOURSHIPS = 4
    ENEMYSHIPS = 4
    game= True





    # Ship()

    # CREATES 8 SHIPS RANDOMLY PLACED ON GRID
    while True:
        s1x = randrange(0, 500, 50)
        if s1x <= 300:
            ship1x = s1x

            break
    while True:
        s1y = randrange(0, 500, 50)
        if s1y <= 450:
            ship1y = s1y

            break
    while True:
        s2x = randrange(0, 500, 50)
        if s2x != ship1x and s2x <= 350:
            ship2x = s2x
            break
    while True:
        s2y = randrange(0, 500, 50)
        if s2y != ship1y and s2x <= 450:
            ship2y = s2y
            break
    while True:
        s3x = randrange(0, 500, 50)
        if s3x != ship1x and s3x != ship2x and s3x <= 450:
            ship3x = s3x
            break
    while True:
        s3y = randrange(0, 500, 50)
        if s3y != ship1y and s3y != ship2y and s3y <= 250:
            ship3y = s3y
            break
    while True:
        s4x = randrange(0, 500, 50)
        if s4x != ship1x and s4x != ship2x and s4x != ship3x and s4x <= 450:
            ship4x = s4x
            break
    while True:
        s4y = randrange(0, 500, 50)
        if s4y != ship1y and s4y != ship2y and s4y != ship3y and s4y <= 250:
            ship4y = s4y
            break
    #     #Enemy ship placement_______________________________________
    while True:
        s5x = randrange(0, 500, 50)
        if s5x <= 350:
            ship5x = s5x
            break
    while True:
        s5y = randrange(0, 500, 50)
        if s5y <= 450:
            ship5y = s5y
            break
    while True:
        s6x = randrange(0, 500, 50)
        if s6x != ship5x and s6x <= 350:
            ship6x = s6x
            break
    while True:
        s6y = randrange(0, 500, 50)
        if s6y != ship5y and s6x <= 450:
            ship6y = s6y
            break
    while True:
        s7x = randrange(0, 500, 50)
        if s7x != ship5x and s7x != ship6x and s7x <= 450:
            ship7x = s7x
            break
    while True:
        s7y = randrange(0, 500, 50)
        if s7y != ship5y and s7y != ship6y and s7y <= 250:
            ship7y = s7y
            break
    while True:
        s8x = randrange(0, 500, 50)
        if s8x != ship5x and s8x != ship6x and s8x != ship7x and s8x <= 450:
            ship8x = s8x
            break
    while True:
        s8y = randrange(0, 500, 50)
        if s8y != ship5y and s8y != ship6y and s8y != ship7y and s8y <= 250:
            ship8y = s8y
            break
    ship1 = (ship1x, ship1y, 200, 50)
    pygame.draw.rect(SCREEN, RED, ship1, 0)
    ship2 = (ship2x, ship2y, 150, 50)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, RED, ship2, 0)
    ship3 = (ship3x, ship3y, 50, 200)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, RED, ship3, 0)
    ship4 = (ship4x, ship4y, 50, 100)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, RED, ship4, 0)
    # #Enemy ships
    ship5 = (ship5x, ship5y, 200, 50)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, GREEN, ship5, 0)
    ship6 = (ship6x, ship6y, 150, 50)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, GREEN, ship6, 0)
    ship7 = (ship7x, ship7y, 50, 200)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, GREEN, ship7, 0)
    ship8 = (ship8x, ship8y, 50, 100)  # x placement, y placment, dimension
    pygame.draw.rect(SCREEN, GREEN, ship8, 0)
    s1 = False

    s2 = False
    s3 = False
    s4 = False
    e1 = False
    e2 = False
    e3 = False
    e4 = False
    still1 = True
    still2 = True
    still3 = True
    still4 = True
    still5 = True
    still6 = True
    still7 = True
    still8 = True
    shots = 0
    grid = True
    while True:
        # drawGrid()
        if grid == True:
            block = 50  # Set the size of the grid block
            for x in range(0, WINDOW_WIDTH, block):
                for y in range(0, WINDOW_HEIGHT, block):
                    rect = pygame.Rect(x, y, block, block)
                    pygame.draw.rect(SCREEN, GREEN, rect, 1)

        # # CHECKS TO SEE IF THE MOUSE COORDINATES = SHIPCOORDINATES
        # for event in pygame.event.get():
        #
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         # pygame.mixer.Sound("hit.wav").play()
        #         shots += 1
        #         mousex, mousey = pygame.mouse.get_pos()
        #
        #         rect1 = pygame.Rect(ship1x, ship1y, 200, 50)
        #         rect2 = pygame.Rect(ship2x, ship2y, 150, 50)
        #         rect3 = pygame.Rect(ship3x, ship3y, 50, 200)
        #         rect4 = pygame.Rect(ship4x, ship4y, 50, 100)
        #         rect5 = pygame.Rect(ship5x, ship5y, 200, 50)
        #         rect6 = pygame.Rect(ship6x, ship6y, 150, 50)
        #         rect7 = pygame.Rect(ship7x, ship7y, 50, 200)
        #         rect8 = pygame.Rect(ship8x, ship8y, 50, 100)
        #         if rect1.collidepoint(pygame.mouse.get_pos()):
        #             pygame.draw.rect(SCREEN, RED, ship1, 0)
        #             s1 = True
        #
        #         elif rect2.collidepoint(pygame.mouse.get_pos()):
        #             pygame.draw.rect(SCREEN, RED, ship2, 0)
        #             s2 = True
        #
        #         elif rect3.collidepoint(pygame.mouse.get_pos()):
        #             pygame.draw.rect(SCREEN, RED, ship3, 0)
        #             s3 = True
        #
        #         elif rect4.collidepoint(pygame.mouse.get_pos()):
        #             pygame.draw.rect(SCREEN, RED, ship4, 0)
        #             s4 = True
        #
        #
        #
        #
        #         else:
        #             hit = (mousex, mousey, 10, 10)
        #             pygame.draw.rect(SCREEN, WHITE, hit, 0)
        #
        #         cx = randrange(0, 500, 50)
        #         cy = randrange(0, 500, 50)
        #
        #         cshot = (cx, cy, 50, 50)
        #         eshot = (cx, cy, 50, 50)
        #
        #         # pygame.draw.rect(SCREEN, BLUE, cshot, 0)
        #         # time.sleep(0.3)
        #
        #         # pygame.draw.rect(SCREEN, BLACK, cshot, 0)
        #         if rect5.collidepoint(cx, cy):
        #             pygame.draw.rect(SCREEN, BLACK, ship5, 0)
        #             e1 = True
        #
        #         elif rect6.collidepoint(cx, cy):
        #             pygame.draw.rect(SCREEN, BLACK, ship6, 0)
        #             e2 = True
        #
        #         elif rect7.collidepoint(cx, cy):
        #             pygame.draw.rect(SCREEN, BLACK, ship7, 0)
        #             e3 = True
        #
        #         elif rect8.collidepoint(cx, cy):
        #             pygame.draw.rect(SCREEN, BLACK, ship8, 0)
        #             e4 = True
        #
        #         if s1 == True:
        #             if still1 == True:
        #                 YOURSHIPS -= 1
        #                 still1 = False
        #
        #         if s2 == True:
        #             if still2 == True:
        #                 YOURSHIPS -= 1
        #                 still2 = False
        #
        #         if s3 == True:
        #             if still3 == True:
        #                 YOURSHIPS -= 1
        #                 still3 = False
        #
        #         if s4 == True:
        #             if still4 == True:
        #                 YOURSHIPS -= 1
        #                 still4 = False
        #
        #         if e1 == True:
        #             if still5 == True:
        #                 ENEMYSHIPS -= 1
        #                 still5 = False
        #                 # sfont = pygame.font.SysFont('impact', 20)
        #                 # space = sfont.render('PRESS SPACE TO CONTINUE', True, RED)
        #                 # losts = sfont.render('YOU LOST A SHIP', True, RED)
        #                 # pygame.display.set_caption("YOU LOST")
        #                 # pygame.draw.rect(SCREEN, BLACK, end, 0)
        #                 # SCREEN.blit(losts, (180, 125))
        #                 # SCREEN.blit(space, (150, 200))
        #                 # grid = False
        #         if e2 == True:
        #             if still6 == True:
        #                 ENEMYSHIPS -= 1
        #                 still6 = False
        #                 # sfont = pygame.font.SysFont('impact', 20)
        #                 # space = sfont.render('PRESS SPACE TO CONTINUE', True, RED)
        #                 # losts = sfont.render('YOU LOST A SHIP', True, RED)
        #                 # pygame.display.set_caption("YOU LOST")
        #                 # pygame.draw.rect(SCREEN, BLACK, end, 0)
        #                 # SCREEN.blit(losts, (180, 125))
        #                 # SCREEN.blit(space, (150, 200))
        #                 # grid = False
        #         if e3 == True:
        #             if still7 == True:
        #                 ENEMYSHIPS -= 1
        #                 still7 = False
        #                 # sfont = pygame.font.SysFont('impact', 20)
        #                 # space = sfont.render('PRESS SPACE TO CONTINUE', True, RED)
        #                 # losts = sfont.render('YOU LOST A SHIP', True, RED)
        #                 # pygame.display.set_caption("YOU LOST")
        #                 # pygame.draw.rect(SCREEN, BLACK, end, 0)
        #                 # SCREEN.blit(losts, (180, 125))
        #                 # SCREEN.blit(space, (150, 200))
        #                 # grid = False
        #         if e4 == True:
        #             if still8 == True:
        #                 ENEMYSHIPS -= 1
        #                 still8 = False
        #                 # sfont = pygame.font.SysFont('impact', 20)
        #                 # space = sfont.render('PRESS SPACE TO CONTINUE', True, RED)
        #                 # losts = sfont.render('YOU LOST A SHIP', True, RED)
        #                 # pygame.display.set_caption("YOU LOST")
        #                 # pygame.draw.rect(SCREEN, BLACK, end, 0)
        #                 # SCREEN.blit(losts, (180, 125))
        #                 # SCREEN.blit(space, (150, 200))
        #                 # grid = False
        #         print(F'You have made {shots} shots')
        #         print(f"You Have {ENEMYSHIPS} ships left")
        #         print(f"You Have {YOURSHIPS}  enemy ships left")
        #
        #         if e1 == True and e2 == True and e3 == True and e4 == True:
        #             pradar = pygame.image.load("radar.png")
        #             SCREEN.blit(pradar, (0, 0))
        #             font = pygame.font.SysFont('impact', 60)
        #             sfont = pygame.font.SysFont('impact', 30)
        #             quit = sfont.render('Press q to quit', True, BLACK)
        #             lost = font.render('YOU LOST', True, BLACK)
        #             pygame.display.set_caption("YOU LOST")
        #             pygame.draw.rect(SCREEN, GREEN, end, 0)
        #             SCREEN.blit(lost, (140, 100))
        #             SCREEN.blit(quit, (165, 250))
        #             grid = False
        #         if s1 == True and s2 == True and s3 == True and s4 == True:
        #             pradar = pygame.image.load("radar.png")
        #             SCREEN.blit(pradar, (0, 0))
        #             pygame.display.set_caption("YOU WON")
        #             font = pygame.font.SysFont('impact', 60)
        #             sfont = pygame.font.SysFont('impact', 30)
        #             quit = sfont.render('Press q to quit', True, WHITE)
        #             win = font.render('YOU WON', True, WHITE)
        #             pygame.display.set_caption("YOU LOST")
        #             pygame.draw.rect(SCREEN, BLACK, end, 0)
        #             SCREEN.blit(win, (140, 100))
        #             SCREEN.blit(quit, (165, 250))
        #             grid = False
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_q:  # PRESTON WILSON HELPED
        #             pygame.quit()
        #             sys.exit()
        #
        #         if event.key == pygame.K_SPACE:
        #             grid = True
        #             pygame.draw.rect(SCREEN, BLACK, end, 0)
        #
        #     if event.type == pygame.QUIT:
        #         pygame.quit
        #
        #         sys.exit()
    def p1 ():

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                # pygame.mixer.Sound("hit.wav").play()

                mousex, mousey = pygame.mouse.get_pos()

                rect1 = pygame.Rect(ship1x, ship1y, 200, 50)
                rect2 = pygame.Rect(ship2x, ship2y, 150, 50)
                rect3 = pygame.Rect(ship3x, ship3y, 50, 200)
                rect4 = pygame.Rect(ship4x, ship4y, 50, 100)

                if rect1.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(SCREEN, RED, ship1, 0)
                    s1 = True

                elif rect2.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(SCREEN, RED, ship2, 0)
                    s2 = True

                elif rect3.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(SCREEN, RED, ship3, 0)
                    s3 = True

                elif rect4.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(SCREEN, RED, ship4, 0)
                    s4 = True
                else:
                    hit = (mousex, mousey, 10, 10)
                    pygame.draw.rect(SCREEN, WHITE, hit, 0)

    def p2():

        rect5 = pygame.Rect(ship5x, ship5y, 200, 50)
        rect6 = pygame.Rect(ship6x, ship6y, 150, 50)
        rect7 = pygame.Rect(ship7x, ship7y, 50, 200)
        rect8 = pygame.Rect(ship8x, ship8y, 50, 100)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()




            if rect5.collidepoint(pygame.mouse.get_pos()):

                pygame.draw.rect(SCREEN, BLACK, ship5, 0)
                e1 = True

            elif rect6.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(SCREEN, BLACK, ship6, 0)
                e2 = True

            elif rect7.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(SCREEN, BLACK, ship7, 0)
                e3 = True

            elif rect8.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(SCREEN, BLACK, ship8, 0)
                e4 = True
            else:
                hit = (mousex, mousey, 10, 10)
                pygame.draw.rect(SCREEN, WHITE, hit, 0)
    def transition():
        SCREEN.fill(WHITE)

        if game == True:
            while True:
                p1()
                transition()
                p2()
                transition()
        pygame.display.update()
MULTIPLAYER()