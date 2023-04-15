import pygame
import os

TAILLE_CASE = 80
TAILLE_ECHIQUIER = 8
# Charger les images des lettres et des chiffres
lettre_image = pygame.image.load("lettre.png")
chiffre_image = pygame.image.load("chiffre.png")


# Charger les images des pièces
def load_images():
    global images
    pieces = ["Pion", "Tour", "Cavalier", "Fou", "Roi", "Reine"]
    images = {}
    for piece in pieces:
        images[piece + "B"] = pygame.image.load(piece.lower() + "blanche.png")
        images[piece + "N"] = pygame.image.load(piece.lower() + "noire.png")
    return images


def case_to_pixel(case):
    return case * TAILLE_CASE


def pixel_to_case(pixel):
    return pixel // TAILLE_CASE


class Echiquier:
    def __init__(self):
        self.initialiser_echiquier()

    def initialiser_echiquier(self):
        self.echiquier = [
            [Tour("N", images["TourN"]), Cavalier("N", images["CavalierN"]), Fou("N", images["FouN"]), Reine("N", images["ReineN"]), Roi("N", images["RoiN"]), Fou("N", images["FouN"]), Cavalier("N", images["CavalierN"]), Tour("N", images["TourN"])],
            [Pion("N", images["PionN"]) for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [Pion("B", images["PionB"]) for _ in range(8)],
            [Tour("B", images["TourB"]), Cavalier("B", images["CavalierB"]), Fou("B", images["FouB"]), Reine("B", images["ReineB"]), Roi("B", images["RoiB"]), Fou("B", images["FouB"]), Cavalier("B", images["CavalierB"]), Tour("B", images["TourB"])]
        ]

    def get_piece(self, case):
        x, y = case
        return self.echiquier[y][x]

    def set_piece(self, case, piece):
        x, y = case
        self.echiquier[y][x] = piece

    def deplacer_piece(self, src, dest):
        piece = self.get_piece(src)
        if piece and piece.deplacement_valide(src, dest, self):
            self.set_piece(dest, piece)
            self.set_piece(src, None)
            return True
        return False


class Piece:
    def __init__(self, couleur, image):
        self.couleur = couleur
        self.image = image

    def deplacement_valide(self, src, dest, echiquier):
        # Vérifie si le déplacement de cette pièce est valide
        pass


class Pion(Piece):
    def deplacement_valide(self, src, dest, echiquier):
        # Implémenter la logique spécifique au pion
        pass


class Tour(Piece):
    def deplacement_valide(self, src, dest, echiquier):
        # Implémenter la logique spécifique à la tour
        pass


class Cavalier(Piece):
    def deplacement_valide(self, src, dest, echiquier):
        # Implémenter la logique spécifique au cavalier
        pass


class Fou(Piece):
    def deplacement_valide(self, src, dest, echiquier):
        # Implémenter la logique spécifique au fou
        pass


class Roi(Piece):
    def deplacement_valide(self, src, dest, echiquier):
        # Implémenter la logique spécifique au roi
        pass


class Reine(Piece):
    def deplacement_valide(self, src, dest, echiquier):
        # Implémenter la logique spécifique à la reine
        pass


def main():
    pygame.init()
    images = load_images()

    # Créer les objets des pièces avec les images correspondantes
    for piece_name, image in images.items():
        if piece_name.startswith("Pion"):
            globals()[piece_name] = Pion(piece_name[4], image)
        elif piece_name.startswith("Tour"):
            globals()[piece_name] = Tour(piece_name[4], image)
        elif piece_name.startswith("Cavalier"):
            globals()[piece_name] = Cavalier(piece_name[8], image)
        elif piece_name.startswith("Fou"):
            globals()[piece_name] = Fou(piece_name[3], image)
        elif piece_name.startswith("Roi"):
            globals()[piece_name] = Roi(piece_name[3], image)
        elif piece_name.startswith("Reine"):
            globals()[piece_name] = Reine(piece_name[5], image)

    screen = pygame.display.set_mode((TAILLE_CASE * TAILLE_ECHIQUIER, TAILLE_CASE * TAILLE_ECHIQUIER))
    pygame.display.set_caption("Jeu d'échecs")

    echiquier = Echiquier()
    clock = pygame.time.Clock()
    running = True
    # Nouvelles couleurs pour les cases
    couleur_claire = (250, 229, 211)  # #FAE5D3
    couleur_foncee = (120, 66, 18)  # #784212
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dessiner l'échiquier et les pièces
        for y in range(TAILLE_ECHIQUIER):
            for x in range(TAILLE_ECHIQUIER):
                rect = pygame.Rect(case_to_pixel(x), case_to_pixel(y), TAILLE_CASE, TAILLE_CASE)
                pygame.draw.rect(screen, couleur_claire if (x + y) % 2 == 0 else couleur_foncee, rect)

                piece = echiquier.get_piece((x, y))
                if piece:
                    screen.blit(piece.image, rect.topleft)

                # Dessiner les images des lettres et des chiffres
        for i in range(1):
                    lettre_rect = pygame.Rect(case_to_pixel(i), TAILLE_ECHIQUIER * TAILLE_CASE, TAILLE_CASE,
                                              TAILLE_CASE)
                    screen.blit(lettre_image, lettre_rect.topleft)

                    chiffre_rect = pygame.Rect(0, case_to_pixel(i), TAILLE_CASE, TAILLE_CASE)
                    screen.blit(chiffre_image, chiffre_rect.topleft)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()


