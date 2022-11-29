# import pygame
# from random import randrange
#
#
# class Ship:
#     def __init__(self):
#         WINDOW_HEIGHT = 500
#         WINDOW_WIDTH = 500
#         SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#
#         RED= (223,0,0)
#         self.ship1x = randrange(0, 500, 50)
#         self.ship1y = randrange(0, 500, 50)
#         self.ship1 = (self.ship1x, self.ship1y, 200, 50) # x placement, y placment, dimension\
#         self.ship1rect= self.ship1
#         self.ship1=pygame.draw.rect(SCREEN, RED, self.ship1, 0)
#
#     # def draw (self, surface):
#     #     surface.blit(self.ship11, self.ship1rect)
#     def get_rect(self):
#         print(self.ship1)