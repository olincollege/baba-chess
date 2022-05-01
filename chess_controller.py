"""
Chess Game Controller.
"""
from abc import ABC, abstractmethod


class ChessController(ABC):
    """
    The Chess abstracted class representing the controllers for the Chess game.
    """

    def __init__(self, board):
        """
        Initializes the Chess Board controller, which takes an instance of the
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
    def move(self):
        """
        A move method that is an abstract method. Used to control the input to
        the Chess game.
        """

class TextController(ChessController):
    """
    The Chess controller that takes in player input and feeds it to the Chess
    game. Takes place of the abstracted move class.
    """

    def move(self):
        """
        Takes in a player input based on the spaces avaliable on the Chess
        board. The player input has to be both the start position and end
        position of the moves.
        """
        coordinates = []
        try:
            input_number = input("Choose the piece you'd like to move and your "
                                "end location(row_start column_start, row_end "
                                "column_end):")
            # If the move inputted by the player is "quit", the game is over.
            if input_number == "quit" or input_number == "undo":
                return input_number
            input_number_list = [i for i in input_number.split(", ")]

            for coords in input_number_list:
                coordinates += [int(i) for i in coords.split()]

            # Start Location, End Location
            coordinate_tuples = [(coordinates[0], coordinates[1]), \
                                (coordinates[2], coordinates[3])]

            if coordinates[0] < 0 or \
                    coordinates[1] < 0 or \
                    coordinates[2] < 0 or \
                    coordinates[3] < 0 or \
                    input_number == "":
                raise IndexError

            self._board.move_piece(coordinate_tuples[0], coordinate_tuples[1])
        except (ValueError, IndexError):
            print(f"Error: '{input_number}' is not a valid move")
            self.move()
