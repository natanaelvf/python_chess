from convertions.board_conversion import *
from pieces.piece import BLACK, WHITE

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

def create_bitboard(binary_board):
    # Initialize bitboards for each piece type and color
    bitboards = [[0, 0] for _ in range(6)]  # 7 piece types (0-based indexing)

    for square, piece in enumerate(binary_board):
        if piece == 0:
            continue

        # Determine the color based on the most significant bit (7th bit)
        color = (piece >> 3) & 1

        # Determine the piece type (strip color information)
        piece_type = piece & 0b0111

        # Set the corresponding bit in the bitboard
        bitboards[piece_type][color] |= 1 << square

    return bitboards



