# har currx is -7
# har curry se -2
# jisse it becomes a multiple of 78
import characters

def isOccupied(piece,new_x,new_y):
    for item in characters.pieces:
        print(item.x,item.y)
        print(new_x,new_y)
        print(item.colour,piece.colour)
        if((item.x <= new_x+5 or item.x >= new_x-5) and (item.y >= new_y-5 or item.y <= new_y+5) and item.colour == piece.colour):
            return True
    return False


def kingMove(piece):
    curr_x = piece.x
    curr_y = piece.y
    # print("Inside king move")
    dx = [78,78,78,-78,-78,-78,0,0]
    dy = [0,78,-78,0,78,-78,78,-78]
    ans = []
    for i in range(8):
        if(curr_x+dx[i] >= 78 and curr_x+dx[i] <= 621 and curr_y+dy[i]>= 78 and curr_y+dy[i]<=621):
            if not (isOccupied(piece,curr_x+dx[i],curr_y+dy[i])):
                ans.append([curr_x+dx[i],curr_y+dy[i]])
    return ans

