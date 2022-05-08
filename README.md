# baba-chess (Rev.1.2)
Omar Salih, Arturo Joya, Drew Pang

This repository contains the necessary files needed to run a game of Chess in Python.

## Python Dependencies
This chess board implementation was written in a Conda environment using Python 3.9.7.

### Code Testing
Although the following is not essential for gameplay, it is helpful to have Pytest installed. If you are unsure whether you have pytest installed, you can do so by running the following command `pip install -U pytest`

## Use the Code
To begin using this code, clone this repository onto a directory of your choice. You will want to make sure that you have `chess_board_alternative`, `chess_view`, `chess_controller`, and `chess_game`.
- Open a new terminal, make sure that you are in the same directory as the code.
- Run `python chess_game.py` on the terminal.
- That's all! you should see the following prompt on the screen:
```
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Hello and Welcome to Baba-Chess 1.2, a simple text-based Python
implementation of a chess board. In order to make a
move on the board, please enter your moves in Long Algebraic
Notation (ie. e2-e4). When prompted to move, there are three valid movetypes.
Make a move - e2-e4
Quit - quit
Undo move - undo
The current revision of this chess board relies heavily on your knowledge of chess.
Notably, enpassant captures, castling, and promotions have not been implemented into this version;
however, progress is being made towards improving this chess board.
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   a b c d e f g h
  +-+-+-+-+-+-+-+-+
8 |r|n|b|q|k|b|n|r| 8
  +-+-+-+-+-+-+-+-+
7 |p|p|p|p|p|p|p|p| 7
  +-+-+-+-+-+-+-+-+
6 | | | | | | | | | 6
  +-+-+-+-+-+-+-+-+
5 | | | | | | | | | 5
  +-+-+-+-+-+-+-+-+
4 | | | | | | | | | 4
  +-+-+-+-+-+-+-+-+
3 | | | | | | | | | 3
  +-+-+-+-+-+-+-+-+
2 |P|P|P|P|P|P|P|P| 2
  +-+-+-+-+-+-+-+-+
1 |R|N|B|Q|K|B|N|R| 1
  +-+-+-+-+-+-+-+-+
   a b c d e f g h
It is now white's turn.
Input your move ie. ('e2-e4'/undo/quit):
```

## Test the Code
Testing the code is not necessary for game play, but to make sure that the code is working properly before running the game, it will be helpful to run these tests.

Firstly, ensure that you are in the directory where the clone of this repository lives. Then run `pytest`. If all goes well you should see the following screen:
```
=========================================== test session starts ===========================================
platform linux -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /home/user/baba-chess
plugins: anyio-2.2.0
collected 60 items

test_chess_board.py ................................................                                 [ 80%]
test_chess_controller.py .........                                                                   [ 95%]
test_chess_view.py ...                                                                               [100%]

=========================================== 60 passed in 0.08s ============================================
```

## Play the Game
The board is set up such that the uppercase letters represent the white player, and the lower case letters represent the black player. The current revision now takes in LAN (long algebraic notation). Note that we are using a simplified version of LAN, such that only the "spots" are noted. For example, to make the move e4 in standard algebraic notation, it would be `e2-e4` in our implementation. For the move Nf6 in standard algebraic notation, that move would be made with the input `g8-f6` which moves the piece at g8 (in this case the black knight) to the spot f6. Please refer to the table below for Chess notation translations.

|Graphical Algebraic|Notation Standard Algebraic|Notation Long Algebraic Notation|
|:-----------------:|:-------------------------:|:------------------------------:|
|e4|e4|e2-e4|
|♞f6|Nf6|g8-f6|

*Note*, castling and pawn promotions have not been implemented yet, therefore those commands should not be attempted as they will result in an invalid-move-prompt.

While playing the game of chess, it is possible that an incorrect move is played. At the mercy of the next player, the input `undo` can be called to revert the state of the board to one move prior. Note that calling `undo` twice will undo the undo and revert the board back to how it was before the undo.

This board implementation does not yet contain a check or checkmate checker; however, to quit the match, you may input `quit` to quit the match. Note that this match does not get saved, and thus the next time that the game is launched, it will be a brand new game.

## Future Implementations
Rev.1.3 seeks to implement the following features:
- Promote Pawn
- Castle

Coming soon...