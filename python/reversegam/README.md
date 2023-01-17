This is Reversegam game, also known as Reversi or Othello.

This is a two-player board game played on a grid. The code is using Cartesian coordinate system with x- and y-coordinates to create the board.

Reversegam has an 8×8 board and tiles that are black on one side and white on the other.

The game starts with 4 tiles in the center of the board.

Two players take turns placing tiles of their chosen color—black or white—on the board. When a player places a tile on the board, any of the opponent’s tiles that are between the new tile and the other tiles of the player’s color are flipped.

Each player can quickly flip many tiles on the board in one or two moves. Players must always make a move that flips at least one tile. The game ends when either a player can’t make a move or the board is com- pletely full.

The goal of the game is to end with more tiles of your color than your opponent’s color.

For this game we create the AI algorythm that will look for any corner moves on the board it can take. If there are no corner moves available, the computer will select the move that claims the most tiles. We will also add randomness to the AI moves so there is nota fixed patern of moves that the player could use to beat it.

The player can also activate 'hint' mode, this mode gives the player the options of the possible moves on the board, this makes player's job much easier.
