from convertions.board_conversion import *
from convertions.square_conversion import *
from board import *
from pieces.piece import *
from folder.moves import *

# Example usage:
board = [
    "r", "n", "b", "q", "k", "b", "n", "r",
    "p", "p", "p", "p", "p", "p", "p", "p",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ",
    "P", "P", "P", "P", "P", "P", "P", "P",
    "R", "N", "B", "Q", "K", "B", "N", "R"
]

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
board = fen_to_board(fen)

# Generate FEN from the board
#generated_fen = board_to_fen(board)

# Assert that the generated FEN and the original FEN are the same
#assert fen == generated_fen

#print("FEN and generated FEN are the same:", fen == generated_fen)

#visualize_board(board)

#white_king = 14
#black_king = 6

#assert has_oponent_piece(white_king, black_king) == has_oponent_piece(black_king, white_king)

#print(string_to_binary_board(board))

#print((white_king & 0b0111) == black_king)

binary_board = string_to_binary_board(board)
available_moves = get_available_moves(binary_board, 0)

"""
# Visualising first move a3
for moves in available_moves :
    piece = moves[1]
    index = moves[0]
    for move in moves:
        print(moves)
        board[moves[3]] = square_binary_to_string(piece)
        board[moves[0]] = " "
        visualize_board(board)
        break
    break
"""