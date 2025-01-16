import chess_logic.pieces


rook = chess_logic.pieces.Rook([0,0], [0,0], True)
print(f"{rook}")
rook.moveCheck()
rook.target = [0,5]
rook.moveCheck()
