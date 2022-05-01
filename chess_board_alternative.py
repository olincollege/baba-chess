"""
Chess Board Implementation.
"""

#from shutil import move
#from tokenize import blank_re

#from numpy import moveaxis
#from pyparsing import White
#from sqlalchemy import BLANK_SCHEMA
#from chess_pieces import Pawn, Rook, Bishop, Knight, Queen, King

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
        self._moves_made = []
        self._pieces_captured = []
        self.fill_generic_board()

    def fill_generic_board(self):
        """
        Fill board with variables and create piece instances.
        """
        self._board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"] # White back row
        self._board[6] = ["P" + str(_) for _ in range (8)] # White pawns
        
        self._board[1] = ["p" + str(_) for _ in range(8)] # Black pawns
        self._board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"] # Black back row

    def next_player(self):
        """
        Return the color of the next player to move.

        Returns:
            A string representing the next player's color (white or black).
        """
        #TODO decide between representing the next player as a bool or a string.
        #* Chose to represent next player as a string
        return self._next_player
    
    def _flip_next_move(self):
        """
        Change the next player to move.
        """
        if self._next_player == self.player_1_color:
            self._next_player = self.player_2_color
        else:
            self._next_player = self.player_1_color

    def get_square(self, pos):
        """
        Return the piece at the given square of the board.

        The first character returned represents the piece type, while the second
        is the nth piece of that type. When the first character is uppercase,
        the piece is white, when the first character is lowercase, the piece is
        black. "B2" describes the second white bishop.

        Args:
            row: An int representing the index of the row of the board to get.
            col: An int representing the index of the column of the board to
                get.
        
        Returns:
            A string representing the piece at a given square. 
        """
        return self._board[pos[0]][pos[1]]

    def get_square_properties(self, row, column):
        #TODO Will be used for legal move checker, to be implemented later
        pass

    def move_piece(self, start_pos, end_pos):
        """
        Move a specified piece to a new location.

        Args:
            start_pos: A tuple representing the location of the piece to move.
            end_pos: A tuple representing the location to the move the piece to.
        """
        #! Changed `move` from `move` to `move_piece` because move is an
        #! abstract method in the controller class.
        game_piece = self.get_square(start_pos)
        self._board[start_pos[0]][start_pos[1]] = self.blank_square
        #if a piece is captured, add it to the pieces_captur
        if self._board[end_pos[0]][end_pos[1]] != self.blank_square:
            self._pieces_captured.append(self._board[end_pos[0]][end_pos[1]])
        self._board[end_pos[0]][end_pos[1]] = game_piece

        # Flips the next player to move.
        self._moves_made.append((start_pos, end_pos))
        self._flip_next_move()

    def undo_move(self, start_pos, end_pos):
        """
        Given the start and end piece position, undo the previous move.

        Args:
            start_pos: A tuple representing the location of the piece before the move.
            end_pos: A tuple representing the current location of the piece.
        """
        self.move_piece(self._moves_made[-1][1], self._moves_made[-1][0])

    def __repr__(self):
        """
        Return a string representing the contents of the board.
        """
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

    
"""

# def in_bound(self, pos):
#         """
#         Check that a position is within the bounds of the board.
        
#         Args:
#             pos: A tuple representing the position the piece is wants to access.
            
#         Return:
#             A bool representing whether the square is valid or not.
#         """
#         try: 
#             self._board.get_square(pos)
#             return True
#         except (IndexError):
#             return False

#     def is_white(self):
#         """
#         Return a bool of the piece's color. White = True, Black = False
#         """
#         return self.color

#     def check_pawn_move(self, pos, color):
#         """
#         Calculate the possible moves to return a list of possible moves that
#         the pawn piece could move to based of the position of the pawn.
        
#         Return: A list of tuples representing the moves that the piece can make.
#         """
#         row = self.pos[0]
#         col = self.pos[1]
#         moves = []
#         #TODO - Condense code 
#         if self.is_white():
#             if self.first_move: #if first move, check the second square ahead
#                 (row, col) = (row+2, col)
#                 if self._board.get_square((row, col)) == " ":
#                     moves.append((row, col))
#             for i in range(-1,2):
#                 (row, col) = (row+1, col+i)
#                 if i == 0:
#                     if self._board.get_square((row, col)) == " ":
#                         moves.append((row, col))
#                 else:
#                     if self.in_bound((row, col)):
#                         if self._board.get_square((row, col)) != " " \
#                         or self._board.get_square((row, col)) != self.is_white():
#                             moves.append((row, col))
#         else:
#             if self.first_move:
#                 (row, col) = (row-2, col)
#                 if self._board.get_square((row, col)) == " ":
#                     moves.append((row, col))
#             for i in range(-1,2):
#                 (row, col) = (row-1, col+i)
#                 if i == 0:
#                     if self._board.get_square((row, col)) == " ":
#                         moves.append((row, col))
#                 else:
#                     if self.in_bound((row, col)):
#                         if self._board.get_square((row, col)) != " " \
#                         or self._board.get_square((row, col)) != self.is_white():
#                             moves.append((row, col))
#         return moves

