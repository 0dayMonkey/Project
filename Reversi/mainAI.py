
import os
from dotenv import load_dotenv
import time
import random

load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

class Reversi:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = '○'
        self.board[3][4] = '●'
        self.board[4][3] = '●'
        self.board[4][4] = '○'
        self.current_player = '●'

    def display(self):
        print("\033[H\033[J", end="")
        print('  0 1 2 3 4 5 6 7')
        for i, row in enumerate(self.board):
            print(i, ' '.join(row))

    def get_opponent_type(self):
        while True:
            opponent_type = input("Choisissez le type d'adversaire: 'humain' ou 'chatgpt': ")
            if opponent_type.lower() in ['humain', 'chatgpt']:
                return opponent_type.lower()
            else:
                print("Veuillez choisir 'humain' ou 'chatgpt'.")

    def get_max_flips_move(self):
        valid_moves = self.list_valid_moves()
        max_flips = -1
        best_move = None

        for x, y in valid_moves:
            flips = self.get_flips_count(x, y)
            if flips > max_flips:
                max_flips = flips
                best_move = (x, y)

        return best_move

    def get_flips_count(self, x, y):
        flips = 0
        directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            flipped = []
            while 0 <= nx < 8 and 0 <= ny < 8:
                if self.board[ny][nx] == ' ':
                    break
                if self.board[ny][nx] == self.current_player:
                    flips += len(flipped)
                    break
                flipped.append((nx, ny))
                nx += dx
                ny += dy
        return flips

    def valid_move(self, x, y):
        if self.board[y][x] != ' ':
            return False

        directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            flipped = []
            while 0 <= nx < 8 and 0 <= ny < 8:
                if self.board[ny][nx] == ' ':
                    break
                if self.board[ny][nx] == self.current_player:
                    if flipped:
                        return True
                    break
                flipped.append((nx, ny))
                nx += dx
                ny += dy
        return False

    def make_move(self, x, y):
        if not self.valid_move(x, y):
            return False
        directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            flipped = []
            while 0 <= nx < 8 and 0 <= ny < 8:
                if self.board[ny][nx] == ' ':
                    break
                if self.board[ny][nx] == self.current_player:
                    for fx, fy in flipped:
                        self.board[fy][fx] = self.current_player
                    break
                flipped.append((nx, ny))
                nx += dx
                ny += dy

        self.board[y][x] = self.current_player
        self.current_player = '○' if self.current_player == '●' else '●'
        return True

    def has_valid_move(self):
        for x in range(8):
            for y in range(8):
                if self.valid_move(x, y):
                    return True
        return False

    def list_valid_moves(self):
        valid_moves = []
        for x in range(8):
            for y in range(8):
                if self.valid_move(x, y):
                    valid_moves.append((x, y))
        return valid_moves

    def play(self):
        opponent_type = self.get_opponent_type()

        if opponent_type == 'chatgpt':
            ai_player = input("Entrez la couleur du symbole contrôlé par l'IA (Noir pour ● , ○ pour Blanc): ")

            while ai_player != 'Noir' and ai_player != 'Blanc':
                ai_player = input("Symbole invalide. Entrez le symbole du joueur contrôlé par l'IA (Noir pour ● , ○ pour Blanc): ")

            ai_player = '●' if ai_player == 'Noir' else '○'
        else:
            ai_player = None

        while True:
            self.display()
            valid_moves = self.list_valid_moves()
            if valid_moves:
                print(f"Joueur {self.current_player}, coups valides: {', '.join(map(str, valid_moves))}")

                if ai_player and self.current_player == ai_player:
                    move = self.get_max_flips_move()
                    time.sleep(random.uniform(1,2.5))
                    x, y = move
                    print(f"IA ({self.current_player}) joue : {x}, {y}")
                    self.make_move(x, y)
                else:
                    while True:
                        move = input(f"Joueur {self.current_player}, entrez votre coup (x, y): ")
                        x, y = map(int, move.split(','))
                        if self.make_move(x, y):
                            break
                        print("Coup invalide, réessayez.")
            else:
                if not self.has_valid_move():
                    break
                print(f"Le joueur {self.current_player} n'a pas de coup valide.")
                self.current_player = '○' if self.current_player == '●' else '●'

        self.display()
        black_count = sum(row.count('●') for row in self.board)
        white_count = sum(row.count('○') for row in self.board)
        print(f"Score final : Noir ({black_count}) - Blanc ({white_count})")
        if black_count > white_count:
            print("Le joueur Noir remporte la partie !")
        elif white_count > black_count:
            print("Le joueur Blanc remporte la partie !")
        else:
            print("La partie est à égalité !")

if __name__ == "__main__":
    reversi = Reversi()
    reversi.play()

