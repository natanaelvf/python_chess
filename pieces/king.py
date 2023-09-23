from typing import List, Tuple

def get_king_moves(index: int, piece_color: int, bitboards: List[Tuple[int, int]]) -> List[int]:
    available_moves = []

    # Define king move directions (horizontal, vertical, and diagonal)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # Get the opponent's piece bitboard
    opponent_bitboard = bitboards[1 - piece_color]

    for dx, dy in directions:
        x, y = index % 8 + dx, index // 8 + dy
        target_index = x + y * 8

        if 0 <= target_index < 64:
            target_piece = (opponent_bitboard[piece_color] >> target_index) & 1
            if target_piece == 0:
                available_moves.append(target_index)

    return available_moves