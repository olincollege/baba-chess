"""
Unit tests for tic-tac-toe controller.
"""
import io
import pytest
from chess_board import ChessBoard
from chess_controller import TextController


@pytest.fixture
def board():
    """
    Create a tic tac toe board for use in testing.
    """
    return ChessBoard()


# Test cases for move. Since the prompt repeats until given an valid input, each
# sequence ends with a valid input.
move_cases = [
    # Single valid move.
    ("e2-e4", {((6,4),(4, 4)): "P"}),
    # Multiple valid moves.
    ("e2-e4\nd7-d6", {((6,4),(4, 4)): "P",
                  ((1,3),(2, 3)): "p"}),
    # Only one index given.
    ("e2\ne2-e4", {((6,4),(4, 4)): "P"}),
    # Non-numerical input.
    ("0 abc\nabc 0\nabc def\ne2-e4", {((6,4),(4, 4)): "P"}),
    # Row or column index too large.
    ("b2-b9\nb2-b9\np7-p8\ne2-e4", {((6,4),(4, 4)): "P"}),
    # # Row or column index negative.
    # ("e2, e4\n-1 0\n-1 -1\n0 0", {(0, 0): ChessBoard.player_1_color}),
    # A capture is made on white's 2nd move
    ("f2-f4\nc7-c5\ng1-c5", {((6, 5),(4, 5)): "P",
                       ((1, 2), (3, 2)): "p",
                       ((7, 6), (3, 2)): "N"}),
]

# Define sets of test cases.
translation_cases = [
    # Single valid move.
    ("e2-e4", ((6,4),(4, 4))),
    # Multiple valid moves.
    # ("e2-e4\nd7-d6", ((6,4),(4, 4)),
    #               (1,3),(2, 3)),
    # Only one index given.
    ("e2\ne2-e4", ((6,4),(4, 4))),
    # Non-numerical input.
    ("0 abc\nabc 0\nabc def\ne2-e4", ((6,4),(4, 4))),
    # Row or column index too large.
    ("b2-b9\nb2-b9\np7-p8\ne2-e4", KeyError) ,#((6,4),(4, 4)))
    # # Row or column index negative.
    # ("e2, e4\n-1 0\n-1 -1\n0 0", {(0, 0): ChessBoard.player_1_color}),
    # A capture is made on white's 2nd move
    # ("f2-f4\nc7-c5\ng1-c5", {((6, 5),(4, 5)): "P",
    #                    ((1, 2), (3, 2)): "p",
    #                    ((7, 6), (3, 2)): "N"}),
]

# @pytest.fixture(params=move_cases)
# def move_case(request):
#     """
#     Provide a pair of text input to the move method of the controller and the
#     expected board state.
#     """
#     return request.param


# def test_draw(board, move_case, monkeypatch):  # pylint: disable=redefined-outer-name
#     """
#     Test that the board is correctly represented as a string in different
#     conditions.

#     Args:
#         board: The ChessBoard instance to use.
#         move_case: A tuple consisting of a string representing input to the move
#             method of the TextController instance used, and a dictionary mapping
#             (row, col) tuples to the expected mark found there after the input
#             has been consumed by the controller (the default mark is assumed to
#             be blank).
#     """
#     controller = TextController(board)
#     user_input, check_squares = move_case
#     valid_moves = 0

#     # Patch standard input to pass the text in user_input to the move method.
#     monkeypatch.setattr("sys.stdin", io.StringIO(user_input))

#     # Consume all input until none is left, using it to make moves in the game.
#     try:
#         while True:
#             move = controller.move()
#             if move is None:
#                 valid_moves += 1
#     except EOFError:
#         pass

#     # Check that the move method was called the appropriate number of times.
#     assert valid_moves == len(check_squares)

#     # Check that the board contains exactly the correct marks.
#     for row in range(8):
#         for col in range(8):
#             for key in check_squares:
#                 if (row, col) == key[1]:
#                     assert board.get_piece((row, col)) == check_squares[key]
#             if row >= 2 and row <= 5:
#                 assert board.get_piece((row, col)) == board.blank_square


@pytest.mark.parametrize("lan,tuples", translation_cases)
def test_lan_to_coords(board, lan, tuples):
    """
    Test that the translation from long-algebraic-notation to tuple form is
    implemented properly

    Args:
        board: The ChessBoard instance to use.
        lan: A string representing the user's long algebraic notation. This will
            translated into tuple form for the other game classes to use.
        tuples: A tuple of tuples representing the translated user input. This
            is implemented within the Model class.
    """
    controller = TextController(board)
    assert controller.lan_to_coords(lan) == tuples
