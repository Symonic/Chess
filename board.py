from square import Square
from figure import Figure

class Board(object):
    def __init__(self,screen):
        self.square_list = {}
        self.figure_list = {}
        self.Screen = screen
        self.initialize_square_list()
        self.initialize_figure_list()

        self.assign_figure(1,"bR")
        self.assign_figure(2,"bN")
        self.assign_figure(3,"bB")
        self.assign_figure(4,"bQ")
        self.assign_figure(5,"bK")
        self.assign_figure(6,"bB2")
        self.assign_figure(7,"bN2")
        self.assign_figure(8,"bR2")
        for i in range(1,9):
            self.assign_figure(i+8,"bp{}".format(i))
        for j in range(1,9):
            self.assign_figure(j+48,"wp{}".format(j)) #bladdddddd --------------------------------
        self.assign_figure(57, "wR")
        self.assign_figure(58, "wN")
        self.assign_figure(59, "wB")
        self.assign_figure(60, "wQ")
        self.assign_figure(61, "wK")
        self.assign_figure(62, "wB2")
        self.assign_figure(63, "wN2")
        self.assign_figure(64, "wR2")

    def initialize_square_list(self):
        iter = 1
        for i in range(0,8):
            for j in range(0,8):
                if (i+j)%2==0:
                    self.square_list[iter] = Square(j*101, i*101, (255,255,255), iter)
                    iter+=1
                else:
                    self.square_list[iter] = Square(j*101, i*101, (50,51,52), iter)
                    iter+=1

    def initialize_figure_list(self):
        self.figure_list["wQ"]=Figure("wQ")
        self.figure_list["wK"]=Figure("wK")
        self.figure_list["wB"]=Figure("wB")
        self.figure_list["wB2"]=Figure("wB2")
        self.figure_list["wN"]=Figure("wN")
        self.figure_list["wN2"]=Figure("wN2")
        self.figure_list["wR"]=Figure("wR")
        self.figure_list["wR2"]=Figure("wR2")

        self.figure_list["bQ"]=Figure("bQ")
        self.figure_list["bK"]=Figure("bK")
        self.figure_list["bB"]=Figure("bB")
        self.figure_list["bB2"]=Figure("bB2")
        self.figure_list["bN"]=Figure("bN")
        self.figure_list["bN2"]=Figure("bN2")
        self.figure_list["bR"]=Figure("bR")
        self.figure_list["bR2"]=Figure("bR2")

        for i in range(1,9):
            self.figure_list["wp{}".format(i)]=Figure("wp{}".format(i))
            self.figure_list["bp{}".format(i)]=Figure("bp{}".format(i))

    def assign_figure(self,number,figure):
        self.square_list[number].figure = self.figure_list[figure]

    def draw_board(self):
        for s in self.square_list.values():
            s.draw(self.Screen)
    def draw_figures(self):
        for s in self.square_list.values():
            if(s.figure!=None):
                s.figure.draw(self.Screen)