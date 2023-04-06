import os
import sys
import time
import random
from colorama import Fore, Back, Style, init

init()

RED = Fore.RED + "●" + Style.RESET_ALL
YELLOW = Fore.YELLOW + "●" + Style.RESET_ALL
EMPTY = " "


class ConnectFour:

  def __init__(self):
    self.board = [[EMPTY for _ in range(7)] for _ in range(6)]

  def print_board(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 2)
    for row in self.board:
      print(" ", " ".join(row), " ")
    print(" ", "1 2 3 4 5 6 7", " ")

  def is_full(self):
    for row in self.board:
      if EMPTY in row:
        return False
    return True

  def is_valid_move(self, col):
    return self.board[0][col] == EMPTY

  def get_row(self, col):
    for row in range(len(self.board) - 1, -1, -1):
      if self.board[row][col] == EMPTY:
        return row
    return -1

  def make_move(self, col, token):
    row = self.get_row(col)
    if row != -1:
      self.board[row][col] = token
    return row

  def has_won(self, token):
    for row in range(len(self.board)):
      for col in range(len(self.board[row])):
        if self.board[row][col] == token:
          if self.check_dir(row, col, 1, 0, token) \
                  or self.check_dir(row, col, 0, 1, token) \
                  or self.check_dir(row, col, 1, 1, token) \
                  or self.check_dir(row, col, 1, -1, token):
            return True
    return False

  def check_dir(self, row, col, row_dir, col_dir, token):
    count = 0
    while 0 <= row < len(self.board) and 0 <= col < len(
        self.board[row]) and self.board[row][col] == token:
      count += 1
      row += row_dir
      col += col_dir
    return count >= 4

  def animate_move(self, col, token):
    row = 0
    while row < len(self.board) - 1 and self.board[row + 1][col] == EMPTY:
      self.board[row][col] = token
      self.print_board()
      time.sleep(0.1)
      self.board[row][col] = EMPTY
      row += 1
    self.board[row][col] = token
    self.print_board()

  def play(self):
    print("Choisissez un mode de jeu :")
    print("1. Humain vs. Humain")
    print("2. Humain vs. IA")
    choice = int(input("Entrez 1 ou 2 : "))

    if choice != 1 and choice != 2:
      print("Choix invalide. Fin du programme.")
      sys.exit(1)

    self.print_board()
    player = RED

    while not self.is_full():
      try:
        if choice == 1 or player == RED:
          col = int(
            input(f"Joueur {player}, choisissez une colonne (1-7): ")) - 1
          if not 0 <= col <= 6 or not self.is_valid_move(col):
            raise ValueError
        else:
          # IA compétitive
          col = self.best_move(player)
      except ValueError:
        print("Mouvement invalide. Essayez à nouveau.")
        continue

      self.animate_move(col, player)

      if self.has_won(player):
        print(f"Le joueur {player} a gagné !")
        break

      player = YELLOW if player == RED else RED

    else:
      print("Match nul !")

  def best_move(self, player):

    def score_move(move, depth):
      if self.has_won(player):
        return 100 - depth
      if self.has_won(YELLOW if player == RED else RED):
        return depth - 100
      if self.is_full():
        return 0
      return -1 * self.minimax(depth - 1, not player)

    def make_move(move, player):
      row = self.get_row(move)
      if row != -1:
        self.board[row][move] = player

    def undo_move(move):
      row = self.get_row(move)
      if row != -1 and row + 1 < len(self.board):
        self.board[row + 1][move] = EMPTY

    def minimax(depth, maximizing_player):
      if depth == 0 or self.is_full() or self.has_won(player) or self.has_won(
          YELLOW if player == RED else RED):
        return 0

      best_value = -1000 if maximizing_player else 1000
      for move in range(7):
        if self.is_valid_move(move):
          make_move(
            move, player if maximizing_player else
            (YELLOW if player == RED else RED))
          value = self.minimax(depth - 1, not maximizing_player)
          undo_move(move)

          if maximizing_player:
            best_value = max(best_value, value)
          else:
            best_value = min(best_value, value)

      return best_value

    scores = [score_move(move, 5) for move in range(7)]
    max_score = max(scores)
    best_moves = [i for i, score in enumerate(scores) if score == max_score]
    return random.choice(best_moves)

    scores = [score_move(move, 5) for move in range(7)]
    max_score = max(scores)
    best_moves = [i for i, score in enumerate(scores) if score == max_score]
    return random.choice(best_moves)


if __name__ == "__main__":
  game = ConnectFour()
  game.play()
