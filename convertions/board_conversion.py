import string
from typing import List
from convertions.square_conversion import *

def fen_to_board(fen : string) -> List:
    board = [" "] * 64  # Initialize an empty board (using a flat list)

    fen_parts = fen.split(" ")
    fen_rows = fen_parts[0].split("/")

    row_index = 0
    col_index = 0

    for fen_row in fen_rows:
        for char in fen_row:
            if char.isdigit():
                col_index += int(char)
            else:
                piece_index = row_index * 8 + col_index
                board[piece_index] = char
                col_index += 1
        row_index += 1
        col_index = 0

    return board

def board_to_fen(board : List[int]) -> List[int] :
    fen = ""
    empty_count = 0

    for i, square in enumerate(board):
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

def string_to_binary_board(board : List[int]) -> List[int] :
    return list(map(lambda square: square_string_to_binary(square), board))

def visualize_board(board : List[int]) -> None:
    print(" | a | b | c | d | e | f | g | h |")
    print("-+-------------------------------+")

    for row in range(8):
        rank = 8 - row
        row_str = f"{rank}|"
        for col in range(8):
            piece = board[row * 8 + col]
            row_str += f" {piece} |"
        print(row_str)
        print("-+-------------------------------+")