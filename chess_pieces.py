"""
Chess game pieces
"""
from abc import ABC, abstractmethod

class ChessPiece(ABC):
    """
    Abstract base class for defining a chess pieces' attributes
    
    Attributes:
        _board: An ChessBoard instance representing the state of the board to
            determine move legality.
        _pos: A tuple indicating the current position of the piece
        color: A bool value representing whether the piece is white or black.
        first_move: A bool representing that the piece has not been moved from
            its original position.
    """
    def __init__(self, board, pos, color):
        """
        Create a new instance of a piece.
        
        Args:
            board: An instance of ChessBoard
            pos: A tuple representing the position of the piece
            color: A bool value representing the color of the piece.
        """
        self._board = board
        self._color = color
        self.pos = pos
        self.first_move = True
        
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

    @property
    def board(self):
        """
        Return the ChessBoard instance the piece interacts with.
        """
        return self._board

    @property
    def color(self):
        """
        Return whether the piece is black or white
        """
        return self._color

    @abstractmethod
    def possible_moves(self):
        """
        Obtain list of possible moves based on the piece.
        """
        pass


class Pawn(ChessPiece):
    """
    Defines the properties of a Pawn piece
    """
    def is_white(self):
        """
        Return a bool of the piece's color. White = True, Black = False
        """
        return self.color

    def possible_moves(self):
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
        if self.is_white():
            return("P")
        return("p")


class Rook(ChessPiece):
    """
    Defines the properties of a Rook piece
    """
    def is_white(self):
        """
        Return a bool of the piece's color. White = True, Black = False
        """
        return self.color
    
    def possible_moves(self):
        """
        Calculate the possible moves to return a list of possible moves that
        the rook piece could move to based of the position of the rook.
        
        Return: A list of tuples representing the moves that the piece can make.
        """
        moves = []
        row = self.pos[0]
        col = self.pos[1]
        orth = [(1,0), (-1,0), (0,1), (0,-1)] #define directions for movement
        for direction in orth:
            for i in range(7):
                (row, col) = (row + i*direction[0], col +i*direction[1])
                if self.in_bound((row, col)):
                    if self._board.get_square((row, col)) == " " \
                    or self._board.get_square((row, col)) != self.is_white():
                        moves.append((row, col))
                else:
                    break
        return moves

    def __repr__(self):
        if self.is_white():
            return("R")
        return("r")


class Bishop(ChessPiece):
    """
    Defines the properties of a Bishop piece
    """
    def is_white(self):
        """
        Return a bool of the piece's color. White = True, Black = False
        """
        return self.color
    
    def possible_moves(self):
        """
        Calculate the possible moves to return a list of possible moves that
        the bishop piece could move to based of the position of the bishop.
        
        Return: A list of tuples representing the moves that the piece can make.
        """
        moves = []
        row = self.pos[0]
        col = self.pos[1]
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)] #define directions for movement
        for direction in diag:
            for i in range(7):
                (row, col) = (row + i*direction[0], col +i*direction[1])
                if self.in_bound((row, col)):
                    if self._board.get_square((row, col)) == " " \
                    or self._board.get_square((row, col)) != self.is_white():
                        moves.append((row, col))
                else:
                    break
        return moves

    def __repr__(self):
        if self.is_white():
            return("B")
        return("b")


class Knight(ChessPiece):
    """
    Defines the properties of a Knight piece
    """
    def is_white(self):
        """
        Return a bool of the piece's color. White = True, Black = False
        """
        return self.color
    
    def possible_moves(self):
        """
        Calculate the possible moves to return a list of possible moves that
        the knight piece could move to based of the position of the knight.
        
        Return: A list of tuples representing the moves that the piece can make.
        """
        moves = []
        row = self.pos[0]
        col = self.pos[1]
        in_L = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
        for direction in in_L:
            (row, col) = (row + direction[0], col +direction[1])
            if self.in_bound((row, col)):
                if self._board.get_square((row, col)) == " " \
                or self._board.get_square((row, col)) != self.is_white():
                    moves.append((row, col))
            else:
                break
        return moves

    def __repr__(self):
        if self.is_white():
            return("N")
        return("n")


class Queen(ChessPiece):
    """
    Defines the properties of a Queen piece
    """
    def is_white(self):
        """
        Return a bool of the piece's color. White = True, Black = False
        """
        return self.color
    
    def possible_moves(self):
        """
        Calculate the possible moves to return a list of possible moves that
        the queen piece could move to based of the position of the queen.
        
        Return: A list of tuples representing the moves that the piece can make.
        """
        moves = []
        row = self.pos[0]
        col = self.pos[1]
        orth = [(1,0), (-1,0), (0,1), (0,-1)]
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)]
        full = orth + diag #queen range is both orthogonal and diagonal 
        for direction in full:
            for i in range(7):
                (row, col) = (row + i*direction[0], col +i*direction[1])
                if self.in_bound((row, col)):
                    if self._board.get_square((row, col)) == " " \
                    or self._board.get_square((row, col)) != self.is_white():
                        moves.append((row, col))
                else:
                    break
        return moves

    def __repr__(self):
        if self.is_white():
            return("Q")
        return("q")


class King(ChessPiece):
    """
    Defines the properties of a King piece
    """
    def is_white(self):
        """
        Return a bool of the piece's color. White = True, Black = False
        """
        return self.color
    
    def possible_moves(self):
        """
        Calculate the possible moves to return a list of possible moves that
        the king piece could move to based of the position of the king.
        
        Return: A list of tuples representing the moves that the piece can make.
        """
        moves = []
        row = self.pos[0]
        col = self.pos[1]
        orth = [(1,0), (-1,0), (0,1), (0,-1)]
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)]
        full = orth + diag #king' range is both orthogonal and diagonal
        for direction in full:
            (row, col) = (row + direction[0], col + direction[1])
            if self.in_bound((row, col)):
                if self._board.get_square((row, col)) == " " \
                or self._board.get_square((row, col)) != self.is_white():
                    moves.append((row, col))
            else:
                break
        return moves

    def __repr__(self):
        if self.is_white():
            return("K")
        return("k")
