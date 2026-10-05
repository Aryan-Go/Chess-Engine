# har currx is -7
# har curry se -2
# jisse it becomes a multiple of 78
import characters

def isOccupied(piece,new_x,new_y):
    for item in characters.pieces:
        print(item.x,item.y)
        print(new_x,new_y)
        print(item.colour,piece.colour)
        if(item.x == new_x and item.y == new_y and item.colour == piece.colour):
            return True
    return False


def kingMove(piece):
    curr_x = piece.x
    curr_y = piece.y
    # print("Inside king move")
    dx = [1,1,1,-1,-1,-1,0,0]
    dy = [0,1,-1,0,1,-1,1,-1]
    ans = []
    for i in range(8):
        if(curr_x+dx[i] >= 0 and curr_x+dx[i] <= 7 and curr_y+dy[i]>= 0 and curr_y+dy[i]<=7):
            if not (isOccupied(piece,curr_x+dx[i],curr_y+dy[i])):
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
                if not (isOccupied(piece,temp_x,temp_y)):
                    ans.append([temp_x,temp_y])
                else:
                    break
            else:
                break
    return ans
