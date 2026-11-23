
import random

# Configuration
WIDTH = 10
HEIGHT = 10
ALIVE_PROBABILITY = 0.3


def create_board(width, height):
    board = []

    for row in range(height):
        new_row = []

        for col in range(width):
            if random.random() < ALIVE_PROBABILITY:
                new_row.append(1)
            else:
                new_row.append(0)

        board.append(new_row)

    return board

def count_neighbors(board, row, col):
    height = len(board)
    width = len(board[0])

    neighbors = 0

    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:

            if row_offset == 0 and col_offset == 0:
                continue

            neighbor_row = row + row_offset
            neighbor_col = col + col_offset

            if (0 <= neighbor_row < height and
                    0 <= neighbor_col < width):
                neighbors += board[neighbor_row][neighbor_col]

    return neighbors


def print_board(board):
    for row in board:
        line = ""

        for cell in row:
            if cell == 1:
                line += "# "
            else:
                line += ". "

        print(line)


def main():
    board = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]

    print_board(board)

    print("Middle:", count_neighbors(board, 1, 1))
    print("Top-left:", count_neighbors(board, 0, 0))
    print("Bottom-right:", count_neighbors(board, 2, 2))


if __name__ == "__main__":
    main()
