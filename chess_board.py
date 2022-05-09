"""
Chess Board Implementation.
"""

def in_bound(pos):
    """
    Return a bool based on if a position is on the board.

    Positions outside of the 0-7 are considered outside of the board, so there
    are 64 valid spots on the board.

    Args:
        pos: A tuple representing the position of a given square. The first
        number is the row, the second is the column.

    Returns:
        A bool representing if a position is on the board. True if it is,
        false if it is not.
    """
    if pos[0] in range(0,8):
        if pos[1] in range(0,8):
            return True
    return False

def get_piece_color(piece):
    """
    Return the color of a piece in a given square.

    Args:
        piece: A string representing a chess piece.

    Returns:
        A string representing the color of a given piece. "white" if the
        piece is white, "black" if the piece is black, and "blank" if
        there is no piece at the given square.
    """
    # Check if a piece is uppercase or lowercase to determine its color.
    if piece == " ":
        return "blank"
    if piece.isupper():
        return "white"
    return "black"

def opponent_color(piece):
    """
    Return the opponent color of a piece in a given square.

    Args:
        piece: A string representing a chess piece.

    Returns:
        A string representing the opponent color of a given piece. "white"
        if the piece is white, "black" if the piece is black, and "blank" if
        there is no piece at the given square.
    """
    # Check if a piece is uppercase or lowercase to determine the color of its
    # opponenet.
    if piece == " ":
        return "blank"
    if piece.isupper():
        return "black"
    return "white"

