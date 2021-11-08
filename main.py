import pygame
import sys
from board import Board
from moves import move


class Game(object):
    def __init__(self):
        #config
        self.tps_max = 60.0

        #initialization
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((1000,808))
        self.tps_clock = pygame.time.Clock()
        self.delta = 0.0
        self.s_number = 1
        self.s_number2 = 2
        self.none = False
        self.white_allowed = True
        self.black_allowed = False
        self.step_iterator=1
        self.font = pygame.font.SysFont("Comic Sans MS", 24)
        self.white_time = 600
        self.black_time = 600
        self.time1 = self.font.render(str(int(self.black_time/60))+":"+str(self.black_time%60),False,(255,255,255))
        self.time2 = self.font.render(str(int(self.white_time/60))+":"+str(self.white_time%60),False,(255,255,255))
        self.white_check = False
        self.black_check = False
        self.white_King_pos = 0
        self.black_King_pos = 0

        self.board = Board(self.screen)

        while(True):
            if self.white_time==0:
                print("Black wins!")
                break
            elif self.black_time==0:
                print("White wins!")
                break
            elif (self.step_iterator % 2 == 0):
                self.white_allowed = False
                self.black_allowed = True
            else:
                self.white_allowed = True
                self.black_allowed = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        n1 = int((pos[0]/101)+1)
                        n2 = int(pos[1]/101)
                        self.s_number = n1+n2*8
                        if self.board.square_list[self.s_number].figure != None:
                            if self.board.square_list[self.s_number].figure.box.collidepoint(pos):
                                self.board.square_list[self.s_number].figure_draging = True
                                pos = pygame.mouse.get_pos()
                                self.offset_x = self.board.square_list[self.s_number].figure.x - pos[0]
                                self.offset_y = self.board.square_list[self.s_number].figure.y - pos[1]
                        else:
                            continue

                elif event.type == pygame.MOUSEMOTION:
                    if self.board.square_list[self.s_number].figure_draging:
                        pos = pygame.mouse.get_pos()
                        self.board.square_list[self.s_number].figure.x = pos[0]+self.offset_x
                        self.board.square_list[self.s_number].figure.y = pos[1]+self.offset_y
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.board.square_list[self.s_number].figure != None:
                            pos = pygame.mouse.get_pos()
                            n1 = int((pos[0] / 101) + 1)
                            n2 = int(pos[1] / 101)
                            self.s_number2 = n1 + n2 * 8
                            if(self.s_number!=self.s_number2):
                                if move(self.s_number,self.s_number2,self.board.square_list[self.s_number].figure.type,self.board,self.white_allowed,self.black_allowed):
                                    self.board.assign_figure(self.s_number2,self.board.square_list[self.s_number].figure.type)
                                    if self.step_iterator%2!=0:
                                        for i in self.board.square_list.values():
                                            if i.figure != None:
                                                if i.figure.type == "bK":
                                                    self.black_King_pos = i.number
                                        print(self.black_King_pos)
                                        print(self.s_number2)
                                        if move(self.s_number2,self.black_King_pos,self.board.square_list[self.s_number2].figure.type,self.board,self.white_allowed,self.black_allowed):
                                            self.black_check = True
                                    else:
                                        for i in self.board.square_list.values():
                                            if i.figure != None:
                                                if i.figure.type == "wK":
                                                    self.white_King_pos = i.number
                                        print(self.s_number2)
                                        print(self.white_King_pos)
                                        if move(self.s_number2,self.white_King_pos,self.board.square_list[self.s_number2].figure.type, self.board, self.white_allowed,self.black_allowed):
                                            self.white_check = True
                                    self.board.square_list[self.s_number2].figure.x = self.board.square_list[self.s_number2].x
                                    self.board.square_list[self.s_number2].figure.y = self.board.square_list[self.s_number2].y
                                    self.board.square_list[self.s_number2].figure.box = pygame.Rect(self.board.square_list[self.s_number2].x, self.board.square_list[self.s_number2].y, 101, 101)
                                    self.board.square_list[self.s_number].figure_draging = False
                                    self.board.square_list[self.s_number].figure = None
                                    self.step_iterator += 1
                                else:
                                    self.board.square_list[self.s_number].figure_draging = False
                                    self.board.square_list[self.s_number].figure.x = self.board.square_list[self.s_number].x
                                    self.board.square_list[self.s_number].figure.y = self.board.square_list[self.s_number].y
                                    self.board.square_list[self.s_number].figure.box = pygame.Rect(self.board.square_list[self.s_number].x,self.board.square_list[self.s_number].y, 101, 101)

                            else:
                                self.board.square_list[self.s_number].figure_draging = False
                                self.board.square_list[self.s_number].figure.x = self.board.square_list[self.s_number].x
                                self.board.square_list[self.s_number].figure.y = self.board.square_list[self.s_number].y
                                self.board.square_list[self.s_number].figure.box = pygame.Rect(self.board.square_list[self.s_number].x, self.board.square_list[self.s_number].y, 101, 101)
                                continue
                        else:
                            continue



            #ticking
            self.delta+=self.tps_clock.tick()/1000
            if(self.delta>1):
                if(self.white_allowed):
                    self.white_time-=int(self.delta)
                    self.time2 = self.font.render(str(int(self.white_time/60))+":"+str(self.white_time%60),False,(255,255,255))
                else:
                    self.black_time-=int(self.delta)
                    self.time1 = self.font.render(str(int(self.black_time/60))+":"+str(self.black_time%60),False,(255,255,255))
                self.delta-=1

            if self.white_check:
                print("White check")
                print(True)
            if self.black_check:
                print("Black check")
                print(True)
            self.screen.fill((100,100,100))
            self.draw()
            pygame.display.flip()



    def tick(self):
        pass

    def draw(self):
        self.board.draw_board()
        self.board.draw_figures()
        self.screen.blit(self.time1,(900,100))
        self.screen.blit(self.time2,(900,700))

    #def king_position(self,color):
       # if color == white:




if __name__ == "__main__":
    Game()