import pygame
class Piece:
    def __init__(self,name,x,y,url,type,colour):
        self.x = x
        self.y = y
        self.size = 77
        self.name = name
        self.url = url
        self.type = type
        self.colour = colour

pieces = [
    Piece("bbrook",78,78,"images/main_pieces/black-rook.bmp","rook","black"),
    Piece("bknight",156,78,"images/main_pieces/black-archbis.bmp","knight","black"),
    Piece("bbishop",233,78,"images/main_pieces/black-bishop.bmp","bishop","black"),
    Piece("bqueen",311,78,"images/main_pieces/black-amazon.bmp","queen","black"),
    Piece("bking",388,78,"images/main_pieces/black-king.bmp","king","black"),
    Piece("bbishop",466,78,"images/main_pieces/black-bishop.bmp","bishop","black"),
    Piece("bknight",543,78,"images/main_pieces/black-archbis.bmp","knight","black"),
    Piece("bbrook",621,78,"images/main_pieces/black-rook.bmp","rook","black"),
    Piece("bpawn1",78,156,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn2",156,156,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn3",233,156,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn4",311,156,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn5",388,156,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn6",466,156,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn7",543,156,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn8",621,156,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("wbrook",78,621,"images/main_pieces/white-rook.bmp","pawn","white"),
    Piece("wknight",156,621,"images/main_pieces/white-archbis.bmp","knight","white"),
    Piece("wbishop",233,621,"images/main_pieces/white-bishop.bmp","bishop","white"),
    Piece("wqueen",311,621,"images/main_pieces/white-amazon.bmp","queen","white"),
    Piece("wking",388,621,"images/main_pieces/white-king.bmp","king","white"),
    Piece("wbishop",466,621,"images/main_pieces/white-bishop.bmp","bishop","white"),
    Piece("wknight",543,621,"images/main_pieces/white-archbis.bmp","knight","white"),
    Piece("wrook",621,621,"images/main_pieces/white-rook.bmp","rook","white"),
    Piece("wpawn1",78,543,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn2",156,543,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn3",233,543,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn4",311,543,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn5",388,543,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn6",466,543,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn7",543,543,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn8",621,543,"images/pawns/white-bpawn2.bmp","pawn","white"),
]