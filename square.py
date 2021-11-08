import pygame

class Square(object):
    def __init__(self, x, y, color, number):
        self.color = color
        self.number = number
        self.x = x
        self.y = y
        self.box = (self.x, self.y, 101, 101)
        self.figure = None
        self.figure_draging = False
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.box)