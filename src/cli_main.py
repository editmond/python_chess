from chess_logic import game_control 
from chess_logic import game_state
from cli import display
from cli import input

#Before the game loop ~~~~
game_control.gameStart()

hasMoved = True

#temporary, remove after testing
counter = 0
#Game loop ~~~
while not game_state.isGameOver and counter < 3:
    #display the board
    gameDisplay = display.createDisplay([])
    gameDisplay = display.addPieces(gameDisplay, game_state.activePieces)
    display.printDisplay(gameDisplay)
    if not hasMoved:
        print("Invalid move")

    # input.inputMove(game_state.isWhiteTurn)

    hasMoved = game_control.player_turn(2, 0, 5, 3)

    counter += 1
