# File: game.py
# Name: Xingzuo Li
# Student ID: 2295275

class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
        print('-' * (2 * len(self.board[0]) - 1))
        print(' '.join(str(i) for i in range(len(self.board[0]))))

    def make_move(self, column):
        # Check if the column is within valid range
        if column < 0 or column >= 7:
            print("Invalid column. Please enter a number between 0 and 6.")
            return False

        for row in reversed(range(6)):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return True

        print("Column is full. Please choose a different column.")
        return False

    def play(self):
        print("Welcome to Connect 4!")
        while True:
            self.display_board()
            try:
                col = int(input(f"Player {self.current_player}, choose a column (0-6): "))
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 6.")
                continue

            if not self.make_move(col):
                continue  # Invalid move, retry

            if self.check_win():
                self.display_board()
                print(f"Player {self.current_player} wins! Congratulations!")
                break

            if self.is_board_full():
                self.display_board()
                print("It's a tie! The board is full.")
                break

            self.switch_player()

        # Ask if user wants to play again
        again = input("Do you want to play again? (y/n): ").lower()
        if again == 'y':
            self.__init__()  # Reinitialize the board
            self.play()

    def check_win(self):
        b = self.board
        p = self.current_player

        # Check horizontal
        for row in range(6):
            for col in range(4):  # The last 3 columns can't form a horizontal line of 4
                if b[row][col] == b[row][col + 1] == b[row][col + 2] == b[row][col + 3] == p:
                    return True

        # Check vertical
        for row in range(3):  # Only the top 3 rows can form vertical lines of 4
            for col in range(7):
                if b[row][col] == b[row + 1][col] == b[row + 2][col] == b[row + 3][col] == p:
                    return True

        # Check diagonal ↘
        for row in range(3):
            for col in range(4):
                if b[row][col] == b[row + 1][col + 1] == b[row + 2][col + 2] == b[row + 3][col + 3] == p:
                    return True

        # Check anti-diagonal ↙
        for row in range(3):
            for col in range(3, 7):
                if b[row][col] == b[row + 1][col - 1] == b[row + 2][col - 2] == b[row + 3][col - 3] == p:
                    return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def get_board_cell(self, row, col):
        return self.board[row][col]

    def get_current_player(self):
        return self.current_player
