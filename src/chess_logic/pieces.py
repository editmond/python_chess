class Piece:
    def __init__(self, position, target, isWhite):
        self.position = position
        self.target = target
        self.isWhite = isWhite 

class Rook(Piece):
    def __init__(self, position, target, isWhite):
        super().__init__(position, target, isWhite)

    def __str__(self):
        return f"A {self.isWhite} at {self.position}"

    def moveCheck(self):
        print(f"check {self} can move to {self.target}")
