# har currx is -7
# har curry se -2
# jisse it becomes a multiple of 78

def kingMove(piece):
    curr_x = piece.x
    curr_y = piece.y
    dx = [78,78,78,-78,-78,-78,0,0]
    dy = [0,78,-78,0,78,-78,78,-78]
    ans = []
    for i in range(8):
        if(curr_x+dx[i] >= 78 and curr_x+dx[i] <= 621 and curr_y+dy[i]>= 78 and curr_y+dy[i]<=621):
            ans.append([curr_x+dx[i],curr_y+dy[i]])
    return ans

