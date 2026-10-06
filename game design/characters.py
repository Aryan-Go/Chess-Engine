import pygame
class Piece:
    def __init__(self,name,x,y,url,type,colour):
        self.x = x
        self.y = y
        self.size = 79
        self.name = name
        self.url = url
        self.type = type
        self.colour = colour

pieces = [
    Piece("bbrook",0,0,"images/main_pieces/black-rook.bmp","rook","black"),
    Piece("bknight",1,0,"images/main_pieces/black-archbis.bmp","knight","black"),
    Piece("bbishop",2,0,"images/main_pieces/black-bishop.bmp","bishop","black"),
    Piece("bqueen",3,0,"images/main_pieces/black-amazon.bmp","queen","black"),
    Piece("bking",4,0,"images/main_pieces/black-king.bmp","king","black"),
    Piece("bbishop",5,0,"images/main_pieces/black-bishop.bmp","bishop","black"),
    Piece("bknight",6,0,"images/main_pieces/black-archbis.bmp","knight","black"),
    Piece("bbrook",7,0,"images/main_pieces/black-rook.bmp","rook","black"),
    Piece("bpawn1",0,1,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn2",1,1,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn3",2,1,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn4",3,1,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn5",4,1,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn6",5,1,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn7",6,1,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn8",7,1,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("wbrook",0,7,"images/main_pieces/white-rook.bmp","rook","white"),
    Piece("wknight",1,7,"images/main_pieces/white-archbis.bmp","knight","white"),
    Piece("wbishop",2,7,"images/main_pieces/white-bishop.bmp","bishop","white"),
    Piece("wqueen",3,7,"images/main_pieces/white-amazon.bmp","queen","white"),
    Piece("wking",4,7,"images/main_pieces/white-king.bmp","king","white"),
    Piece("wbishop",5,7,"images/main_pieces/white-bishop.bmp","bishop","white"),
    Piece("wknight",6,7,"images/main_pieces/white-archbis.bmp","knight","white"),
    Piece("wrook",7,7,"images/main_pieces/white-rook.bmp","rook","white"),
    Piece("wpawn1",0,6,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn2",1,6,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn3",2,6,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn4",3,6,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn5",4,6,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn6",5,6,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn7",6,6,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn8",7,6,"images/pawns/white-bpawn2.bmp","pawn","white"),
]