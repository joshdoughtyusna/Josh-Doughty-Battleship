import sys
import pygame
from random import randrange

class Battleship:
    def __init__(self):
        pygame.init()
        self.BLACK = (0, 0, 0)
        self.GREY = (100, 100, 100)
        self.GREEN = (0, 223, 0)
        self.RED = (223, 0, 0)
        self.BLUE = (0, 0, 223)
        self.PURPLE = (123, 45, 233)
        self.WHITE = (233, 233, 233)
        self.WINDOW_HEIGHT = 500
        self.WINDOW_WIDTH = 500
        # pygame.SYSTEM_CURSOR_CROSSHAIR
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.BG = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("BATTLESHIP")
        self.end = (100, 100, 300, 200)
        pygame.init()
        YOURSHIPS = 4
        ENEMYSHIPS = 4
        self.game = True
    def create_ships(self):
        while True:
            self.s1x = randrange(0, 500, 50)
            if self.s1x <= 300:
                self.ship1x = self.s1x

                break
        while True:
            self.s1y = randrange(0, 500, 50)
            if self.s1y <= 450:
                self.ship1y = self.s1y

                break
        while True:
            self.s2x = randrange(0, 500, 50)
            if self.s2x != self.ship1x and self.s2x <= 350:
                self.ship2x = self.s2x
                break
        while True:
            self.s2y = randrange(0, 500, 50)
            if self.s2y != self.ship1y and self.s2x <= 450:
                self.ship2y = self.s2y
                break
        while True:
            self.s3x = randrange(0, 500, 50)
            if self.s3x != self.ship1x and self.s3x != self.ship2x and self.s3x <= 450:
                self.ship3x = self.s3x
                break
        while True:
            self.s3y = randrange(0, 500, 50)
            if self.s3y != self.ship1y and self.s3y != self.ship2y and self.s3y <= 250:
                self.ship3y = self.s3y
                break
        while True:
            self.s4x = randrange(0, 500, 50)
            if self.s4x != self.ship1x and self.s4x != self.ship2x and self.s4x != self.ship3x and self.s4x <= 450:
                self.ship4x = self.s4x
                break
        while True:
            self.s4y = randrange(0, 500, 50)
            if self.s4y != self.ship1y and self.s4y != self.ship2y and self.s4y != self.ship3y and self.s4y <= 250:
                self.ship4y = self.s4y
                break
        #     #Enemy ship placement_______________________________________
        while True:
            self.s5x = randrange(0, 500, 50)
            if self.s5x <= 350:
                self.ship5x = self.s5x
                break
        while True:
            self.s5y = randrange(0, 500, 50)
            if self.s5y <= 450:
                self.ship5y = self.s5y
                break
        while True:
            self.s6x = randrange(0, 500, 50)
            if self.s6x != self.ship5x and self.s6x <= 350:
                self.ship6x = self.s6x
                break
        while True:
            self.s6y = randrange(0, 500, 50)
            if self.s6y != self.ship5y and self.s6x <= 450:
                self.ship6y = self.s6y
                break
        while True:
            self.s7x = randrange(0, 500, 50)
            if self.s7x != self.ship5x and self.s7x != self.ship6x and self.s7x <= 450:
                self.ship7x = self.s7x
                break
        while True:
            self.s7y = randrange(0, 500, 50)
            if self.s7y != self.ship5y and self.s7y != self.ship6y and self.s7y <= 250:
                self.ship7y = self.s7y
                break
        while True:
            self.s8x = randrange(0, 500, 50)
            if self.s8x != self.ship5x and self.s8x != self.ship6x and self.s8x != self.ship7x and self.s8x <= 450:
                self.ship8x = self.s8x
                break
        while True:
            self.s8y = randrange(0, 500, 50)
            if self.s8y != self.ship5y and self.s8y != self.ship6y and self.s8y != self.ship7y and self.s8y <= 250:
                ship8y = self.s8y
                break
        self.ship1 = (self.ship1x, self.ship1y, 200, 50)
        pygame.draw.rect(self.SCREEN, self.RED, self.ship1, 0)
        self.ship2 = (self.ship2x, self.ship2y, 150, 50)  # x placement, y placment, dimension
        pygame.draw.rect(self.SCREEN, self.RED, self.ship2, 0)
        ship3 = (self.ship3x, self.ship3y, 50, 200)  # x placement, y placment, dimension
        pygame.draw.rect(self.SCREEN, self.RED, self.ship3, 0)
        ship4 = (self.ship4x, self.ship4y, 50, 100)  # x placement, y placment, dimension
        pygame.draw.rect(self.SCREEN, self.RED, ship4, 0)
        # #Enemy ships
        ship5 = (self.ship5x, self.ship5y, 200, 50)  # x placement, y placment, dimension
        pygame.draw.rect(self.SCREEN, self.GREEN, ship5, 0)
        ship6 = (self.ship6x, self.ship6y, 150, 50)  # x placement, y placment, dimension
        pygame.draw.rect(self.SCREEN, self.GREEN, ship6, 0)
        ship7 = (self.ship7x, self.ship7y, 50, 200)  # x placement, y placment, dimension
        pygame.draw.rect(self.SCREEN, self.GREEN, ship7, 0)
        ship8 = (self.ship8x, self.ship8y, 50, 100)  # x placement, y placment, dimension
        pygame.draw.rect(self.SCREEN, self.GREEN, ship8, 0)
        self.s1 = False

        self.s2 = False
        self.s3 = False
        self.s4 = False
        self.e1 = False
        self.e2 = False
        self.e3 = False
        self.e4 = False
        self.still1 = True
        self.still2 = True
        self.still3 = True
        self.still4 = True
        self.still5 = True
        self.still6 = True
        self.still7 = True
        self.still8 = True
    def draw_grid(self):
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.BG = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.block = 50  # Set the size of the grid block
        for x in range(0, self.WINDOW_WIDTH, self.block):
            for y in range(0, self.WINDOW_HEIGHT, self.block):
                rect = pygame.Rect(x, y, self.block, self.block)
                pygame.draw.rect(self.SCREEN, self.GREEN, rect, 1)
    def run(self):
        while True:
            Battleship.draw_grid()
            Battleship.create_ships()
            pygame.display.flip()



if __name__ == '__main__':
    Battleship.run()