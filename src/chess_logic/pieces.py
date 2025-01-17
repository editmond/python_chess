from chess_logic import game_state

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

        #eliminate any targets that do not fit the cross pattern
        if self.xtarget != self.xpos and self.ytarget != self.ypos:
            return False
        
        #check for pieces in the way of the move to the target
        if self.xpos == self.xtarget:
            for piece in game_state.activePieces:
                if piece.ypos in range(self.ypos+1, self.ytarget) or piece.ypos in range(self.ytarget+1, self.ypos):
                    return False
        elif self.ypos == self.ytarget:
            for piece in game_state.activePieces:
                if piece.xpos in range(self.xpos+1, self.xtarget) or piece.xpos in range(self.xtarget+1, self.xpos):
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

        #possible knight changes to a knight's position: [x,y]. Constant, do not change
        knightChanges = [[2,1], [1,2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

        possiblePositions = []
        for change in knightChanges:
            possiblePositions.append([self.xpos+change[0], self.ypos+change[1]])
            if possiblePositions[-1][0] < 0 or possiblePositions[-1][1] < 0:
                possiblePositions.pop(-1)

        # print(f"This knight's possible positons{possiblePositions}")
        
        target = [self.xtarget, self.ytarget]
        if not (target in possiblePositions):
            return False

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

