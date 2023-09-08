from pieces.piece import *

def get_rook_moves(index, piece, board):
    available_moves = []

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dx, dy in directions:
        for i in range(1, 8):  # Rook can move up to 7 squares in each direction
            x, y = index % 8 + dx * i, index // 8 + dy * i
            target_index = x + y * 8

            if 0 <= target_index < 64:
                target_piece = board[target_index]

                if target_piece == 0 or is_oponent_piece(piece, target_piece):
                    available_moves.append(target_index)
                if target_piece != 0:
                    break
            else:
                break

    return available_moves