import string
from typing import List, Tuple
from convertions.square_conversion import *
from pieces.piece import *

def board_to_fen(bitboard : List[List[int]]) -> List[int] :
    fen = ""
    empty_count = 0

    for i, square in enumerate(bitboard):
        if square == " ":
            empty_count += 1
        else:
            if empty_count > 0:
                fen += str(empty_count)
                empty_count = 0
            fen += str(square)

        if (i + 1) % 8 == 0:
            if empty_count > 0:
                fen += str(empty_count)
                empty_count = 0
            if i != 63:
                fen += "/"
    return fen

def create_bitboard_from_fen(fen: str) -> List[Tuple[int, int]]:
    bitboards = [(0, 0) for _ in range(6)]
    
    # Split the FEN string to obtain the position part
    fen_parts = fen.split(" ")[0].split("/")

    # Loop through the FEN position characters and map them to piece types and colors
    for rank, fen_rank in enumerate(fen_parts):
        file = 0
        for char in fen_rank:
            if char.isdigit():
                file += int(char)
            else:
                piece_color = WHITE if char.isupper() else BLACK
                piece_type = None

                char = char.lower()
                if char == 'p':
                    piece_type = PAWN
                elif char == 'n':
                    piece_type = KNIGHT
                elif char == 'b':
                    piece_type = BISHOP
                elif char == 'r':
                    piece_type = ROOK
                elif char == 'q':
                    piece_type = QUEEN
                elif char == 'k':
                    piece_type = KING

                if piece_type is not None:
                    square = (7 - rank) * 8 + file
                    black_bitboard, white_bitboard = bitboards[piece_type]
                    if piece_color == BLACK:
                        black_bitboard |= 1 << square
                    else:
                        white_bitboard |= 1 << square
                    bitboards[piece_type] = (black_bitboard, white_bitboard)

                file += 1

    return bitboards

def visualize_bitboards(bitboards: List[Tuple[int, int]]) -> None:
    piece_symbols = {
            0: ['P', 'N', 'B', 'R', 'Q', 'K'],
            1: ['p', 'n', 'b', 'r', 'q', 'k']
    }

    print(" | a | b | c | d | e | f | g | h |")
    print("-+-------------------------------+")

    for row in range(8):
        rank = 8 - row
        row_str = f"{rank}|"

        for col in range(8):
            square = row * 8 + col
            piece_found = False

            for piece_type in range(6):  # Iterate over piece types
                for color in range(2):  # Iterate over both colors
                    if (bitboards[piece_type][color] >> square) & 1:
                        piece_symbol = piece_symbols[color][piece_type]
                        row_str += f" {piece_symbol} |"
                        piece_found = True
                        break

                if piece_found:
                    break

            if not piece_found:
                row_str += "   |"

        print(row_str)
        print("-+-------------------------------+")
