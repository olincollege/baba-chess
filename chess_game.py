"""
Main program to set up and run a game of chess.
"""
from chess_board import ChessBoard
from chess_pieces import Pawn, Rook, Bishop, Knight, Queen, King
from chess_view import TextView
from chess_controller import TextController

def main():
    """
    Main function to run a chess game.
    
    The current main function runs infinitely until a player choses to quit the
    game.
    """
    #set up MVC components for an instance of chess
    board = ChessBoard()
    view = TextView(board)
    controllers = {
        "white": TextController(board),
        "black": TextController(board),
    }
    current_player = None
    
    #TODO find a win condition so this isn't an infinite loop
    while True:
        if board.next_player():
            current_player = controllers["white"]
        else:
            current_player = controllers["black"]
        if controllers[current_player].quit():
            break
        view.draw()
        controllers[current_player].move()
        view.draw()
    print(f"{current_player} has ended the game.")

#if __name__ == "__main__":
#    main()

def drews_test():
    board = ChessBoard()
    board.fill_generic_board()
    print(board)


drews_test()
