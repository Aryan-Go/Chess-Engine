import pygame
class Piece:
    def __init__(self,name,x,y,url):
        self.x = x
        self.y = y
        self.size = 78 
        self.name = name
        self.url = url

pieces = [
    Piece("bbrook",85,80,"images/main_pieces/black-rook.bmp"),
    Piece("bknight",163,80,"images/main_pieces/black-archbis.bmp"),
    Piece("bbishop",241,80,"images/main_pieces/black-bishop.bmp"),
    Piece("bqueen",319,80,"images/main_pieces/black-amazon.bmp"),
    Piece("bking",397,80,"images/main_pieces/black-king.bmp"),
    Piece("bbishop",475,80,"images/main_pieces/black-bishop.bmp"),
    Piece("bknight",553,80,"images/main_pieces/black-archbis.bmp"),
    Piece("bbrook",631,80,"images/main_pieces/black-rook.bmp"),
    Piece("bpawn1",85,158,"images/pawns/black-bpawn2.bmp"),
    Piece("bpawn2",163,158,"images/pawns/black-bpawn2.bmp"),
    Piece("bpawn3",241,158,"images/pawns/black-bpawn2.bmp"),
    Piece("bpawn4",319,158,"images/pawns/black-bpawn2.bmp"),
    Piece("bpawn5",397,158,"images/pawns/black-bpawn2.bmp"),
    Piece("bpawn6",475,158,"images/pawns/black-bpawn2.bmp"),
    Piece("bpawn7",553,158,"images/pawns/black-bpawn2.bmp"),
    Piece("bpawn8",631,158,"images/pawns/black-bpawn2.bmp"),
    Piece("wbrook",85,626,"images/main_pieces/white-rook.bmp"),
    Piece("wknight",163,626,"images/main_pieces/white-archbis.bmp"),
    Piece("wbishop",241,626,"images/main_pieces/white-bishop.bmp"),
    Piece("wqueen",319,626,"images/main_pieces/white-amazon.bmp"),
    Piece("wking",397,626,"images/main_pieces/white-king.bmp"),
    Piece("wbishop",475,626,"images/main_pieces/white-bishop.bmp"),
    Piece("wknight",553,626,"images/main_pieces/white-archbis.bmp"),
    Piece("wrook",631,626,"images/main_pieces/white-rook.bmp"),
    Piece("wpawn1",85,548,"images/pawns/white-bpawn2.bmp"),
    Piece("wpawn2",163,548,"images/pawns/white-bpawn2.bmp"),
    Piece("wpawn3",241,548,"images/pawns/white-bpawn2.bmp"),
    Piece("wpawn4",319,548,"images/pawns/white-bpawn2.bmp"),
    Piece("wpawn5",397,548,"images/pawns/white-bpawn2.bmp"),
    Piece("wpawn6",475,548,"images/pawns/white-bpawn2.bmp"),
    Piece("wpawn7",553,548,"images/pawns/white-bpawn2.bmp"),
    Piece("wpawn8",631,548,"images/pawns/white-bpawn2.bmp"),
]