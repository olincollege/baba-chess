"""
Chess Board Implementation.
"""

from shutil import move

from numpy import moveaxis
from pyparsing import White
# from chess_pieces import Pawn, Rook, Bishop, Knight, Queen, King

class ChessBoard:
    """
    Your docstring goes here.
    """

    player_1_color = "white"
    player_2_color = "black"
    blank_square = " "

    def __init__(self):
        """
        Create and populate a new Chess board.
        """
        self._board = [[self.blank_square for _ in range(8)] for _ in range(8)]
        self._next_player = self.player_1_color
        self.fill_generic_board()

    def fill_generic_board(self):
        """
        Fill board with variables and create piece instances.
        """
        self._board[0] = ["R1", "N1", "B1", "Q1", "K1", "B2", "N2", "R2"] # White back row
        self._board[1] = ["P" + str(_) for _ in range (8)] # White pawns
        
        self._board[6] = ["p" + str(_) for _ in range(8)] # Black pawns
        self._board[7] = ["r1", "n1", "b1", "q1", "k1", "b2", "n2", "r2"] # Black back row

    def next_player(self):
        """
        Return a bool for the next color player to move.

        Returns:
            A bool representing.
        """
        if self._next_player == self.player_1_color:
            return True
        return False
    
    def get_square_properties(self, row, column):
        pass
    
    def in_bound(self, pos):
        """
        Check that a position is within the bounds of the board.
        
        Args:
            pos: A tuple representing the position the piece is wants to access.
            
        Return:
            A bool representing whether the square is valid or not.
        """
        try: 
            self._board.get_square(pos)
            return True
        except (IndexError):
            return False

    def is_white(self):
        """
        Return a bool of the piece's color. White = True, Black = False
        """
        return self.color

    def check_pawn_move(self, pos, color):
        """
        Calculate the possible moves to return a list of possible moves that
        the pawn piece could move to based of the position of the pawn.
        
        Return: A list of tuples representing the moves that the piece can make.
        """
        row = self.pos[0]
        col = self.pos[1]
        moves = []
        #TODO - Condense code 
        if self.is_white():
            if self.first_move: #if first move, check the second square ahead
                (row, col) = (row+2, col)
                if self._board.get_square((row, col)) == " ":
                    moves.append((row, col))
            for i in range(-1,2):
                (row, col) = (row+1, col+i)
                if i == 0:
                    if self._board.get_square((row, col)) == " ":
                        moves.append((row, col))
                else:
                    if self.in_bound((row, col)):
                        if self._board.get_square((row, col)) != " " \
                        or self._board.get_square((row, col)) != self.is_white():
                            moves.append((row, col))
        else:
            if self.first_move:
                (row, col) = (row-2, col)
                if self._board.get_square((row, col)) == " ":
                    moves.append((row, col))
            for i in range(-1,2):
                (row, col) = (row-1, col+i)
                if i == 0:
                    if self._board.get_square((row, col)) == " ":
                        moves.append((row, col))
                else:
                    if self.in_bound((row, col)):
                        if self._board.get_square((row, col)) != " " \
                        or self._board.get_square((row, col)) != self.is_white():
                            moves.append((row, col))
        return moves

    def __repr__(self):
        row_divider = "+-" * 8 + "+"
        lines = [row_divider]
        for i in range(8):
            pieces_row = [self._board[i][_][0] for _ in range(8)]
            row = f"|{'|'.join(pieces_row)}|"
            lines.append(row)
            lines.append(row_divider)
        return "\n".join(lines)
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

