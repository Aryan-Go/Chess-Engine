import pygame
import os

pygame.init()

backGround = pygame.image.load("images/chessboard.bmp")
bgRect = backGround.get_rect()
width = bgRect.width/1.5
height = bgRect.height/1.5
backGround = pygame.transform.scale(backGround,(width,height))
gameDisplay = pygame.display.set_mode((width,height))
gameDisplay.blit(backGround,(0,0))

def handlePiecesAdding(path,x,y):
    piece = pygame.image.load(path)
    pieceRect = piece.get_rect()
    width = pieceRect.width/2
    height = pieceRect.height/2
    piece = pygame.transform.scale(piece,(width,height))
    gameDisplay.blit(piece,(x,y))

# x = 78
handlePiecesAdding("images/main_pieces/black-rook.bmp",85,80)
handlePiecesAdding("images/main_pieces/black-archbis.bmp",163,80)
handlePiecesAdding("images/main_pieces/black-bishop.bmp",241,80)
handlePiecesAdding("images/main_pieces/black-amazon.bmp",319,80)
handlePiecesAdding("images/main_pieces/black-king.bmp",397,80)
handlePiecesAdding("images/main_pieces/black-bishop.bmp",475,80)
handlePiecesAdding("images/main_pieces/black-archbis.bmp",553,80)
handlePiecesAdding("images/main_pieces/black-rook.bmp",631,80)
x = 85
for i in range(8):
    handlePiecesAdding("images/pawns/black-bpawn2.bmp",x,158)
    x+=78


handlePiecesAdding("images/main_pieces/white-rook.bmp",85,626)
handlePiecesAdding("images/main_pieces/white-archbis.bmp",163,626)
handlePiecesAdding("images/main_pieces/white-bishop.bmp",241,626)
handlePiecesAdding("images/main_pieces/white-amazon.bmp",319,626)
handlePiecesAdding("images/main_pieces/white-king.bmp",397,626)
handlePiecesAdding("images/main_pieces/white-bishop.bmp",475,626)
handlePiecesAdding("images/main_pieces/white-archbis.bmp",553,626)
handlePiecesAdding("images/main_pieces/white-rook.bmp",631,626)
x = 85
for i in range(8):
    handlePiecesAdding("images/pawns/white-bpawn2.bmp",x,548)
    x+=78

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()