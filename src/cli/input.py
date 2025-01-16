def inputMove(isWhiteTurn):
    if isWhiteTurn:
        print("White's turn")
    else:
        print("Black's turn")

    position = input("Position of piece to move. (XY e.g. 41): ")
    target = input("Co-ordinates to move to. (XY e.g. 41): ")
    return
