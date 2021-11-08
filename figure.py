import pygame

class Figure(object):
    def __init__(self,type):
        self.type = type
        if self.type == "wQ":
            self.image = pygame.image.load("wQ.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 303
            self.y = 707
            self.figure_draging = False
            self.box = pygame.Rect(self.x,self.y,101,101)
        elif self.type == "wK":
            self.image = pygame.image.load("wK.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 404
            self.y = 707
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "wB":
            self.image = pygame.image.load("wB.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 202
            self.y = 707
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "wB2":
            self.image = pygame.image.load("wB.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 505
            self.y = 707
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "wN":
            self.image = pygame.image.load("wN.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 101
            self.y = 707
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "wN2":
            self.image = pygame.image.load("wN.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 606
            self.y = 707
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "wR":
            self.image = pygame.image.load("wR.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 0
            self.y = 707
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "wR2":
            self.image = pygame.image.load("wR.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 707
            self.y = 707
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)

        elif self.type =="wp1":
            self.image = pygame.image.load("wp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 0
            self.y = 606
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="wp2":
            self.image = pygame.image.load("wp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 101
            self.y = 606
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="wp3":
            self.image = pygame.image.load("wp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 202
            self.y = 606
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="wp4":
            self.image = pygame.image.load("wp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 303
            self.y = 606
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="wp5":
            self.image = pygame.image.load("wp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 404
            self.y = 606
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="wp6":
            self.image = pygame.image.load("wp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 505
            self.y = 606
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="wp7":
            self.image = pygame.image.load("wp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 606
            self.y = 606
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="wp8":
            self.image = pygame.image.load("wp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 707
            self.y = 606
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)


        elif self.type == "bQ":
            self.image = pygame.image.load("bQ.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 303
            self.y = 0
            self.figure_draging = False
            self.box = pygame.Rect(self.x,self.y,101,101)
        elif self.type == "bK":
            self.image = pygame.image.load("bK.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 404
            self.y = 0
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "bB":
            self.image = pygame.image.load("bB.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 202
            self.y = 0
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "bB2":
            self.image = pygame.image.load("bB.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 505
            self.y = 0
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "bN":
            self.image = pygame.image.load("bN.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 101
            self.y = 0
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "bN2":
            self.image = pygame.image.load("bN.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 606
            self.y = 0
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "bR":
            self.image = pygame.image.load("bR.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 0
            self.y = 0
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type == "bR2":
            self.image = pygame.image.load("bR.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 707
            self.y = 0
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)

        elif self.type =="bp1":
            self.image = pygame.image.load("bp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 0
            self.y = 101
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="bp2":
            self.image = pygame.image.load("bp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 101
            self.y = 101
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="bp3":
            self.image = pygame.image.load("bp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 202
            self.y = 101
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="bp4":
            self.image = pygame.image.load("bp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 303
            self.y = 101
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="bp5":
            self.image = pygame.image.load("bp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 404
            self.y = 101
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="bp6":
            self.image = pygame.image.load("bp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 505
            self.y = 101
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="bp7":
            self.image = pygame.image.load("bp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 606
            self.y = 101
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
        elif self.type =="bp8":
            self.image = pygame.image.load("bp.png")
            self.image = pygame.transform.scale(self.image, (101, 101))
            self.x = 707
            self.y = 101
            self.figure_draging = False
            self.box = pygame.Rect(self.x, self.y, 101, 101)
    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))