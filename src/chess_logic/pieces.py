from enum import Enum

class Piece:
    def __init__(self, xpos, ypos, xtarget, ytarget, isWhite):
        self.xpos = xpos
        self.ypos = ypos
        self.xtarget = xtarget
        self.ytarget = ytarget
        self.isWhite = isWhite 


class Rook(Piece):
    def __init__(self, xpos, ypos, xtarget, ytarget, isWhite):
        super().__init__(xpos, ypos, xtarget, ytarget, isWhite)

    def __str__(self):
        #
        pieceString = ("RB","RW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.xtarget}{self.ytarget}")
        if self.xtarget != self.xpos and self.ytarget != self.ypos:
            return False
        return True

class Knight(Piece):
    def __init__(self, xpos, ypos, xtarget, ytarget, isWhite):
        super().__init__(xpos, ypos, xtarget, ytarget, isWhite)

    def __str__(self):
        #
        pieceString = ("NB","NW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.xtarget}{self.ytarget}")
        return True

class Bishop(Piece):
    def __init__(self, xpos, ypos, xtarget, ytarget, isWhite):
        super().__init__(xpos, ypos, xtarget, ytarget, isWhite)

    def __str__(self):
        #
        pieceString = ("BB","BW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.xtarget}{self.ytarget}")
        return True

class Queen(Piece):
    def __init__(self, xpos, ypos, xtarget, ytarget, isWhite):
        super().__init__(xpos, ypos, xtarget, ytarget, isWhite)

    def __str__(self):
        #
        pieceString = ("QB","QW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.xtarget}{self.ytarget}")
        return True

class King(Piece):
    def __init__(self, xpos, ypos, xtarget, ytarget, isWhite):
        super().__init__(xpos, ypos, xtarget, ytarget, isWhite)

    def __str__(self):
        #
        pieceString = ("KB","KW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.xtarget}{self.ytarget}")
        return True

class Pawn(Piece):
    def __init__(self, xpos, ypos, xtarget, ytarget, isWhite):
        super().__init__(xpos, ypos, xtarget, ytarget, isWhite)

    def __str__(self):
        #
        pieceString = ("PB","PW")[self.isWhite]
        return f"{pieceString}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.xtarget}{self.ytarget}")
        return True

#an attempt to leverage enums
# class Pieces(Enum):
#     Pawn = 1
#     Rook = 2
#     Knight = 3
#     Bishop = 4
#     Queen = 5
#     King = 6

#class NoPiece(Piece):
#    def __init__(self, xpos, ypos, xtarget, ytarget, isWhite):
#        super().__init__(xpos, ypos, xtarget, ytarget, isWhite)
#
#    def __str__(self):
#        #
#        pieceString = ("KB","KW")[self.isWhite]
#        return f"{pieceString}"
#
#    def moveCheck(self):
#        print(f"Check if a {self} can move to {self.xtarget}{self.ytarget}")

