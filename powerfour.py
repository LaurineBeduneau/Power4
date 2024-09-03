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

def play_game():
    rows, cols = 6, 7
    board = create_board(rows, cols)
    players = ["X", "O"]
    turn = 0

    print("Bienvenue dans Puissance 4 !")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Joueur {player}, à vous de jouer !")
        try:
            col = int(input("Choisissez une colonne (1-7) : ")) - 1
            if not is_valid_move(board, col):
                print("Coup invalide. Essayez encore.")
                continue
        except ValueError:
            print("Entrée invalide. Entrez un numéro de colonne.")
            continue

        make_move(board, col, player)
        print_board(board)

        if check_win(board, player):
            print(f"Félicitations, joueur {player} a gagné !")
            break

        if is_board_full(board):
            print("La partie est un match nul !")
            break

        turn += 1


if __name__ == "__main__":
    play_game()