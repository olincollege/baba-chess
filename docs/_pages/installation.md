---
title: Installation
permalink: /installation/
---

# Getting the game
Note - this chess board implementation has only been tested for gameplay in a Conda Environment in Ubuntu 20.04 and there is no guarantee that this implementation will work beyond its noted intended use and tested environments.
The following instructions are written for installation, testing, and gameplay in the terminal.
## Step 1 - Clone
Make sure to clone this (embed link to repo) repository to your local machine by running this command in a directory of your choice `git clone git@github.com:olincollege/baba-chess.git` 
## Step 2 - Python Dependencies
The only external library used in this implementation is `Pytest`, which was used only to test the code. If you don’t know whether or not you have pytest installed, run the command `pip install -U pytest`.

Note, testing the code is not necessary for gameplay; however, it is provided as a means to validate the functionality of this code and help curious players understand the edge cases that this code implementation was designed to handle.
## Step 3 (optional) - Testing the Code
To test the code, make sure that you are in the directory where your clone of this repository lives, and run the command `pytest`. If there are no errors, you should get the following screen.

![UnitTestSuccess](./images/UnitTestsSuccess.PNG)

You are now ready to play a game of chess!
## Step 4 - Launch the game
In order to launch the game simply run the following command in your terminal `python chess_game.py main`
You should get the following prompt
![InitialScreen](./assets/images/initscreen.PNG)
