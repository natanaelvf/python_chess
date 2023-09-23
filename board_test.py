from convertions.board_conversion import *
from convertions.square_conversion import *
from board import *
from pieces.piece import *
from folder.moves import *

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
bitboard = create_bitboard_from_fen(fen)

# Generate FEN from the bitboard
#generated_fen = board_to_fen(bitboard)

# Assert that the generated FEN and the original FEN are the same
#assert fen == generated_fen

#print("FEN and generated FEN are the same:", fen == generated_fen)

#visualize_board(bitboard)

#white_king = 14
#black_king = 6

#assert has_oponent_piece(white_king, black_king) == has_oponent_piece(black_king, white_king)

#print(string_to_binary_board(bitboard))

#print((white_king & 0b0111) == black_king)

#visualize_board(bitboard)

# Visualising first move a3
# Assuming `available_moves` is a list of moves [index, piece, move, move, move, ...]
visualize_bitboards(bitboard)
available_moves = get_available_moves(bitboard, WHITE)

