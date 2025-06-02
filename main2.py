board = [' ' for _ in range(9)]  # Initialize the board with 9 empty spaces

def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def check_win():
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return False

def main():
    current_player = 'X'
    while True:
        print_board()
        move = input(f"Player {current_player}, enter your move (1-9): ")
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        move = int(move) - 1
        if board[move] == ' ':
            board[move] = current_player
            result = check_win()
            if result:
                print_board()
                if result == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"Player {result} wins! Congratulations!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That space is already taken. Try again.")

if __name__ == "__main__":
    main()