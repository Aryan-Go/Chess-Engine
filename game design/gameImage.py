import pygame
from characters import pieces
from rulesPiece import kingMove,queenMove,pawnMovement,bishopMove,rookMove,knightMove
from helper import handleDeletion

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("audio/chess_move_sound.mp3")

def handlePiecesAdding(path,x,y):
    piece = pygame.image.load(path).convert_alpha()
    pieceRect = piece.get_rect()
    width = pieceRect.width/2
    height = pieceRect.height/2
    # print(width,height)
    piece = pygame.transform.scale(piece,(width,height))
    gameDisplay.blit(piece,(x*77+85,y*77+80))

def handleDotAdding(path,x,y):
    piece = pygame.image.load(path).convert_alpha()
    pieceRect = piece.get_rect()
    width = pieceRect.width/2
    height = pieceRect.height/2
    # print(width,height)
    piece = pygame.transform.scale(piece,(width,height))
    gameDisplay.blit(piece,(x*77+70,y*77+75))

backGround = pygame.image.load("images/chessboard.bmp")
bgRect = backGround.get_rect()
width = bgRect.width/1.5
height = bgRect.height/1.5
# print(width,height)
backGround = pygame.transform.scale(backGround,(width,height)) #? This is the steps that affects the main image
gameDisplay = pygame.display.set_mode((width,height)) #? This is a step that affects the main display
gameDisplay.blit(backGround,(0,0))
pygame.display.set_caption("Lets start the game. Its white turn to move")

mover = "white" #? so that I can know which one to move black or white

selectedPiece = None
legalCoord = []

for items in pieces:
    handlePiecesAdding(items.url,items.x,items.y)

pygame.display.flip()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and selectedPiece == None:
            gameDisplay.blit(backGround,(0,0))
            for items in pieces:
                if((event.pos[0]-85)/77 >= items.x and (event.pos[0]-85)/77 <= (items.x+1) and (event.pos[1]-80)/77 >= items.y and (event.pos[1]-80)/77 <= (items.y+1)):
                    if(items.colour != mover):
                        handlePiecesAdding(items.url,items.x,items.y)
                        continue
                    pygame.draw.rect(gameDisplay, (105,146,62), pygame.Rect(items.x*77+78, items.y*77+78, items.size, items.size)) 
                    handlePiecesAdding(items.url,items.x,items.y)
                    if(items.type == "king"):
                        coord = kingMove(items)
                    elif(items.type == "queen"):
                        coord = queenMove(items)
                    elif(items.type == "knight"):
                        coord = knightMove(items)
                    elif(items.type == "bishop"):
                        coord = bishopMove(items)
                    elif(items.type == "rook"):
                        coord = rookMove(items)
                    elif(items.type == "pawn"):
                        coord = pawnMovement(items)
                    selectedPiece = items
                    legalCoord = coord
                else:
                    handlePiecesAdding(items.url,items.x,items.y)
                for pts in legalCoord:
                    handleDotAdding("images/main_pieces/legal_move_dots.bmp",pts[0],pts[1])
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONDOWN and selectedPiece != None:
            currx = int((event.pos[0]-78)/77)
            curry = int((event.pos[1]-78)/77)
            moved = False
            gameDisplay.blit(backGround,(0,0))

            #? Moving the piece
            for item in pieces:
                if item.name == selectedPiece.name and [currx,curry] in legalCoord:
                    pygame.mixer.music.play()
                    moved = True
                    item.x = currx
                    item.y = curry

            #? If any enemy so handling its delettion
            for items in pieces:
                if selectedPiece.colour != items.colour and selectedPiece.x == items.x and selectedPiece.y == items.y:
                    handleDeletion(items)

            #? Rendering the pieces
            for items in pieces:
                handlePiecesAdding(items.url,items.x,items.y)
            pygame.display.flip()
            selectedPiece = None
            legalCoord = []
            if(mover == "white" and moved):
                mover = "black"
                pygame.display.set_caption("Its black turn to move")
            elif(mover == "black" and moved):
                mover = "white"
                pygame.display.set_caption("Its white turn to move")
            

            