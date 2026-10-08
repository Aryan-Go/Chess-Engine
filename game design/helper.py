from characters import pieces
def handleDeletion(piece):
    for item in pieces:
        if(piece.name == item.name):
            pieces.remove(item)

def isOccupied(piece,new_x,new_y):
    for item in pieces:
        if(item.x == new_x and item.y == new_y):
            return True
    return False
def isOpponent(piece,new_x,new_y):
    for item in pieces:
        if(item.x == new_x and item.y == new_y and item.colour != piece.colour):
            return True
    return False