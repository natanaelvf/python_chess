from typing import List, Tuple

from pieces.piece import ROOK

def get_rook_moves(index: int, piece_color: int, bitboards: List[Tuple[int, int]]) -> List[int]:
    available_moves = []

    # Determine the color's bitboard
    color_bitboard = bitboards[ROOK][piece_color]

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dx, dy in directions:
        x, y = index % 8 + dx, index // 8 + dy
        target_index = x + y * 8

        while 0 <= target_index < 64:
            target_piece = color_bitboard & (1 << target_index)
            if target_piece == 0:
                available_moves.append(target_index)
            elif piece_color != ((target_piece >> target_index) >> 3):
                available_moves.append(target_index)
                break
            else:
                break
            x, y = x + dx, y + dy
            target_index = x + y * 8

    return available_moves