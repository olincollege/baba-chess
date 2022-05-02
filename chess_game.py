"""
Main program to set up and run a game of chess.
"""
from chess_board import ChessBoard
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
    #Print out a set of rules and allowed inputs
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"\
          "Hello and Welcome to Baba-Chess 1.0, a simple text-based Python\n"\
          "implementation of a chess board. In order to make a\n"\
          "move on the board, please enter your moves in Long Algebraic\n"\
          "Notation (ie. e2, e4). When prompted to move, there are three valid"\
          " movetypes.\nMake a move - e2, e4\nQuit - quit\n"\
          "Undo move - undo\nThe current revision of this chess board relies "\
          "heavily on your knowledge of chess.\nNotably, enpassant captures, "\
          "castling, and promotions have not been implemented into this "\
          "version;\nhowever, progress is being made towards improving this "\
          "chess board.\n"\
          "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    
    #TODO find a win condition so this isn't an infinite loop
    while True:
        #TODO make a bidirectional dictionary to condense code
        current_player = controllers[(board.next_player())]

        view.draw()
        move = current_player.move()
        # If the move inputted by the player is "quit", the game is over.
        if move == "quit":
            break
        elif move == "undo":
            board.undo_move()
        else:
            move
    print(f"{board.next_player()} has ended the game.")

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
