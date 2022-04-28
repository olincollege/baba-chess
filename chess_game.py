"""
Main program to set up and run a game of chess.
"""
from chess_board import ChessBoard

def main():
    """
    Main function to run a chess game.
    """
    board = ChessBoard()
    print(board._board)