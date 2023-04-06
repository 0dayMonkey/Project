import os
import sys
import time
import random
import pygame

pygame.init()

# Configuration
WINDOW_SIZE = (600, 600)
FPS = 30
CELL_SIZE = 75

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

# Images
BLACK_PIECE = pygame.image.load("black_piece.png")
WHITE_PIECE = pygame.image.load("white_piece.png")


class Reversi:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = '○'
        self.board[3][4] = '●'
        self.board[4][3] = '●'
        self.board[4][4] = '○'
        self.current_player = '●'

    def draw_board(self, screen):
        screen.fill(GREEN)

        # Dessiner les lignes
        for i in range(1, 8):
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE[1]), 2)
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE[0], i * CELL_SIZE), 2)

        # Dessiner les pièces
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell == '●':
                    screen.blit(BLACK_PIECE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
                elif cell == '○':
                    screen.blit(WHITE_PIECE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))

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
    opponent_type = reversi.get_opponent_type()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Reversi")

    clock = pygame.time.Clock()
    if opponent_type == 'chatgpt':
        ai_player = input("Entrez la couleur du symbole contrôlé par l'IA (Noir pour ● , ○ pour Blanc): ")
    
        while ai_player != 'Noir' and ai_player != 'Blanc':
            ai_player = input("Symbole invalide. Entrez le symbole du joueur contrôlé par l'IA (Noir pour ● , ○ pour Blanc): ")
    
        ai_player = '●' if ai_player == 'Noir' else '○'
    else:
        ai_player = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    grid_x, grid_y = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE
                    if reversi.valid_move(grid_x, grid_y):
                        reversi.make_move(grid_x, grid_y)
            
                        # Passer le tour si l'adversaire n'a pas de coups valides
                        if not reversi.has_valid_move():
                            reversi.current_player = '○' if reversi.current_player == '●' else '●'
            
                        if opponent_type == 'chatgpt' and reversi.current_player != reversi.ai_player:
                            move = reversi.get_max_flips_move() 
                            if move:
                                time.sleep(random.uniform(1, 2.5))
                                x, y = move
                                reversi.make_move(x, y)
            
                                # Passer le tour si l'adversaire n'a pas de coups valides
                                if not reversi.has_valid_move():
                                    reversi.current_player = '○' if reversi.current_player == '●' else '●'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Appui sur la touche Échap
                    running = False
                    break            # Ajouter ici la gestion des événements de la souris et du clavier

        reversi.draw_board(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()



