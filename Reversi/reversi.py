import openai
import os
from dotenv import load_dotenv
import random, time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class Reversi:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = '●'
        self.board[3][4] = '○'
        self.board[4][3] = '○'
        self.board[4][4] = '●'
        self.current_player = '○'

    def display(self):
        print("\033[H\033[J", end="")
        print('  0 1 2 3 4 5 6 7')
        for i, row in enumerate(self.board):
            print(i, ' '.join(row))

    def get_opponent_type(self):
        opponent_type = input("Choisissez le type d'adversaire ( 1- Humain  ou 2- ChatGPT): ")
        while opponent_type.lower() not in ['humain', 'chatgpt', 1, 2]:
            opponent_type = input("Type d'adversaire invalide. Choisissez le type d'adversaire (Humain ou ChatGPT): ")
        return opponent_type.lower()

    def get_chatgpt_move(self):
      
      
      """ Version aléatoire 
      valid = self.list_valid_moves()
      time.sleep(random.randint(1,3))
      return random.choice(valid)
      """
      """
      Ancienne methode mais qui m'as bouffer bcp d'argent 
        prompt = f"Jouez à Reversi en tant que joueur {self.current_player}. Le plateau actuel est :\n\n"

        for row in self.board:
            prompt += ''.join(row) + '\n'

        prompt += f'coups valides: {self.list_valid_moves}'

        prompt += f"\nQuel est votre coup, joueur {self.current_player} ?"

        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=10,
            n=1,
            stop=None,
            temperature=0.5,
        )

        move_text = response.choices[0].text.strip()
        move = move_text.split(',')

        if len(move) != 2:
            return None

        try:
            x, y = int(move[0]), int(move[1])
        except ValueError:
            return None

        if not self.valid_move(x, y):
            return None

        return x, y
        """
        

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
        for         dx, dy in directions:
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
        self.current_player = '●' if self.current_player == '○' else '○'
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
            chatgpt_player = input("Entrez la couleur du symbole contrôlé par ChatGPT (Noir pour ○ , Blanc pour ●): ")

            while chatgpt_player != 'Noir' and chatgpt_player != 'Blanc':
                chatgpt_player = input("Symbole invalide. Entrez le symbole du joueur contrôlé par ChatGPT (Noir pour ○ , Blanc pour ●): ")

            chatgpt_player = '○' if chatgpt_player == 'Noir' else '●'
        else:
            chatgpt_player = None

        while True:
            self.display()
            valid_moves = self.list_valid_moves()
            if valid_moves:
                print(f"Joueur {self.current_player}, coups valides: {', '.join(map(str, valid_moves))}")

                if chatgpt_player and self.current_player == chatgpt_player:
                    move = self.get_chatgpt_move()
                    while move is None:
                        move = self.get_chatgpt_move()
                    x, y = move
                    print(f"ChatGPT ({self.current_player}) joue : {x}, {y}")
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
                self.current_player = '●' if self.current_player == '○' else '○'

        self.display()
        black_count = sum(row.count('○') for row in self.board)
        white_count = sum(row.count('●') for row in self.board)
        print(f"Score final : Noir ({black_count}) - Blanc ({white_count})")
        if black_count > white_count:
            print("Le joueur Noir remporte la partie !")
        elif white_count > black_count:
            print("Le joueur Blanc remporte la partie !")
        else:
            print("La partie se termine par un match nul !")


if __name__ == '__main__':
    game = Reversi()
    game.play()

