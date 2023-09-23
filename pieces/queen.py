from typing import List, Tuple

def get_queen_moves(index: int, piece_color: int, bitboards: List[Tuple[int, int]]) -> List[int]:
    available_moves = []

    # Determine the color's bitboard
    color_bitboard = bitboards[piece_color]

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Horizontal and vertical
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal
    ]

    for dx, dy in directions:
        for i in range(1, 8):  # Queen can move up to 7 squares in each direction
            x, y = index % 8 + dx * i, index // 8 + dy * i
            target_index = x + y * 8

            if 0 <= target_index < 64:
                target_piece = color_bitboard[piece_color] & (1 << target_index)
                if target_piece == 0:
                    available_moves.append(target_index)
                elif piece_color != ((target_piece >> target_index) >> 3):
                    available_moves.append(target_index)
                    break
                else:
                    break
            else:
                break

    return available_moves