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
        game_state.activePieces.append(pieces.Bishop(3,j, 3,j, addingWhite))
        game_state.activePieces.append(pieces.Bishop(5,j, 5,j, addingWhite))
        game_state.activePieces.append(pieces.Queen(4,j, 4,j, addingWhite))
        game_state.activePieces.append(pieces.King(5,j, 5,j, addingWhite))
        
        pawnRows = (1, 6)[addingWhite]
        for i in range(8):
            game_state.activePieces.append((pieces.Pawn(i, pawnRows, i, pawnRows, addingWhite)))
        
        addingWhite = False
    
    return

def player_turn(position, target):
    return
