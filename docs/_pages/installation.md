---
title: Installation
permalink: /installation/
---
## A Gentle Forewarning
*Note - this chess board implementation has only been tested for gameplay in a Conda Environment in Ubuntu 20.04 and there is no guarantee that this implementation will work beyond its noted intended use and tested environments.*
*The following instructions are written for installation, testing, and gameplay in the terminal.*
## Step 1 - Clone
Make sure to clone this (embed link to repo) repository to your local machine by running this command in a directory of your choice `git clone git@github.com:olincollege/baba-chess.git` 
## Step 2 - Python Dependencies
The only external library used in this implementation is `Pytest`, which was used only to test the code. If you don’t know whether or not you have pytest installed, run the command `pip install -U pytest`.

Note, testing the code is not necessary for gameplay; however, it is provided as a means to validate the functionality of this code and help curious players understand the edge cases that this code implementation was designed to handle.
## Step 3 (optional) - Testing the Code
To test the code, make sure that you are in the directory where your clone of this repository lives, and run the command `pytest`. If there are no errors, you should get the following screen.

```bash
====================== test session starts =======================
platform linux -- Python 3.9.7, pytest-6.2.4, py-1.10.0,
pluggy-0.13.1
rootdir: /home/osalih/baba-chess
plugins: anyio-2.2.0
collected 60 items

test_chess_board.py ...................................... [ 63%]
..........                                                 [ 80%]
test_chess_controller.py .........                         [ 95%]
test_chess_view.py ...                                     [100%]

======================= 60 passed in 0.08s =======================
```

You are now ready to play a game of chess!
## Step 4 - Launch the game
In order to launch the game simply run the following command in your terminal `python chess_game.py`
You should get the following prompt:
```
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Hello and Welcome to Baba-Chess 1.2, a simple text-based Python
implementation of a chess board. In order to make a
move on the board, please enter your moves in Long Algebraic
Notation (ie. e2-e4). When prompted to move, there are three valid
movetypes.
Make a move - e2-e4
Quit - quit
Undo move - undo
The current revision of this chess board relies heavily on your
knowledge of chess.
Notably, enpassant captures, castling, and promotions have not
been implemented into this version; however, progress is being
made towards improving this chess board.
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
