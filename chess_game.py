"""
Main program to set up and run a game of chess.
"""
from chess_board_alternative import ChessBoard
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
        #TODO make a bidirectional dictionary to condense code
        if board.next_player():
            current_player = controllers["white"]
            current_player_color = "white"
        else:
            current_player = controllers["black"]
            current_player_color = "black"
        # if controllers[current_player].quit():
        #    break
        view.draw()
        controllers[current_player_color].move()
        view.draw()
    print(f"{current_player} has ended the game.")

if __name__ == "__main__":
   main()

# def board_move_test():
#     #set up MVC components for an instance of chess
#     board = ChessBoard()
#     view = TextView(board)
#     controllers = {
#         "white": TextController(board),
#         "black": TextController(board),
#     }
#     current_player = None

#     if board.next_player():
#         current_player = controllers["white"]
#         current_player_color = "white"
#     else:
#         current_player = controllers["black"]
#         current_player_color = "black"
#     view.draw()
#     board.move((1, 0), (2, 0))
#     view.draw()
#     board.move((6, 6), (5, 6))
#     view.draw()

# board_move_test()
