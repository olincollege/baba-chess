"""
Chess Board Implementation.
"""

from shutil import move

from numpy import moveaxis
from pyparsing import White
from chess_pieces import Pawn, Rook, Bishop, Knight, Queen, King

class ChessBoard:
    """
    Your docstring goes here.
    """

    player_1_color = "white"
    player_2_color = "black"
    blank_square = "  "

    def __init__(self):
        """
        Create and populate a new Chess board.
        """
        self._board = [[self.blank_square for _ in range(8)] for _ in range(8)]
        self._current_player = self.player_1_color

    def fill_generic_board(self):
        """
        Fill board with variables and create piece instances.
        """
        self._board[0] = ["R1", "N1", "B1", "Q1", "K1", "B2", "N2", "R2"] # White back row
        self._board[1] = ["P" + str(_) for _ in range (8)] # White pawns
        
        self._board[6] = ["p" + str(_) for _ in range(8)] # Black pawns
        self._board[7] = ["r1", "n1", "b1", "q1", "k1", "b2", "n2", "r2"] # Black back row
        
        self._generate_piece_instances()

    def _generate_piece_instances(self):
        """
        Docstring
        """
        #globals()[self._board[1][0]] = Pawn(self._board, (1, 0), True)

        self.test = Pawn(self._board, (1, 0), True)
        #print(self.test)
        # pieces = []
        # for row_count, row in enumerate(self._board):
        #     if row[0].isupper():
        #         color = True
        #     else: 
        #         color = False
        #     for column_count, column in enumerate(row):
        #         pieces.append(column)
        #         if column[0] in ["P", "p"]:
        #             #print(color)
        #             globals()[column] = Pawn(self._board, (row_count, column_count), color)
        #             #print(column)
        #             #locals()[column] = Pawn(self._board, (row_count, column_count), color)
        #             # print("pawn found!")
        # #print(self._board[1][0])

    def get_square_properties(self, row, column):
        pass

    def __repr__(self):
        # row_divider = "+--" * 8 + "+"
        # lines = [row_divider]
        # for i in range(8):
        #     row = f"|{'|'.join(self._board[i])}|"
        #     #row = str(print(self._board[i][0]))
        #     lines.append(row)
        #     lines.append(row_divider)

        # return "\n".join(lines)

        #test1 = str(print(self.test))
        #print(test1)
        return self.test.__repr__()
        """
        
        """
"""
    flip next move

    move    
        take move from controller
        pass to Pieces
        give me list of possible pievce move
        check if move is possible
        update board
        update piece instance 


 def undo_move
"""

