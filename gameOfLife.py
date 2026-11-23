import time
import random

# Konfiguracija
WIDTH = 10
HEIGHT = 10
ALIVE_PROBABILITY = 0.3
GENERATIONS = 20
DELAY = 0.2


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
    #sugeneruoju 9 kordinaciu kombinacijas kurios eina aplink pasirinkta cell(0,0)
    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
            #skip pasirinkta cella, kad neiskaiciuoti i gyvus
            if row_offset == 0 and col_offset == 0:
                continue

            neighbor_row = row + row_offset
            neighbor_col = col + col_offset

            #tikrinu board ribas
            if (0 <= neighbor_row < height and
                    0 <= neighbor_col < width):
                neighbors += board[neighbor_row][neighbor_col]

    return neighbors

def next_generation(board):
    height = len(board)
    width = len(board[0])

    new_board = []

    for row in range(height):
        new_row = []
        #salygos kada langelis turi but gyvas kada negyvas pagal tasko uzduoti
        for col in range(width):
            neighbors = count_neighbors(board, row, col)
            cell = board[row][col]

            if cell == 1:
                if neighbors == 2 or neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
            else:
                if neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)

        new_board.append(new_row)

    return new_board


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
    # Test case #1 (islieka toks pat nes kiekviena cell turi 3 alive kaimynus)
    # board = [
    # [0, 0, 0, 0],
    # [0, 1, 1, 0],
    # [0, 1, 1, 0],
    # [0, 0, 0, 0]
    # ]
    # Test #2 mirsta kitam decke nes nera gyvu kaimynu
    #     board = [
    #     [0, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 0]
    # ]
    board = create_board(WIDTH, HEIGHT)

    for generation in range(GENERATIONS + 1):
        print(f"\nGeneration {generation}")
        print_board(board)

        if generation < GENERATIONS:
            time.sleep(DELAY)
            board = next_generation(board)

#ensure to execute directly
if __name__ == "__main__":
    main()
