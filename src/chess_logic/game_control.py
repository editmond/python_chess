from chess_logic import game_state
from chess_logic import pieces

def gameStart():
    #reset variables
    game_state.activePieces = []
    game_state.isWhiteTurn = True
    game_state.totalMoves = 0
    game_state.movesSinceCheck = 0

    # add pieces
    addingWhite = True
    startingRows = [7,0]
    for j in startingRows:
        game_state.activePieces.append(pieces.Rook(0,j, 0,j, addingWhite))
        game_state.activePieces.append(pieces.Rook(7,j, 7,j, addingWhite))
        game_state.activePieces.append(pieces.Knight(1,j, 1,j, addingWhite))
        game_state.activePieces.append(pieces.Knight(6,j, 6,j, addingWhite))
        game_state.activePieces.append(pieces.Bishop(2,j, 2,j, addingWhite))
        game_state.activePieces.append(pieces.Bishop(5,j, 5,j, addingWhite))
        game_state.activePieces.append(pieces.Queen(3,j, 3,j, addingWhite))
        game_state.activePieces.append(pieces.King(4,j, 4,j, addingWhite))
        
        pawnRows = (1, 6)[addingWhite]
        for i in range(8):
            game_state.activePieces.append((pieces.Pawn(i, pawnRows, i, pawnRows, addingWhite)))
        
        addingWhite = False
    
    return

def player_turn(xpos, ypos, xtarget, ytarget):
    #search for piece in position
    foundPiece = False
    index = 0

    while not foundPiece and index < len(game_state.activePieces):
        if xpos == game_state.activePieces[index].xpos and ypos == game_state.activePieces[index].ypos:
            foundPiece = True
        else:
            index += 1

    if not foundPiece:
        return False

    #check to see if target is a valid move
    game_state.activePieces[index].xtarget = xtarget
    game_state.activePieces[index].ytarget = ytarget
    isValidMove = game_state.activePieces[index].moveCheck()

    if not isValidMove:
        return False

    #remove captured pieces
    foundPiece = False
    captureIndex = 0
    while not foundPiece and captureIndex < len(game_state.activePieces):
        if xtarget == game_state.activePieces[captureIndex].xpos and ytarget == game_state.activePieces[captureIndex].ypos:
            foundPiece = True
        else:
            captureIndex += 1

    if game_state.activePieces[captureIndex].isWhite == game_state.isWhiteTurn:
        return False #a check to prevent capturing your own pieces

    game_state.activePieces.pop(captureIndex)

    #change the piece's position
    game_state.activePieces[index].xpos = xtarget
    game_state.activePieces[index].ypos = ytarget

    #switch to the other player's turn'
    game_state.isWhiteTurn = not game_state.isWhiteTurn
    return True
