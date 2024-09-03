def create_board(rows, cols):
    return [[" " for _ in range(cols)] for _ in range(rows)]

def print_board(board):
    print("\n  " + "   ".join(map(str, range(1, len(board[0]) + 1))))
    print("+" + "---+" * len(board[0]))
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+" * len(row))

def is_valid_move(board, col):
    return 0 <= col < len(board[0]) and board[0][col] == " "

def make_move(board, col, player):
    for row in reversed(board):
        if row[col] == " ":
            row[col] = player
            return

def check_win(board, player):
    rows, cols = len(board), len(board[0])

    # Vérification horizontal
    for row in board:
        for c in range(cols - 3):
            if all(cell == player for cell in row[c:c + 4]):
                return True

    # Vérification vertical
    for c in range(cols):
        for r in range(rows - 3):
            if all(board[r + i][c] == player for i in range(4)):
                return True

    # Vérification diagonal /
    for r in range(3, rows):
        for c in range(cols - 3):
            if all(board[r - i][c + i] == player for i in range(4)):
                return True

        # Vérification diagonal \
        for r in range(rows - 3):
            for c in range(cols - 3):
                if all(board[r + i][c + i] == player for i in range(4)):
                    return True

        return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)