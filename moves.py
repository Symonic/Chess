white_pawn_list = ["wp1","wp2","wp3","wp4","wp5","wp6","wp7","wp8"]
black_pawn_list = ["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"]

def move(p1,p2,type,board,white_allowed,black_allowed): #white moves
    if ((type=="wN") or (type=="wN2")) and (white_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "w":
                return False
            elif (p1 - p2 == 15) or (p1 - p2 == 17) or (p1 - p2 == 6) or (p1 - p2 == 10) or (p1 - p2 == -6) or (
                    p1 - p2 == -10) or (p1 - p2 == -15) or (p1 - p2 == -17):
                return True
            else:
                return False
        elif (p1-p2==15) or (p1-p2==17) or (p1-p2==6) or (p1-p2==10) or (p1-p2==-6) or (p1-p2==-10) or (p1-p2==-15) or (p1-p2==-17):
            return True
        else:
            return False
    elif ((type=="wB") or (type=="wB2")) and (white_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "w":
                return False
            elif ((p1 - p2) % 7 == 0) or ((p1 - p2) % 9 == 0):
                if ((p1 - p2) % 7 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 7, p1, 7):
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 7, p2, 7):
                            if board.square_list[i].figure != None:
                                return False
                else:
                    if (p1 > p2):
                        for i in range(p2 + 9, p1, 9):
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 9, p2, 9):
                            if board.square_list[i].figure != None:
                                return False
                return True
            else:
                return False
        elif ((p1-p2)%7==0) or ((p1-p2)%9==0):
            if ((p1 - p2) % 7 == 0):
                if (p1 > p2):
                    for i in range(p2 + 7, p1, 7):
                        print(board.square_list[i].figure)
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 7, p2, 7):
                        if board.square_list[i].figure != None:
                            return False
            else:
                if (p1 > p2):
                    for i in range(p2 + 9, p1, 9):
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 9, p2, 9):
                        if board.square_list[i].figure != None:
                            return False
            return True
        else:
            return False
    elif ((type=="wR") or (type=="wR2")) and (white_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "w":
                return False
            elif ((p1 - p2) % 8 == 0) or ((p2 >= 1 + int((p1 - 1) / 8) * 8) and (p2 <= 8 + int((p1 - 1) / 8) * 8)):
                if ((p1 - p2) % 8 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 8, p1, 8):
                            print(board.square_list[i].figure)
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 8, p2, 8):
                            if board.square_list[i].figure != None:
                                return False
                else:
                    if (p1 > p2):
                        for i in range(p2 + 1, p1):
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 1, p2):
                            if board.square_list[i].figure != None:
                                return False
                return True
            else:
                return False
        elif ((p1-p2)%8==0) or ((p2>=1+int((p1-1)/8)*8) and (p2<=8+int((p1-1)/8)*8)):
            if((p1-p2)%8==0):
                if(p1>p2):
                    for i in range(p2+8,p1,8):
                        print(board.square_list[i].figure)
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1+8,p2,8):
                        if board.square_list[i].figure != None:
                            return False
            else:
                if(p1>p2):
                    for i in range(p2+1,p1):
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1+1,p2):
                        if board.square_list[i].figure != None:
                            return False
            return True
        else:
            return False
    elif (type=="wK") and (white_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "w":
                return False
            elif ((p1 - p2) == 1) or ((p1 - p2) == -1) or ((p1 - p2) == 8) or ((p1 - p2) == -8) or ((p1 - p2) == 9) or (
                    (p1 - p2) == -9) or ((p1 - p2) == 7) or ((p1 - p2) == -7):
                return True
            else:
                return False
        elif ((p1-p2)==1) or ((p1-p2)==-1) or ((p1-p2)==8) or ((p1-p2)==-8) or ((p1-p2)==9) or ((p1-p2)==-9) or ((p1-p2)==7) or ((p1-p2)==-7):
            return True
        else:
            return False
    elif (type=="wQ") and (white_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "w":
                return False
            elif ((p1 - p2) % 7 == 0) or ((p1 - p2) % 9 == 0) or ((p1 - p2) % 8 == 0) or (
                    (p2 >= 1 + int((p1 - 1) / 8) * 8) and (p2 <= 8 + int((p1 - 1) / 8) * 8)):
                if ((p1 - p2) % 7 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 7, p1, 7):
                            print(board.square_list[i].figure)
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 7, p2, 7):
                            if board.square_list[i].figure != None:
                                return False
                elif ((p1 - p2) % 9 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 9, p1, 9):
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 9, p2, 9):
                            if board.square_list[i].figure != None:
                                return False
                elif ((p1 - p2) % 8 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 8, p1, 8):
                            print(board.square_list[i].figure)
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 8, p2, 8):
                            if board.square_list[i].figure != None:
                                return False
                else:
                    if (p1 > p2):
                        for i in range(p2 + 1, p1):
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 1, p2):
                            if board.square_list[i].figure != None:
                                return False
                return True
            else:
                return False
        elif ((p1-p2)%7==0) or ((p1-p2)%9==0) or ((p1-p2)%8==0) or ((p2>=1+int((p1-1)/8)*8) and (p2<=8+int((p1-1)/8)*8)):
            if ((p1 - p2) % 7 == 0):
                if (p1 > p2):
                    for i in range(p2 + 7, p1, 7):
                        print(board.square_list[i].figure)
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 7, p2, 7):
                        if board.square_list[i].figure != None:
                            return False
            elif ((p1-p2)%9 == 0):
                if (p1 > p2):
                    for i in range(p2 + 9, p1, 9):
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 9, p2, 9):
                        if board.square_list[i].figure != None:
                            return False
            elif ((p1 - p2) % 8 == 0):
                if (p1 > p2):
                    for i in range(p2 + 8, p1, 8):
                        print(board.square_list[i].figure)
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 8, p2, 8):
                        if board.square_list[i].figure != None:
                            return False
            else:
                if (p1 > p2):
                    for i in range(p2 + 1, p1):
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 1, p2):
                        if board.square_list[i].figure != None:
                            return False
            return True
        else:
            return False
    elif ((type=="bN") or (type=="bN2")) and (black_allowed==True): #black moves
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "b":
                return False
            elif (p1 - p2 == 15) or (p1 - p2 == 17) or (p1 - p2 == 6) or (p1 - p2 == 10) or (p1 - p2 == -6) or (
                    p1 - p2 == -10) or (p1 - p2 == -15) or (p1 - p2 == -17):
                return True
            else:
                return False
        elif (p1-p2==15) or (p1-p2==17) or (p1-p2==6) or (p1-p2==10) or (p1-p2==-6) or (p1-p2==-10) or (p1-p2==-15) or (p1-p2==-17):
            return True
        else:
            return False
    elif ((type=="bB") or (type=="bB2")) and (black_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "b":
                return False
            elif ((p1 - p2) % 7 == 0) or ((p1 - p2) % 9 == 0):
                if ((p1 - p2) % 7 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 7, p1, 7):
                            print(board.square_list[i].figure)
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 7, p2, 7):
                            if board.square_list[i].figure != None:
                                return False
                else:
                    if (p1 > p2):
                        for i in range(p2 + 9, p1, 9):
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 9, p2, 9):
                            if board.square_list[i].figure != None:
                                return False
                return True
            else:
                return False
        elif ((p1-p2)%7==0) or ((p1-p2)%9==0):
            if ((p1 - p2) % 7 == 0):
                if (p1 > p2):
                    for i in range(p2 + 7, p1, 7):
                        print(board.square_list[i].figure)
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 7, p2, 7):
                        if board.square_list[i].figure != None:
                            return False
            else:
                if (p1 > p2):
                    for i in range(p2 + 9, p1, 9):
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 9, p2, 9):
                        if board.square_list[i].figure != None:
                            return False
            return True
        else:
            return False
    elif ((type=="bR") or (type=="bR2")) and (black_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "b":
                return False
            elif ((p1 - p2) % 8 == 0) or ((p2 >= 1 + int((p1 - 1) / 8) * 8) and (p2 <= 8 + int((p1 - 1) / 8) * 8)):
                if ((p1 - p2) % 8 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 8, p1, 8):
                            print(board.square_list[i].figure)
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 8, p2, 8):
                            if board.square_list[i].figure != None:
                                return False
                else:
                    if (p1 > p2):
                        for i in range(p2 + 1, p1):
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 1, p2):
                            if board.square_list[i].figure != None:
                                return False
                return True
            else:
                return False
        elif ((p1-p2)%8==0) or ((p2>=1+int((p1-1)/8)*8) and (p2<=8+int((p1-1)/8)*8)):
            if((p1-p2)%8==0):
                if(p1>p2):
                    for i in range(p2+8,p1,8):
                        print(board.square_list[i].figure)
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1+8,p2,8):
                        if board.square_list[i].figure != None:
                            return False
            else:
                if(p1>p2):
                    for i in range(p2+1,p1):
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1+1,p2):
                        if board.square_list[i].figure != None:
                            return False
            return True
        else:
            return False
    elif (type=="bK") and (black_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "b":
                return False
            elif ((p1 - p2) == 1) or ((p1 - p2) == -1) or ((p1 - p2) == 8) or ((p1 - p2) == -8) or ((p1 - p2) == 9) or (
                    (p1 - p2) == -9) or ((p1 - p2) == 7) or ((p1 - p2) == -7):
                return True
            else:
                return False
        elif ((p1-p2)==1) or ((p1-p2)==-1) or ((p1-p2)==8) or ((p1-p2)==-8) or ((p1-p2)==9) or ((p1-p2)==-9) or ((p1-p2)==7) or ((p1-p2)==-7):
            return True
        else:
            return False
    elif (type=="bQ") and (black_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "b":
                return False
            elif ((p1 - p2) % 7 == 0) or ((p1 - p2) % 9 == 0) or ((p1 - p2) % 8 == 0) or (
                    (p2 >= 1 + int((p1 - 1) / 8) * 8) and (p2 <= 8 + int((p1 - 1) / 8) * 8)):
                if ((p1 - p2) % 7 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 7, p1, 7):
                            print(board.square_list[i].figure)
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 7, p2, 7):
                            if board.square_list[i].figure != None:
                                return False
                elif ((p1 - p2) % 9 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 9, p1, 9):
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 9, p2, 9):
                            if board.square_list[i].figure != None:
                                return False
                elif ((p1 - p2) % 8 == 0):
                    if (p1 > p2):
                        for i in range(p2 + 8, p1, 8):
                            print(board.square_list[i].figure)
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 8, p2, 8):
                            if board.square_list[i].figure != None:
                                return False
                else:
                    if (p1 > p2):
                        for i in range(p2 + 1, p1):
                            if board.square_list[i].figure != None:
                                return False
                    else:
                        for i in range(p1 + 1, p2):
                            if board.square_list[i].figure != None:
                                return False
                return True
            else:
                return False
        elif ((p1-p2)%7==0) or ((p1-p2)%9==0) or ((p1-p2)%8==0) or ((p2>=1+int((p1-1)/8)*8) and (p2<=8+int((p1-1)/8)*8)):
            if ((p1 - p2) % 7 == 0):
                if (p1 > p2):
                    for i in range(p2 + 7, p1, 7):
                        print(board.square_list[i].figure)
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 7, p2, 7):
                        if board.square_list[i].figure != None:
                            return False
            elif ((p1-p2)%9 == 0):
                if (p1 > p2):
                    for i in range(p2 + 9, p1, 9):
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 9, p2, 9):
                        if board.square_list[i].figure != None:
                            return False
            elif ((p1 - p2) % 8 == 0):
                if (p1 > p2):
                    for i in range(p2 + 8, p1, 8):
                        print(board.square_list[i].figure)
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 8, p2, 8):
                        if board.square_list[i].figure != None:
                            return False
            else:
                if (p1 > p2):
                    for i in range(p2 + 1, p1):
                        if board.square_list[i].figure != None:
                            return False
                else:
                    for i in range(p1 + 1, p2):
                        if board.square_list[i].figure != None:
                            return False
            return True
        else:
            return False


    elif type in white_pawn_list and (white_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "w":
                return False
            elif ((p1 - p2) == 8):
                return True
            elif ((p1 - p2 == 7)) and (board.square_list[p1 - 7].figure != None):
                return True
            elif ((p1 - p2 == 9)) and (board.square_list[p1 - 9].figure != None):
                return True
            elif ((p1 - p2 == 16)) and (int((p1-1)/8)==6):
                return True
            else:
                return False
        elif ((p1-p2)==8):
            return True
        elif ((p1-p2==7)) and (board.square_list[p1-7].figure != None):
            return True
        elif ((p1-p2==9)) and (board.square_list[p1-9].figure != None):
            return True
        elif ((p1 - p2 == 16)) and (int((p1 - 1) / 8) == 6):
            return True
        else:
            return False
    elif type in black_pawn_list and (black_allowed==True):
        if board.square_list[p2].figure != None:
            if board.square_list[p2].figure.type[0] == "b":
                return False
            elif ((p1 - p2) == -8):
                return True
            elif ((p1 - p2 == -7)) and (board.square_list[p1 + 7].figure != None):
                return True
            elif ((p1 - p2 == -9)) and (board.square_list[p1 + 9].figure != None):
                return True
            elif ((p1 - p2 == -16)) and (int((p1-1)/8)==1):
                return True
            else:
                return False
        elif ((p1-p2)==-8):
            return True
        elif ((p1-p2==-7)) and (board.square_list[p1+7].figure != None):
            return True
        elif ((p1-p2==-9)) and (board.square_list[p1+9].figure != None):
            return True
        elif ((p1 - p2 == -16)) and (int((p1 - 1) / 8) == 1):
            return True
        else:
            return False