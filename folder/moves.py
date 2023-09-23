

from typing import List, Tuple, Tuple
from pieces.piece import BISHOP, KING, KNIGHT, PAWN, QUEEN, ROOK
from pieces.bishop import get_bishop_moves
from pieces.knight import get_knight_moves
from pieces.queen import get_queen_moves
from pieces.rook import get_rook_moves
from pieces.pawn import get_pawn_moves
from pieces.king import get_king_moves

def get_available_moves(bitboards: List[Tuple[int, int]], player_color: int) -> List[List[int]]:
    available_moves = []

    # Determine the player's piece bitboard
    player_piece_bitboard = bitboards[player_color][0]  # Assuming we start with PAWN

    for from_square in range(64):
        if not (player_piece_bitboard & (1 << from_square)):
            continue  # Skip empty squares
        
        for piece_type in range(6):
            moves = get_piece_moves(from_square, piece_type, player_color, bitboards)
            if moves:
                # Add the "from" square to each move and group them
                moves_with_from_square = [from_square, moves]
                available_moves = moves_with_from_square

    return available_moves

def get_piece_moves(index: int, piece_type: int, player_color: int, bitboards: List[Tuple[int, int]]) -> List[int]:
    if piece_type == PAWN:
        return get_pawn_moves(index, player_color, bitboards)
    elif piece_type == ROOK:
        return get_rook_moves(index, player_color, bitboards)
    elif piece_type == KING:
        return get_king_moves(index, player_color, bitboards)
    elif piece_type == QUEEN:
        return get_queen_moves(index, player_color, bitboards)
    elif piece_type == KNIGHT:
        return get_knight_moves(index, player_color, bitboards)
    elif piece_type == BISHOP:
        return get_bishop_moves(index, player_color, bitboards)