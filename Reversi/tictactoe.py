import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = '●'

    def display(self):
        print(' ' * 3 + '|'.join(self.board[0]))
        print(' ' * 2 + '-' * 7)
        print(' ' * 3 + '|'.join(self.board[1]))
        print(' ' * 2 + '-' * 7)
        print(' ' * 3 + '|'.join(self.board[2]))

    def play(self):
        opponent = input("Voulez-vous jouer contre un autre humain (H) ou contre l'IA (I)? (H/I): ")
        while opponent not in ['H', 'I']:
            opponent = input("Choix invalide. Voulez-vous jouer contre un autre humain (H) ou contre l'IA (I)? (H/I): ")

        if opponent == 'I':
            print("L'IA gagnera forcément.")

        while not self.is_full():
            self.display()
            x, y = self.get_move()
            self.board[y][x] = self.current_player

            if self.is_winner():
                self.display()
                print(f"Le joueur {self.current_player} remporte la partie!")
                return

            self.current_player = '◯' if self.current_player == '●' else '●'
            if opponent == 'I':
                x, y = self.get_best_move()
                self.board[y][x] = self.current_player

                if self.is_winner():
                    self.display()
                    print(f"L'IA (joueur {self.current_player}) remporte la partie!")
                    return

                self.current_player = '◯' if self.current_player == '●' else '●'

        self.display()
        print("Match nul!")

    def get_move(self):
        move = input(f"Joueur {self.current_player}, entrez votre coup (x, y): ")
        x, y = map(int, move.split(','))
        while not self.is_valid_move(x, y):
            move = input("Coup invalide. Réessayez (x, y): ")
            x, y = map(int, move.split(','))
        return x, y

    def is_valid_move(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[y][x] == ' '

    def is_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_full(self):
        return all(self.board[y][x] != ' ' for x in range(3) for y in range(3))

    def get_best_move(self):
        for y in range(3):
            for x in range(3):
                if self.is_valid_move(x, y):
                    self.board[y][x] = self.current_player
                    if self.is_winner():
                        self.board[y][x] = ' '
                        return x, y
                    self.board[y][x] = ' '

        while True:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if self.is_valid_move(x, y):
                return x, y

if __name__ == '__main__':
    game = TicTacToe()
    game.play()
