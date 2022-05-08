"""
Unit tests for Chess View
"""
import pytest
from chess_board import ChessBoard
from chess_view import TextView

board_reprs = [
    # Ruy Lopez Opening
    ([((6,4),(4,4)),((1,4),(3,4)),((7,6),(5,5)),((0,1),(2,2)),((7,5),(3,1))],
     "a b c d e f g h\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "8 |r| |b|q|k|b|n|r| 8\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "7 |p|p|p|p| |p|p|p| 7\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "6 | | |n| | | | | | 6\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "5 | |B| | |p| | | | 5\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "4 | | | | |P| | | | 4\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "3 | | | | | |N| | | 3\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "2 |P|P|P|P| |P|P|P| 2\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "1 |R|N|B|Q|K| | |R| 1\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "   a b c d e f g h\n"
     "It is now black's turn."),
    # Stafford Gambit Accepted (multiple captures)
    ([((6,4),(4,4)),((1,4),(3,4)),((7,6),(5,5)),((0,6),(2,5)),((5,5),(3,4)),
      ((0,1),(2,2)),((3,4),(2,2)),((1,3),(2,2))],
     "a b c d e f g h\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "8 |r| |b|q|k|b| |r| 8\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "7 |p|p|p| | |p|p|p| 7\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "6 | | |p| | |n| | | 6\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "5 | | | | | | | | | 5\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "4 | | | | |P| | | | 4\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "3 | | | | | | | | | 3\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "2 |P|P|P|P| |P|P|P| 2\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "1 |R|N|B|Q|K|B| |R| 1\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "   a b c d e f g h\n"
     "It is now white's turn."),
    #Bongcloud Opening
    ([((6,4),(4,4)),((1,4),(3,4)),((7,4),(6,4))],
     "a b c d e f g h\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "8 |r|n|b|q|k|b|n|r| 8\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "7 |p|p|p|p| |p|p|p| 7\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "6 | | | | | | | | | 6\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "5 | | | | |p| | | | 5\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "4 | | | | |P| | | | 4\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "3 | | | | | | | | | 3\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "2 |P|P|P|P|K|P|P|P| 2\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "1 |R|N|B|Q| |B|N|R| 1\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "   a b c d e f g h\n"
     "It is now black's turn."),
]

@pytest.fixture
def board():
    """
    Create a chess board for use in testing.
    """
    return ChessBoard()

@pytest.fixture(params=board_reprs)
def game_repr(request):
    """
    Create a representation of a sequence of moves for use in testing.
    """
    return request.param

def test_draw(board, game_repr, capsys):  # pylint: disable=redefined-outer-name
    """
    Test that the board is correctly represented as a string in different
    conditions.
    Args:
        board: The ChessBoard instance to use.
        game_repr: A tuple where the first element is a list of moves to be made
            in the game, and the second element is a string representing the
            expected string representation of the board after those moves have
            been made.
    """
    moves, board_repr = game_repr
    for row, col in moves:  # pylint: disable=redefined-outer-name
        board.move_piece(row, col)
    view = TextView(board)
    view.draw()
    assert capsys.readouterr().out.strip() == board_repr
