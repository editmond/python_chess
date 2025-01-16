from chess_logic import game_state
from chess_logic import pieces

def game_start():
    #reset variables
    game_state.activePieces = []
    game_state.isWhiteTurn = True
    game_state.totalMoves = 0
    game_state.movesSinceCheck = 0

    # add pieces
    addingWhite = True
    startingRows = [0,7]
    for j in startingRows:
        game_state.activePieces.append(pieces.Rook(0,j, 0,j, addingWhite))
        game_state.activePieces.append(pieces.Rook(7,j, 7,j, addingWhite))
        game_state.activePieces.append(pieces.Knight(1,j, 1,j, addingWhite))
        game_state.activePieces.append(pieces.Knight(6,j, 6,j, addingWhite))
        game_state.activePieces.append(pieces.Bishop(3,j, 3,j, addingWhite))
        game_state.activePieces.append(pieces.Bishop(5,j, 5,j, addingWhite))
        game_state.activePieces.append(pieces.Queen(4,j, 4,j, addingWhite))
        game_state.activePieces.append(pieces.King(5,j, 5,j, addingWhite))
        
        pawnRows = (6, 1)[addingWhite]
        for i in range(8):
            game_state.activePieces.append((pieces.Pawn(i, pawnRows, i, pawnRows, addingWhite)))
        
        addingWhite = False
    
    print(f"{game_state.activePieces}")
    return

def player_turn(target):
    return
