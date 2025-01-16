from chess_logic import game_control 
from chess_logic import game_state
from cli import display
from cli import input

#Before the game loop ~~~~
game_control.gameStart()

#Game loop ~~~
while not game_state.isGameOver:
    #display the board
    gameDisplay = display.createDisplay([])
    gameDisplay = display.addPieces(gameDisplay, game_state.activePieces)
    display.printDisplay(gameDisplay)

    # input.inputMove(game_state.isWhiteTurn)

    game_control.player_turn(0, 0, 2, 0)

    
