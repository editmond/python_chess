from enum import Enum

class Piece:
    def __init__(self, position, target, isWhite):
        self.position = position
        self.target = target
        self.isWhite = isWhite 


class Rook(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        #
        pieceString = ("RB","RW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class Knight(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        #
        pieceString = ("NB","NW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class Bishop(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        #
        pieceString = ("BB","BW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class Queen(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        #
        pieceString = ("QB","QW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class King(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        #
        pieceString = ("KB","KW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class Pawn(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        #
        pieceString = ("PB","PW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

#an attempt to leverage enums
# class Pieces(Enum):
#     Pawn = 1
#     Rook = 2
#     Knight = 3
#     Bishop = 4
#     Queen = 5
#     King = 6

#class NoPiece(Piece):
#    def __init__(self, position, target, isWhite):
#        super().__init__(position, target, isWhite)
#
#    def __str__(self):
#        #
#        pieceString = ("KB","KW")[self.isWhite]
#        return f"{pieceString}"
#
#    def moveCheck(self):
#        print(f"Check if a {self} can move to {self.target}")

