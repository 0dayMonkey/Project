import os
import pygame
from pygame.locals import *

# Initialisation de pygame
pygame.init()

# Constantes
BOARD_SIZE = (552, 552)
SQUARE_SIZE = 69
WHITE = (250, 229, 211)
BROWN = (120, 66, 18)
PIECES_DIR = "assets/"

def load_piece_images():
    global pieces_images
    pieces_images = {}
    for color in ["blanche", "noire"]:
        for piece in ["pion", "tour", "cavalier", "fou", "dame", "roi"]:
            image_path = os.path.join(PIECES_DIR, f"{piece}{color}.png")
            pieces_images[f"{piece}_{color}"] = pygame.image.load(image_path).convert_alpha()


# Fenêtre du jeu
screen = pygame.display.set_mode(BOARD_SIZE)
pygame.display.set_caption("Jeu d'échecs")


# Fonction pour dessiner l'échiquier
def draw_board(screen):
    for x in range(0, BOARD_SIZE[0], SQUARE_SIZE):
        for y in range(0, BOARD_SIZE[1], SQUARE_SIZE):
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, WHITE if (x // SQUARE_SIZE) % 2 == (y // SQUARE_SIZE) % 2 else BROWN, rect)


####################### GESTION DES PIECES ########################

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def get_valid_moves(self, board):
        raise NotImplementedError("La méthode get_valid_moves doit être implémentée par les classes héritées.")

    def move(self, board, new_position):
        if is_valid_move(board, self, new_position):
            board.update_piece_position(self, new_position)
            self.position = new_position
            return True
        return False

    def draw(self, screen):
        piece_key = f"{self.__class__.__name__.lower()}_{self.color}"
        screen.blit(pieces_images[piece_key], (self.position[1] * SQUARE_SIZE, self.position[0] * SQUARE_SIZE))


class Pawn(Piece):
    def get_valid_moves(self, board):
        moves = []
        row, col = self.position

        if self.color == "blanche":
            move_positions = [(row - 1, col)]

            if row == 6:
                move_positions.append((row - 2, col))

            for r, c in move_positions:
                if board.is_empty((r, c)):
                    moves.append((r, c))

            capture_positions = [(row - 1, col - 1), (row - 1, col + 1)]
        else:
            move_positions = [(row + 1, col)]

            if row == 1:
                move_positions.append((row + 2, col))

            for r, c in move_positions:
                if board.is_empty((r, c)):
                    moves.append((r, c))

            capture_positions = [(row + 1, col - 1), (row + 1, col + 1)]

        for r, c in capture_positions:
            if board.is_opponent_piece(self.color, (r, c)):
                moves.append((r, c))

        # TODO: Ajoutez une vérification pour la prise en passant

        return moves


class Rook(Piece):
    def get_valid_moves(self, board):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        return self.get_moves_in_directions(board, directions)


class Knight(Piece):
    def get_valid_moves(self, board):
        row, col = self.position
        potential_moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]

        return [
            move for move in potential_moves
            if board.is_valid_position(move) and not board.is_same_color_piece(self.color, move)
        ]


class Bishop(Piece):
    def get_valid_moves(self, board):
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        return self.get_moves_in_directions(board, directions)


class Queen(Piece):
    def get_valid_moves(self, board):
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        return self.get_moves_in_directions(board, directions)


class King(Piece):
    def get_valid_moves(self, board):
        row, col = self.position
        potential_moves = [
            (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)
        ]

        valid_moves = [
            move for move in potential_moves
            if board.is_valid_position(move) and not board.is_same_color_piece(self.color, move)
        ]
        # TODO: Ajoutez une vérification pour le roque
        return valid_moves


####################### GESTION DU PLATEAU ########################
class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Placer les pièces sur l'échiquier
        for i in range(8):
            self.board[1][i] = Pawn("blanche", (1, i))
            self.board[6][i] = Pawn("noire", (6, i))

        pieces_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece_class in enumerate(pieces_order):
            self.board[0][i] = piece_class("blanche", (0, i))
            self.board[7][i] = piece_class("noire", (7, i))

    def draw(self, screen):
            draw_board(screen)
            for row in self.board:
                for piece in row:
                    if piece:
                        piece.draw(screen)

    def update_piece_position(self, piece, new_position):
            self.board[piece.position[0]][piece.position[1]] = None
            self.board[new_position[0]][new_position[1]] = piece

    def is_game_over(self):
        white_king = None
        black_king = None

        for row in self.board:
            for piece in row:
                if isinstance(piece, King):
                    if piece.color == "blanche":
                        white_king = piece
                    else:
                        black_king = piece

        # Si l'un des rois est absent, la partie est terminée
        if white_king is None or black_king is None:
            return True

        ####################### FONCTIONS UTILITAIRES ########################

