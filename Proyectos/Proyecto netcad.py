import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def ai_move(board):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        return random.choice(empty_cells)
    return None

def tic_tac_toe_vs_ai():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"
    current_player = human

    while True:
        print_board(board)
        
        if current_player == human:
            print("Tu turno (X)")
            try:
                row = int(input("Fila (0-2): "))
                col = int(input("Columna (0-2): "))
            except ValueError:
                print("Entrada inválida. Intenta de nuevo.")
                continue
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = human
                    if check_winner(board, human):
                        print_board(board)
                        print("¡Ganaste!")
                        break
                    current_player = ai
                else:
                    print("Celda ocupada.")
            else:
                print("Posición fuera de rango.")
        else:
            print("Turno de la máquina (O)...")
            row, col = ai_move(board)
            board[row][col] = ai
            if check_winner(board, ai):
                print_board(board)
                print("¡La máquina gana!")
                break
            current_player = human

        if is_full(board):
            print_board(board)
            print("¡Empate!")
            break

tic_tac_toe_vs_ai()