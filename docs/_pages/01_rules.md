---
title: Rules
permalink: /rules/
order: 1
---

# Rules of the game:
Firstly, if you aren’t familiar with the rules of chess, specifically how chess pieces should and shouldn’t move [Learn Chess Here!](https://chess.org/rules?msclkid=93fbb98ace7c11eca3716e0e73ad05af)
All of the pieces follow these basic move rules, with the exception that en passant captures, castling, and pawn promotions have not yet been implemented into this chess board. In order to make these moves, we are taking in Long Algebraic Notation. Below is a table that may be helpful for understanding the connection between standard algebraic notation and our coordinate-based long algebraic notation.

|Graphical Algebraic|Notation Standard Algebraic|Notation Long Algebraic Notation|
|:-----------------:|:-------------------------:|:------------------------------:|
|e4|e4|e2-e4|
|♞f6|Nf6|g8-f6|

Thus, to make a move you must input the coordinate of the square the piece you are moving is, then the destination square. A legend for these coordinates is found in the representation of the chess board in the terminal.

While a normal game of chess ends in either a checkmate or a stalemate, our current implementation does not check for those winning conditions, and thus, like a physical board, a win is determined by the players playing the game.

In order to undo a move, a player may call `undo`, which will reset the state of the board to how it was before the move that was undone. Note, that you can only call undo for one move. Therefore, calling undo after an undo was called, it will simply undo the undo and revert the board to how it was had the undo’s not been called to begin with.

Since a win condition is not checked autonomously, it is up to the players to quit out of the game. This can be done by calling `quit`, which simply quits out of the game. This can be called by either player at any time. Note that there is no save file, therefore quitting out of a match loses the data of the game played. Thus, relaunching the game will launch a brand new game.

These limitations of the board means that it is up to the player’s knowledge of the game to determine whether or not a game has been won, lost, or drawn. 

