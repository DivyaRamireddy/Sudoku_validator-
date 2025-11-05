def is_valid_sudoku(board):
    # Validate rows
    for row in board:
        if not is_valid_group(row):
            return False

    # Validate columns
    for col in zip(*board):
        if not is_valid_group(col):
            return False

    # Validate 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_group(subgrid):
                return False

    return True


def is_valid_group(nums):
    """Check if a row/column/subgrid has unique numbers (1–9)."""
    elements = [num for num in nums if num != 0]  # 0 means empty cell
    return len(elements) == len(set(elements)) and all(1 <= num <= 9 for num in elements)


# 🧠 Example Sudoku boards
valid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

invalid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 5]  # duplicate '5' in last row ❌
]


if __name__ == "__main__":
    print("🧩 Sudoku Validator 🧩")
    print("="*30)
    print("Valid Board:", "✅" if is_valid_sudoku(valid_board) else "❌")
    print("Invalid Board:", "✅" if is_valid_sudoku(invalid_board) else "❌")