def is_valid_move(board, piece, new_position):
            if new_position in piece.get_valid_moves(board):
                if isinstance(piece, King) and piece.can_castle(board, new_position):
                    return True
                if isinstance(piece, Pawn) and piece.can_en_passant(board, new_position):
                    return True
                if isinstance(piece, Pawn) and piece.can_promote(board, new_position):
                    return True
                return True
            return False

def play_against_human(board):
            current_player = "white"
            while not board.is_game_over():
                valid_move = False
                while not valid_move:
                    print(f"C'est au tour des {current_player}.")
                    move = input("Entrez votre mouvement (par ex. 'e2 e4'): ")
                    start, end = move.split()

                    start_x, start_y = ord(start[0]) - ord('a'), int(start[1]) - 1
                    end_x, end_y = ord(end[0]) - ord('a'), int(end[1]) - 1

                    piece = board.get_piece(start_x, start_y)
                    if piece and piece.color == current_player:
                        if is_valid_move(board, piece, (end_x, end_y)):
                            valid_move = True
                            board.move_piece(piece, (end_x, end_y))
                        else:
                            print("Mouvement invalide. Veuillez réessayer.")
                    else:
                        print("Veuillez sélectionner une pièce de votre couleur.")

                current_player = "black" if current_player == "white" else "white"

def play_against_ai(board):
            # TODO: Ajoutez la logique pour jouer contre une IA
            pass

def setup_timer(screen, font, board):
            white_time = 1800  # 30 minutes en secondes
            black_time = 1800  # 30 minutes en secondes

            white_timer = pygame.time.Clock()
            black_timer = pygame.time.Clock()

            current_player = "white"

            while not board.is_game_over() and (white_time > 0 and black_time > 0):
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()

                if current_player == "white":
                    white_time -= white_timer.tick() / 1000
                else:
                    black_time -= black_timer.tick() / 1000

                white_time_text = font.render(f"White: {int(white_time // 60)}:{int(white_time % 60):02}", True,
                                              (0, 0, 0))
                black_time_text = font.render(f"Black: {int(black_time // 60)}:{int(black_time % 60):02}", True,
                                              (0, 0, 0))

                screen.blit(white_time_text, (10, BOARD_SIZE[1] + 10))
                screen.blit(black_time_text, (BOARD_SIZE[0] - 100, BOARD_SIZE[1] + 10))
                board.draw(screen)
                pygame.display.flip()

            if white_time <= 0:
                print("Le temps des Blancs est écoulé. Les Noirs ont gagné!")
            elif black_time <= 0:
                print("Le temps des Noirs est écoulé. Les Blancs ont gagné!")

####################### BOUCLE PRINCIPALE DU JEU ########################


def main():
    board = Board()
    pygame.font.init()
    font = pygame.font.Font(None, 36)

    # Fenêtre du jeu
    screen = pygame.display.set_mode(BOARD_SIZE)
    pygame.display.set_caption("Jeu d'échecs")

    load_piece_images()

    running = True
    clock = pygame.time.Clock()  # Ajout d'une horloge pour contrôler la fréquence de rafraîchissement
    selected_piece = None

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Gestion des clics de souris pour sélectionner et déplacer les pièces
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col, row = x // SQUARE_SIZE, y // SQUARE_SIZE

                # Si une pièce est déjà sélectionnée
                if selected_piece:
                    # Essayez de déplacer la pièce sélectionnée
                    if selected_piece.move(board, (row, col)):
                        # Si le mouvement est valide, désélectionnez la pièce
                        selected_piece = None
                    else:
                        # Si le mouvement n'est pas valide, désélectionnez la pièce
                        selected_piece = None

                # Si aucune pièce n'est sélectionnée, sélectionnez la pièce cliquée
                else:
                    selected_piece = board.board[row][col]

        board.draw(screen)  # Ajout d'un appel à la méthode draw() pour mettre à jour l'affichage
        pygame.display.flip()
        clock.tick(60)  # Limite la fréquence de rafraîchissement à 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()



