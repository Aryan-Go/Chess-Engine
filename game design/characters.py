import pygame
class Piece:
    def __init__(self,name,x,y,url,type,colour):
        self.x = x
        self.y = y
        self.size = 78 
        self.name = name
        self.url = url
        self.type = type
        self.colour = colour

pieces = [
    Piece("bbrook",85,80,"images/main_pieces/black-rook.bmp","rook","black"),
    Piece("bknight",163,80,"images/main_pieces/black-archbis.bmp","knight","black"),
    Piece("bbishop",241,80,"images/main_pieces/black-bishop.bmp","bishop","black"),
    Piece("bqueen",319,80,"images/main_pieces/black-amazon.bmp","queen","black"),
    Piece("bking",397,80,"images/main_pieces/black-king.bmp","king","black"),
    Piece("bbishop",475,80,"images/main_pieces/black-bishop.bmp","bishop","black"),
    Piece("bknight",553,80,"images/main_pieces/black-archbis.bmp","knight","black"),
    Piece("bbrook",631,80,"images/main_pieces/black-rook.bmp","rook","black"),
    Piece("bpawn1",85,158,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn2",163,158,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn3",241,158,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn4",319,158,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn5",397,158,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn6",475,158,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn7",553,158,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("bpawn8",631,158,"images/pawns/black-bpawn2.bmp","pawn","black"),
    Piece("wbrook",85,626,"images/main_pieces/white-rook.bmp","pawn","white"),
    Piece("wknight",163,626,"images/main_pieces/white-archbis.bmp","knight","white"),
    Piece("wbishop",241,626,"images/main_pieces/white-bishop.bmp","bishop","white"),
    Piece("wqueen",319,626,"images/main_pieces/white-amazon.bmp","queen","white"),
    Piece("wking",397,626,"images/main_pieces/white-king.bmp","king","white"),
    Piece("wbishop",475,626,"images/main_pieces/white-bishop.bmp","bishop","white"),
    Piece("wknight",553,626,"images/main_pieces/white-archbis.bmp","knight","white"),
    Piece("wrook",631,626,"images/main_pieces/white-rook.bmp","rook","white"),
    Piece("wpawn1",85,548,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn2",163,548,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn3",241,548,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn4",319,548,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn5",397,548,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn6",475,548,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn7",553,548,"images/pawns/white-bpawn2.bmp","pawn","white"),
    Piece("wpawn8",631,548,"images/pawns/white-bpawn2.bmp","pawn","white"),
]