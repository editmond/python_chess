def createDisplay(display):
    for j in range(8):
        row = []
        for i in range(8):
            square_shading = ("XX", "OO")[(i+j) % 2 == 0]
            row.append(square_shading)
        display.append(row)
    return display

def addPieces(display, activePieces):
    for piece in activePieces:
        display[piece.ypos][piece.xpos] = f"{piece}"

    return display

def printDisplay(display):
    for row in display:
        row = " ".join(row)
        print(row)
