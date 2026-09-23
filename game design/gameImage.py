import pygame
from characters import pieces
pygame.init()

def handlePiecesAdding(path,x,y):
    piece = pygame.image.load(path)
    pieceRect = piece.get_rect()
    width = pieceRect.width/2
    height = pieceRect.height/2
    piece = pygame.transform.scale(piece,(width,height))
    gameDisplay.blit(piece,(x,y))


backGround = pygame.image.load("images/chessboard.bmp")
bgRect = backGround.get_rect()
width = bgRect.width/1.5
height = bgRect.height/1.5
backGround = pygame.transform.scale(backGround,(width,height)) #? This is the steps that affects the main image
gameDisplay = pygame.display.set_mode((width,height)) #? This is a step that affects the main display
gameDisplay.blit(backGround,(0,0))

for items in pieces:
    handlePiecesAdding(items.url,items.x,items.y)

pygame.display.flip()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for items in pieces:
                if(event.pos[0] >= items.x and event.pos[0] <= (items.x+78) and event.pos[1] >= items.y and event.pos[1] <= (items.y+78)):
                    # print(items.name)
                    pygame.draw.rect(gameDisplay, (105,146,62), pygame.Rect(items.x-7, items.y-3, items.size, items.size)) 
                    handlePiecesAdding(items.url,items.x,items.y)
                    pygame.display.flip()
                    print("Pressed")

            