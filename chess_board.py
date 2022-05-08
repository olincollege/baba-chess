"""
Chess Board Implementation.
"""

from selectors import PollSelector


class ChessBoard:
    """
    Chess board with built-in legal move checker.

    Attrubutes:
        player_1_color: A string representing the first player's color.
        player_2_color: A string representing the second player's color.
        blank_square: A string representing a blank square symbol.
        _board: A list of lists representing the squares of the board.
        _next_player: A string representing the color of the player to move.
        _moves_made: A list of tuples representing the moves that have been made.
        _pieces_captured: A list of single character strings representing the pieces that have been captured.
        _undo_flag: An integer representing the 
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
        self._undo_flag = 0
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

    def _in_bound(self, pos):
        """
        Your docsting here
        """
        if pos[0] in range(0,8):
            if pos[1] in range(0,8):
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

    def _opponent_color(self, piece):
        """
        Your docstring goes here.
        """
        if piece == " ":
            return "blank"
        if piece.isupper():
            return "black"
        return "white"

    def check_legal_move(self, start_pos, end_pos):
        """
        Your docstring goes here.
        """
        piece = self.get_piece(start_pos)

        if self.piece_color(piece) != self._next_player:
            print("Not your own piece!")
            raise ValueError

        # Check if move will capture your own piece.
        if self.piece_color(self.get_piece(end_pos)) == self.piece_color(piece):
            print("You cannot capture your own piece!")
            raise ValueError

        if piece in ["P", "p"]:
            legal_moves = self.check_pawn_move(start_pos)
        if piece in ["R", "r"]:
            legal_moves = self.check_rook_move(start_pos)
        if piece in ["N", "n"]:
            legal_moves = self.check_knight_move(start_pos)
        if piece in ["B", "b"]:
            legal_moves = self.check_bishop_move(start_pos)
        if piece in ["Q", "q"]:
            legal_moves = self.check_queen_move(start_pos)
        if piece in ["K", "k"]:
            legal_moves = self.check_king_move(start_pos)

        if end_pos not in legal_moves:
            print("Not a legal move!")
            raise ValueError

    def check_pawn_move(self, start_pos):
        row = start_pos[0]
        col = start_pos[1]
        moves = []
        piece = self.get_piece(start_pos)
        #TODO - Condense code 
        if self.piece_color(piece) == "white":
            if row == 6: #if first move, check the second square ahead
                if self.get_piece((row - 2, col)) == " ": #TODO add check to make sure this does not jump a piece
                    moves.append((row - 2, col))
            for i in range(-1,2):
                test_pos = (row - 1, col + i)
                if self._in_bound(test_pos):
                    if i == 0:
                        if self.get_piece(test_pos) == " ":
                            moves.append(test_pos)
                    elif self.piece_color(self.get_piece(test_pos)) == "black":
                        moves.append(test_pos)
        else:
            if row == 1:
                if self.get_piece((row + 2, col)) == " ":
                    moves.append((row + 2, col))
            for i in range(-1,2):
                test_pos = (row + 1, col + i)
                if self._in_bound(test_pos):
                    if i == 0:
                        if self.get_piece(test_pos) == " ":
                            moves.append(test_pos)
                    elif self.piece_color(self.get_piece(test_pos)) == "white":
                        moves.append(test_pos)
        return moves

    def check_rook_move(self, start_pos):
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        orth = [(1,0), (-1,0), (0,1), (0,-1)] # define directions for movement
        piece_color = self.piece_color(self.get_piece(start_pos))
        for direction in orth:
            for i in range(1,8):
                test_pos = (row + i*direction[0], col + i*direction[1])
                if self._in_bound(test_pos):
                    if self.get_piece(test_pos) == " ":
                        moves.append(test_pos)
                    if self.piece_color(self.get_piece(test_pos)) == piece_color:
                        break
                    if self.piece_color(self.get_piece(test_pos)) not in ["blank", piece_color]:
                        moves.append(test_pos)
                        break
                else:
                    break
        return moves

    def check_knight_move(self, start_pos):
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        in_L = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
        opp_color = self._opponent_color(self.get_piece(start_pos))
        for direction in in_L:
            test_pos = (row + direction[0], col + direction[1])
            if self._in_bound(test_pos):
                if self.piece_color(self.get_piece(test_pos)) in ["blank", opp_color]:
                    moves.append(test_pos)
        return moves

    def check_bishop_move(self, start_pos):
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        piece_color = self.piece_color(self.get_piece(start_pos))
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)] # define directions for movement
        for direction in diag:
            for i in range(1,8):
                test_pos = (row + i*direction[0], col +i*direction[1])
                if self._in_bound(test_pos):
                    if self.get_piece(test_pos) == " ":
                        moves.append(test_pos)
                    if self.piece_color(self.get_piece(test_pos)) == piece_color:
                        break
                    if self.piece_color(self.get_piece(test_pos)) not in ["blank", piece_color]:
                        moves.append(test_pos)
                        break
                else:
                    break
        return moves

    def check_queen_move(self, start_pos):
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        orth = [(1,0), (-1,0), (0,1), (0,-1)] # define directions for movement
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)]
        full = orth + diag
        piece_color = self.piece_color(self.get_piece(start_pos))
        for direction in full:
            for i in range(1,8):
                test_pos = (row + i*direction[0], col + i*direction[1])
                if self._in_bound(test_pos):
                    if self.get_piece(test_pos) == " ":
                        moves.append(test_pos)
                    if self.piece_color(self.get_piece(test_pos)) == piece_color:
                        break
                    if self.piece_color(self.get_piece(test_pos)) not in ["blank", piece_color]:
                        moves.append(test_pos)
                        break
                else:
                    break
        return moves

    def check_king_move(self, start_pos):
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        orth = [(1,0), (-1,0), (0,1), (0,-1)]
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)]
        full = orth + diag # king's range is both orthogonal and diagonal
        opp_color = self._opponent_color(self.get_piece(start_pos))
        for direction in full:
            test_pos = (row + direction[0], col + direction[1])
            if self._in_bound(test_pos):
                if self.piece_color(self.get_piece(test_pos)) in ["blank", opp_color]:
                        moves.append(test_pos)
        return moves

    def move_piece(self, start_pos, end_pos):
        """
        Move a specified piece to a new location.

        Args:
            start_pos: A tuple representing the location of the piece to move.
            end_pos: A tuple representing the location to the move the piece to.
        """
        piece = self.get_piece(start_pos)

        #TODO: Move both if statement into legal move checker and only run
        # legal move checker when a move is not an undo move
        # Check if piece is an opponent's piece or a blank square.
        if self._undo_flag == 0:
            # All-in-one legal move checker.
            self.check_legal_move(start_pos, end_pos)
        
        # Move piece and replace previous square with a blank square.
        self._board[start_pos[0]][start_pos[1]] = self.blank_square
        #if a piece is captured, add it to the pieces_captured list.
        #for the sake of the undo functionality, blanks are also "captured".
        self._pieces_captured.append(self._board[end_pos[0]][end_pos[1]])
        self._board[end_pos[0]][end_pos[1]] = piece

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
        self._undo_flag = 1
        self.move_piece(self._moves_made[-1][1], self._moves_made[-1][0])
        end_pos_0 = self._moves_made[-1][0][0]
        end_pos_1 = self._moves_made[-1][0][1]
        self._board[end_pos_0][end_pos_1] = self._pieces_captured[-2]
        self._undo_flag = 0

    def __repr__(self):
        """
        Return a string representing the contents of the board.
        """
        files = "   a b c d e f g h" 
        # files = "   0 1 2 3 4 5 6 7"
        row_divider = "  " + ("+-" * 8) + "+"
        lines = [files, row_divider]
        for i in range(8):
            pieces_row = [self._board[i][_][0] for _ in range(8)]
            row = f"{8-i} |{'|'.join(pieces_row)}| {8-i}"
            # row = f"{8-i} |{'|'.join(pieces_row)}| {8-i}"
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
