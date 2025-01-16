class Piece:
    def __init__(self, position, target, isWhite):
        self.position = position
        self.target = target
        self.isWhite = isWhite 

class Rook(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        colour = ("Black", "White")[self.isWhite]
        return f"{colour} at {self.position}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class Knight(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        colour = ("Black", "White")[self.isWhite]
        return f"{colour} at {self.position}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class Bishop(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        colour = ("Black", "White")[self.isWhite]
        return f"{colour} at {self.position}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class Queen(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        colour = ("Black", "White")[self.isWhite]
        return f"{colour} at {self.position}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class King(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        colour = ("Black", "White")[self.isWhite]
        return f"{colour} at {self.position}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")

class Pawn(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        colour = ("Black", "White")[self.isWhite]
        return f"{colour} at {self.position}"

    def moveCheck(self):
        print(f"Check if a {self} can move to {self.target}")



