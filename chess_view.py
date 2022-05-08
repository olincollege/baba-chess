"""
Chess Game View.
"""
from abc import ABC, abstractmethod


class ChessView(ABC):
    """
    The Chess abstracted class representing the controllers for the Chess game.
    """

    def __init__(self, board):
        """
        Initializes the Chess Board view, which takes an instance of the
        Chess board as a parameter, and stores it as a private instance
        attribute.
        """
        self._board = board

    @property
    def board(self):
        """
        Returns the Chess board stores in the Chess board instance.
        """
        return self._board

    @abstractmethod
    def draw(self):
        """
        A draw method that is an abstract method.
        """

class TextView(ChessView):
    """
    The Chess text-based view board. Takes place of the abstracted view class.
    """

    def draw(self):
        """
        Prints the Tic-Tac-Toe board, and identifies the next player to play.
        """
        print(self.board)
        #! Make sure that whatever the next_move function becomes in the future
        #! is changed here as well
        print(f"It is now {self.board.next_player()}'s turn.")
