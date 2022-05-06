"""
Chess Board Implementation.
"""

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
        # self._error_message = None
        self.fill_generic_board()

    def fill_generic_board(self):
        """
        Fill board with variables and create piece instances.
        """
        self._board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"] # White back row
        self._board[6] = ["P" for _ in range (8)] # White pawns
        
        self._board[1] = ["p" for _ in range(8)] # Black pawns
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

    # def _error_message(self):
    #     """
    #     Return the current error message of the chess board.

    #     #TODO: Add a more descriptive docstring after legal move checker had
    #     # been fully implemented.

    #     Returns:
    #         A string representing the current error for the chess board.
    #     """
    #     return self._error_message
    
    def _flip_next_move(self):
        """
        Change the next player to move.
        """
        if self._next_player == self.player_1_color:
            self._next_player = self.player_2_color
        else:
            self._next_player = self.player_1_color

    def get_piece(self, pos):
        """
        #TODO update this docstring
        Return the piece at the given square of the board.

        The first character returned represents the piece type, while the second
        is the nth piece of that type. When the first character is uppercase,
        the piece is white, when the first character is lowercase, the piece is
        black. "B2" describes the second white bishop.

        Args:
            pos: A tuple representing the position of a given square. The first
            number is the row, the second is the column.
        
        Returns:
            A string representing the piece at a given square. An empty string
            is returned if a piece is empty.
        """
        return self._board[pos[0]][pos[1]]

    def is_occupied(self, pos):
        """
        Returns a bool for if a square is occupied.

        Args:
            pos: A tuple representing the position of a given square. The first
            number is the row, the second is the column.

        Returns:
            True if a square is occupied and false if it is not.
        """
        if self._board[pos[0]][pos[1]] != " ":
            return True
        return False

    def piece_color(self, piece):
        """
        Returns a the color of a piece in a given square.

        Args:
            Piece: A string representing a chess piece. Capitalization
                determines the color of a piece, so"B" would represent a white
                bishop while "b" would represent a black bishop. 
        
        Returns:
            A string representing the color of a given piece. "white" if the
            piece is white, "black" if the piece is black. 
        """
        if piece == " ":
            return "blank"
        if piece.isupper():
            return "white"
        return "black"

    def check_legal_move(self, start_pos, end_pos):
        piece = self.get_piece(start_pos)

        if piece in ["P", "p"]:
            self.check_pawn_move(start_pos, end_pos)
        if piece in ["R", "r"]:
            self.check_rook_move(start_pos, end_pos)
        if piece in ["N", "n"]:
            self.check_knight_move(start_pos, end_pos)
        if piece in ["B", "b"]:
            self.check_bishop_move(start_pos, end_pos)
        if piece in ["Q", "q"]:
            self.check_queen_move(start_pos, end_pos)
        if piece in ["K", "k"]:
            self.check_king_move(start_pos, end_pos)

    def check_pawn_move(self, start_pos, end_pos):
        pass

    def check_rook_move(self, start_pos, end_pos):
        pass

    def check_knight_move(self, start_pos, end_pos):
        pass

    def check_bishop_move(self, start_pos, end_pos):
        pass

    def check_queen_move(self, start_pos, end_pos):
        pass

    def check_king_move(self, start_pos, end_pos):
        pass

    def move_piece(self, start_pos, end_pos):
        """
        Move a specified piece to a new location.

        Args:
            start_pos: A tuple representing the location of the piece to move.
            end_pos: A tuple representing the location to the move the piece to.
        """
        piece = self.get_piece(start_pos)

        # Check if piece is an opponent's piece or a blank square.
        if self.piece_color(piece) != self._next_player:
            print("Not your own piece!")
            raise ValueError

        # Check if move will capture your own piece.
        if self.piece_color(self.get_piece(end_pos)) == self.piece_color(piece):
            print("You cannot capture your own piece!")
            raise ValueError


        
        # Move piece and replace previous square with a blank square.
        self._board[start_pos[0]][start_pos[1]] = self.blank_square
        #if a piece is captured, add it to the pieces_captured list.
        #for the sake of the undo functionality, blanks are also "captured".
        self._pieces_captured.append(self._board[end_pos[0]][end_pos[1]])
        self._board[end_pos[0]][end_pos[1]] = game_piece

        # Adds move to moves_made list and flips the next player to move.
        self._moves_made.append((start_pos, end_pos))
        self._flip_next_move()

    def undo_move(self):
        """
        Given the start and end piece position, undo the previous move.

        Args:
            start_pos: A tuple representing the location of the piece before the move.
            end_pos: A tuple representing the current location of the piece.
        """
        self.move_piece(self._moves_made[-1][1], self._moves_made[-1][0])
        end_pos_0 = self._moves_made[-1][0][0]
        end_pos_1 = self._moves_made[-1][0][1]
        self._board[end_pos_0][end_pos_1] = self._pieces_captured[-2]

    def __repr__(self):
        """
        Return a string representing the contents of the board.
        """
        files = "   a b c d e f g h" 
        row_divider = "  " + ("+-" * 8) + "+"
        lines = [files, row_divider]
        for i in range(8):
            pieces_row = [self._board[i][_][0] for _ in range(8)]
            row = f"{8-i} |{'|'.join(pieces_row)}| {8-i}"
            lines.append(row)
            lines.append(row_divider)
        lines.append(files)
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
#             self._board.get_piece(pos)
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
#                 if self._board.get_piece((row, col)) == " ":
#                     moves.append((row, col))
#             for i in range(-1,2):
#                 (row, col) = (row+1, col+i)
#                 if i == 0:
#                     if self._board.get_piece((row, col)) == " ":
#                         moves.append((row, col))
#                 else:
#                     if self.in_bound((row, col)):
#                         if self._board.get_piece((row, col)) != " " \
#                         or self._board.get_piece((row, col)) != self.is_white():
#                             moves.append((row, col))
#         else:
#             if self.first_move:
#                 (row, col) = (row-2, col)
#                 if self._board.get_piece((row, col)) == " ":
#                     moves.append((row, col))
#             for i in range(-1,2):
#                 (row, col) = (row-1, col+i)
#                 if i == 0:
#                     if self._board.get_piece((row, col)) == " ":
#                         moves.append((row, col))
#                 else:
#                     if self.in_bound((row, col)):
#                         if self._board.get_piece((row, col)) != " " \
#                         or self._board.get_piece((row, col)) != self.is_white():
#                             moves.append((row, col))
#         return moves