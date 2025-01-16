from chess_logic import game_control 
from chess_logic import game_state
from cli import display


#Before the game loop ~~~~
game_control.gameStart()
#display the board
gameDisplay = display.createDisplay([])
gameDisplay = display.addPieces(gameDisplay, game_state.activePieces)

display.printDisplay(gameDisplay)

#Game loop ~~~
