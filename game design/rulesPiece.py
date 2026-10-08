# har currx is -7
# har curry se -2
# jisse it becomes a multiple of 78
import characters
from helper import isOccupied , isOpponent

def kingMove(piece):
    curr_x = piece.x
    curr_y = piece.y
    # print("Inside king move")
    dx = [1,1,1,-1,-1,-1,0,0]
    dy = [0,1,-1,0,1,-1,1,-1]
    ans = []
    for i in range(8):
        if(curr_x+dx[i] >= 0 and curr_x+dx[i] <= 7 and curr_y+dy[i]>= 0 and curr_y+dy[i]<=7):
            if isOpponent(piece,curr_x+dx[i],curr_y+dy[i]):
                ans.append([curr_x+dx[i],curr_y+dy[i]])
            elif not (isOccupied(piece,curr_x+dx[i],curr_y+dy[i])):
                ans.append([curr_x+dx[i],curr_y+dy[i]])
    return ans

def knightMove(piece):
    curr_x = piece.x
    curr_y = piece.y
    # print("Inside king move")
    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]
    ans = []
    for i in range(8):
        if(curr_x+dx[i] >= 0 and curr_x+dx[i] <= 7 and curr_y+dy[i]>= 0 and curr_y+dy[i]<=7):
            if isOpponent(piece,curr_x+dx[i],curr_y+dy[i]):
                ans.append([curr_x+dx[i],curr_y+dy[i]])
            elif not (isOccupied(piece,curr_x+dx[i],curr_y+dy[i])):
                ans.append([curr_x+dx[i],curr_y+dy[i]])
    return ans

def queenMove(piece):
    curr_x = piece.x
    curr_y = piece.y
    # print("Inside king move")
    dx = [1,1,1,-1,-1,-1,0,0]
    dy = [0,1,-1,0,1,-1,1,-1]
    ans = []
    for i in range(8):
        temp_x = curr_x
        temp_y = curr_y
        for j in range(8):
            if(temp_x+dx[i] >= 0 and temp_x+dx[i] <= 7 and temp_y+dy[i]>= 0 and temp_y+dy[i]<=7):
                temp_x = temp_x+dx[i]
                temp_y = temp_y+dy[i]
                if isOpponent(piece,curr_x+dx[i],curr_y+dy[i]):
                    ans.append([curr_x+dx[i],curr_y+dy[i]])
                elif not (isOccupied(piece,temp_x,temp_y)):
                    ans.append([temp_x,temp_y])
                else:
                    break
            else:
                break
    return ans

def bishopMove(piece):
    curr_x = piece.x
    curr_y = piece.y
    # print("Inside king move")
    dx = [1,1,-1,-1]
    dy = [1,-1,1,-1]
    ans = []
    for i in range(4):
        temp_x = curr_x
        temp_y = curr_y
        for j in range(8):
            if(temp_x+dx[i] >= 0 and temp_x+dx[i] <= 7 and temp_y+dy[i]>= 0 and temp_y+dy[i]<=7):
                temp_x = temp_x+dx[i]
                temp_y = temp_y+dy[i]
                if isOpponent(piece,curr_x+dx[i],curr_y+dy[i]):
                    ans.append([curr_x+dx[i],curr_y+dy[i]])
                elif not (isOccupied(piece,temp_x,temp_y)):
                    ans.append([temp_x,temp_y])
                else:
                    break
            else:
                break
    return ans

def rookMove(piece):
    curr_x = piece.x
    curr_y = piece.y
    # print("Inside king move")
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    ans = []
    for i in range(4):
        temp_x = curr_x
        temp_y = curr_y
        for j in range(8):
            if(temp_x+dx[i] >= 0 and temp_x+dx[i] <= 7 and temp_y+dy[i]>= 0 and temp_y+dy[i]<=7):
                temp_x = temp_x+dx[i]
                temp_y = temp_y+dy[i]
                if isOpponent(piece,curr_x+dx[i],curr_y+dy[i]):
                    ans.append([curr_x+dx[i],curr_y+dy[i]])
                elif not (isOccupied(piece,temp_x,temp_y)):
                    ans.append([temp_x,temp_y])
                else:
                    break
            else:
                break
    return ans

def pawnMovement(piece):
    curr_x = piece.x
    curr_y = piece.y
    print(curr_x,curr_y)
    ans = []
    if(piece.colour == "black"):
        print("in")
        if(curr_y == 1 and not isOccupied(piece,curr_x,curr_y+2) and not isOccupied(piece,curr_x,curr_y+1)):
            ans.append([curr_x,curr_y+2])
        if isOpponent(piece,curr_x+1,curr_y+1):
            ans.append([curr_x+1,curr_y+1])
        if isOpponent(piece,curr_x-1,curr_y+1):
            ans.append([curr_x-1,curr_y+1])
        if not isOccupied(piece,curr_x,curr_y+1):
            ans.append([curr_x,curr_y+1])
    else:
        if(curr_y == 6 and not isOccupied(piece,curr_x,curr_y-2) and not isOccupied(piece,curr_x,curr_y-1)):
            ans.append([curr_x,curr_y-2])
        if isOpponent(piece,curr_x+1,curr_y-1):
            ans.append([curr_x+1,curr_y-1])
        if isOpponent(piece,curr_x-1,curr_y-1):
            ans.append([curr_x-1,curr_y-1])
        if not isOccupied(piece,curr_x,curr_y-1):
            ans.append([curr_x,curr_y-1])
    return ans


