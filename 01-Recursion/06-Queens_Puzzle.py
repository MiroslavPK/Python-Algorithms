def can_add_queen(row, col, busy_rows, busy_cols, left_diagonals, right_diagonals):
    left_diagonal = col - row
    right_diagonal = col + row
    row_col_conflict = row in busy_rows or col in busy_cols
    diagonals_conflict = left_diagonal in left_diagonals or right_diagonal in right_diagonals
    if not(row_col_conflict or diagonals_conflict):
        return True


def add_queen(board, row, col, busy_rows, busy_cols, left_diagonals, right_diagonals):
    board[row][col] = '*'
    busy_rows.append(row)
    busy_cols.append(col)
    left_diagonals.append(col - row)
    right_diagonals.append(col + row)


def remove_queen(board, row, col, busy_rows, busy_cols, left_diagonals, right_diagonals):
    if board[row][col] == '*':
        board[row][col] = '-'
        busy_rows.pop()
        busy_cols.pop()
        left_diagonals.pop()
        right_diagonals.pop()


def queen_puzzle(board, row, busy_rows, busy_cols, left_diagonals, right_diagonals):
    if row == 8:
        [print(' '.join(row)) for row in board]
        print()
        return

    for col in range(8):
        if can_add_queen(row, col, busy_rows, busy_cols, left_diagonals, right_diagonals):
            add_queen(board, row, col, busy_rows, busy_cols, left_diagonals, right_diagonals)
            queen_puzzle(board, row + 1, busy_rows, busy_cols, left_diagonals, right_diagonals)
            remove_queen(board, row, col, busy_rows, busy_cols, left_diagonals, right_diagonals)


board = []
[board.append(['-'] * 8) for _ in range(8)]

queen_puzzle(board, 0, [], [], [], [])