class ChessBoard:
    """
    Chess board with built-in legal move checker.

    Attrubutes:
        player_1_color: A string representing the first player's color.
        player_2_color: A string representing the second player's color.
        blank_square: A string representing a blank square symbol.
        _board: A list of lists representing the squares of the board.
        _next_player: A string representing the color of the player to move.
        _moves_made: A list of tuples representing the moves that have been
            made.
        _pieces_captured: A list of single character strings representing the
            pieces that have been captured.
        _undo_flag: An integer representing the undo state of a move.
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
        Fill chess board with piece string representations.

        Uppercase strings represent white pieces, while lowercase strings
        represent black pieces. Strings represent pieces as the following:
        "R" = Rook, "N" = Knight, "B" = Bishop, "Q" = Queen, and "K" = King.
        """
        # White back row and pawns
        self._board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        self._board[6] = ["P" for _ in range (8)]

        # Black back row and pawns
        self._board[1] = ["p" for _ in range(8)]
        self._board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]

    def next_player(self):
        """
        Return the color of the next player to move.

        Returns:
            A string representing the next player's color (white or black).
        """
        return self._next_player

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
        Return the piece at the given square of the board.

        Args:
            pos: A tuple representing the position of a given square. The first
            number is the row, the second is the column.

        Returns:
            A string representing the piece at a given square. An empty string
            is returned if a square is empty.
        """
        return self._board[pos[0]][pos[1]]

    def check_legal_move(self, start_pos, end_pos):
        """
        Based on a start and end position as well as the piece type, check the
        legality of a move.

        Args:
            start_pos: A tuple representing the start position of the piece
            being moved.
            end_pos: A tuple representing the position the piece would like to
            be moved to.
        """
        piece = self.get_piece(start_pos)

        # Check the piece being moved belongs to the player
        if get_piece_color(piece) != self._next_player:
            print("Not your own piece!")
            raise ValueError

        # Check if move will capture a player's own piece.
        if get_piece_color(self.get_piece(end_pos)) == get_piece_color(piece):
            print("You cannot capture your own piece!")
            raise ValueError

        # Based on the piece being moved, run the coresponding legal move
        # generator.
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

        # Based on the list of legal moves returned by the legal move generator,
        # determine if the end position is in the list of legal moves.
        if end_pos not in legal_moves:
            print("Not a legal move!")
            raise ValueError

    def check_pawn_move(self, start_pos):
        """
        Based on the start position of a pawn, return a list of legal moves.

        Args:
            start_pos: A tuple representing the start position of the pawn.

        Returns:
            A list of tuples representing the legal moves of the pawn.
        """
        row = start_pos[0]
        col = start_pos[1]
        moves = []
        piece = self.get_piece(start_pos)
        # Legal move checker for white pawns.
        if get_piece_color(piece) == "white":
            if row == 6: # Determine if the pawn is in the starting position.
                if self.get_piece((row - 2, col)) == " " and \
                    self.get_piece((row - 1, col)) == " ":
                    moves.append((row - 2, col))
            # Check the three positions in front of the pawn to determine if
            # they are legal moves.
            for i in range(-1,2):
                test_pos = (row - 1, col + i)
                if in_bound(test_pos):
                    if i == 0:
                        if self.get_piece(test_pos) == " ":
                            moves.append(test_pos)
                    elif get_piece_color(self.get_piece(test_pos)) == "black":
                        moves.append(test_pos)
        # Legal move checker for black pawns.
        else:
            if row == 1: # Determine if the pawn is in the starting position.
                if self.get_piece((row + 2, col)) == " " and \
                    self.get_piece((row + 1, col)) == " ":
                    moves.append((row + 2, col))
            # Check the three positions in front of the pawn to determine if
            # they are legal moves.
            for i in range(-1,2):
                test_pos = (row + 1, col + i)
                if in_bound(test_pos):
                    if i == 0:
                        if self.get_piece(test_pos) == " ":
                            moves.append(test_pos)
                    elif get_piece_color(self.get_piece(test_pos)) == "white":
                        moves.append(test_pos)
        return moves

    def check_rook_move(self, start_pos):
        """
        Based on the start position of a rook, return a list of legal moves.

        Args:
            start_pos: A tuple representing the start position of the rook.

        Returns:
            A list of tuples representing the legal moves of the pawn.
        """
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        orth = [(1,0), (-1,0), (0,1), (0,-1)] # define directions for movement
        piece_color = get_piece_color(self.get_piece(start_pos))
        # For each direction of movement, progressively check squares futher
        # from the start position.
        for direction in orth:
            for i in range(1,8):
                test_pos = (row + i*direction[0], col + i*direction[1])
                if in_bound(test_pos):
                    # If the square is not occupied, append it to the list of
                    # legal moves.
                    if self.get_piece(test_pos) == " ":
                        moves.append(test_pos)
                    # If the square is occupied by a piece of the same color,
                    # stop searching for legal moves in that direction.
                    if get_piece_color(self.get_piece(test_pos)) == \
                        piece_color:
                        break
                    # If the square is occupied by a piece of the opponent's
                    # color, append the square as a legal move and stop
                    # searching in that direction.
                    if get_piece_color(self.get_piece(test_pos)) not in \
                        ["blank", piece_color]:
                        moves.append(test_pos)
                        break
                else:
                    break
        return moves

    def check_knight_move(self, start_pos):
        """
        Based on the start position of a knight, return a list of legal moves.

        Args:
            start_pos: A tuple representing the start position of the knight.

        Returns:
            A list of tuples representing the legal moves of the knight.
        """
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        possible_moves = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), \
            (-2,1), (-2,-1)] # Define all knight possible moves
        opp_color = opponent_color(self.get_piece(start_pos))
        # For each possible move, check if it is in-bound and either un-occupied
        # or occupied by an opponent piece.
        for direction in possible_moves:
            test_pos = (row + direction[0], col + direction[1])
            if in_bound(test_pos):
                if get_piece_color(self.get_piece(test_pos)) in \
                    ["blank", opp_color]:
                    moves.append(test_pos)
        return moves

    def check_bishop_move(self, start_pos):
        """
        Based on the start position of a bishop, return a list of legal moves.

        Args:
            start_pos: A tuple representing the start position of the bishop.

        Returns:
            A list of tuples representing the legal moves of the bishop.
        """
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        piece_color = get_piece_color(self.get_piece(start_pos))
        # Define directions formovement.
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)]
        # For each direction of movement, progressively check squares futher
        # from the start position.
        for direction in diag:
            for i in range(1,8):
                test_pos = (row + i*direction[0], col +i*direction[1])
                if in_bound(test_pos):
                    # If the square is not occupied, append it to the list of
                    # legal moves.
                    if self.get_piece(test_pos) == " ":
                        moves.append(test_pos)
                    # If the square is occupied by a piece of the same color,
                    # stop searching for legal moves in that direction.
                    if get_piece_color(self.get_piece(test_pos)) == \
                        piece_color:
                        break
                    # If the square is occupied by a piece of the opponent's
                    # color, append the square as a legal move and stop
                    # searching in that direction.
                    if get_piece_color(self.get_piece(test_pos)) not in \
                        ["blank", piece_color]:
                        moves.append(test_pos)
                        break
                else:
                    break
        return moves

    def check_queen_move(self, start_pos):
        """
        Based on the start position of a queen, return a list of legal moves.

        Args:
            start_pos: A tuple representing the start position of the queen.

        Returns:
            A list of tuples representing the legal moves of the queen.
        """
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        orth = [(1,0), (-1,0), (0,1), (0,-1)] # Define directions for movement.
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)]
        full = orth + diag
        piece_color = get_piece_color(self.get_piece(start_pos))
        # For each direction of movement, progressively check squares futher
        # from the start position.
        for direction in full:
            for i in range(1,8):
                test_pos = (row + i*direction[0], col + i*direction[1])
                if in_bound(test_pos):
                    # If the square is not occupied, append it to the list of
                    # legal moves.
                    if self.get_piece(test_pos) == " ":
                        moves.append(test_pos)
                    # If the square is occupied by a piece of the same color,
                    # stop searching for legal moves in that direction.
                    if get_piece_color(self.get_piece(test_pos)) == \
                        piece_color:
                        break
                    # If the square is occupied by a piece of the opponent's
                    # color, append the square as a legal move and stop
                    # searching in that direction.
                    if get_piece_color(self.get_piece(test_pos)) not in \
                        ["blank", piece_color]:
                        moves.append(test_pos)
                        break
                else:
                    break
        return moves

    def check_king_move(self, start_pos):
        """
        Based on the start position of a king, return a list of legal moves.

        Args:
            start_pos: A tuple representing the start position of the king.

        Returns:
            A list of tuples representing the legal moves of the king.
        """
        moves = []
        row = start_pos[0]
        col = start_pos[1]
        orth = [(1,0), (-1,0), (0,1), (0,-1)]
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)]
        full = orth + diag # King's range is both orthogonal and diagonal.
        opp_color = opponent_color(self.get_piece(start_pos))
        # For each possible move, check if it is in-bound and either un-occupied
        # or occupied by an opponent piece.
        for direction in full:
            test_pos = (row + direction[0], col + direction[1])
            if in_bound(test_pos):
                if get_piece_color(self.get_piece(test_pos)) in \
                    ["blank", opp_color]:
                    moves.append(test_pos)
        return moves

    def move_piece(self, start_pos, end_pos):
        """
        Move a specified piece to a new location.

        Additionally, if a move is not an undo move, run the legal move checker.

        Args:
            start_pos: A tuple representing the start position of the piece
            being moved.
            end_pos: A tuple representing the position the piece would like to
            be moved to.
        """
        piece = self.get_piece(start_pos)

        # If a move is not an undo move, run the legal move checker.
        if self._undo_flag == 0:
            self.check_legal_move(start_pos, end_pos)

        # Move piece and replace previous square with a blank square.
        self._board[start_pos[0]][start_pos[1]] = self.blank_square
        # If a piece is captured, add it to the pieces_captured list.
        # For the sake of the undo functionality, blanks are also "captured".
        self._pieces_captured.append(self._board[end_pos[0]][end_pos[1]])
        self._board[end_pos[0]][end_pos[1]] = piece

        # Add move to moves_made list and flip the next player to move.
        self._moves_made.append((start_pos, end_pos))
        self._flip_next_move()

    def undo_move(self):
        """
        Given the start and end piece position, undo the previous move.
        """
        # Set an undo flag to ensure the legal move checker does not run.
        self._undo_flag = 1

        # Run the move method in reverse from the list of moves made and replace
        # pieces on the board with the list of captured pieces.
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
        row_divider = "  " + ("+-" * 8) + "+"
        lines = [files, row_divider]
        # Run through the board and format accordingly.
        for i in range(8):
            pieces_row = [self._board[i][_][0] for _ in range(8)]
            row = f"{8-i} |{'|'.join(pieces_row)}| {8-i}"
            lines.append(row)
            lines.append(row_divider)
        lines.append(files)
        return "\n".join(lines)
