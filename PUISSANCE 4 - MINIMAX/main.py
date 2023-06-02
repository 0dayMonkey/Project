import os, time
import numpy as np

matrice_x, matrice_y = os.get_terminal_size()
CONSTANTE_PROFONDEUR = 6


def affichage_grille_interaction(*lignes_):
  for _ligne in lignes_:
    print(_ligne.center(matrice_x))


class PS4:

  def __init__(self, hauteur=6, largeur=7):
    self.binaire = 2**np.arange(hauteur * (largeur + 2), dtype=object)
    self.hauteur, self.largeur = hauteur, min(largeur, 35)
    self.verif_eti = "1234567"[:self.largeur]
    self.grille = np.zeros((self.hauteur, self.largeur + 2), dtype=int)

  def evaluate_state(state):
    player, opposant = 1, 2  # joueur maximisant & joueur minimisant (minimax)

    # max
    if state.verif_win(player):
      return 100

    # mini
    if state.verif_win(opposant):
      return -100

    # dans le cas où on ne trouve ni victoire du côté max et du côté mini, on renvoi 0 pour l'égalité
    return 0

  def generation_mouv(self):
    m = []
    for col in range(self.largeur):
      if np.count_nonzero(self.grille[:, col]) < self.hauteur:
        m.append(col)
    return m

  def minimax(self, profondeur, alpha, beta, maximizing_player):
    if profondeur == 0 or self.verif_win(1) or self.verif_win(2):
      return self.evaluate_state()

    if maximizing_player:
      max_eval = float('-inf')
      for move in self.generation_mouv():
        self.act_mouvement(move, 1)
        eval = self.minimax(profondeur - 1, alpha, beta, False)
        self.undo_mouvement(move)
        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)
        if beta <= alpha:
          break
      return max_eval
    else:
      min_eval = float('inf')
      for move in self.generation_mouv():
        self.act_mouvement(move, 2)
        eval = self.minimax(profondeur - 1, alpha, beta, True)
        self.undo_mouvement(move)
        min_eval = min(min_eval, eval)
        beta = min(beta, eval)
        if beta <= alpha:
          break
      return min_eval

  def max_value(self):
    max_eval = float('-inf')
    best_move = None
    for move in self.generation_mouv():
      self.act_mouvement(move, 1)
      eval = self.minimax(CONSTANTE_PROFONDEUR, float('-inf'), float('inf'),
                          False)
      self.undo_mouvement(move)
      if eval > max_eval:
        max_eval = eval
        best_move = move
    return best_move

  def min_value(self):
    min_eval = float('inf')
    best_move = None
    for move in self.generation_mouv():
      self.act_mouvement(move, 2)
      eval = self.minimax(CONSTANTE_PROFONDEUR, float('-inf'), float('inf'),
                          True)
      self.undo_mouvement(move)
      if eval < min_eval:
        min_eval = eval
        best_move = move
    return best_move

  def act_mouvement(self, colone, player):
    dernier_a_fr = np.count_nonzero(self.grille[:, colone])
    self.grille[dernier_a_fr, colone] = player

  def undo_mouvement(self, colone):
    dernier_a_fr = np.count_nonzero(self.grille[:, colone]) - 1
    self.grille[dernier_a_fr, colone] = 0

  #gitfork
  @property  # https://my.nword.fr/pgc8
  def tour_de(self):
    return np.count_nonzero(self.grille) % 2 + 1

  def affichage_grille(self):
    os.system('cls' if os.name == 'nt' else 'clear')

    milieu, bas, num_col = (
      f"│{'│'.join(' ●○'[value] for value in ligne_[:-2])}│ "
      for ligne_ in self.grille[::-1]
    ), f"╰{'─┴' * (self.largeur - 1)}─╯", f"{' '.join(self.verif_eti)} "
    affichage_grille_interaction(*milieu, bas, num_col)

  def verif_choix(self, choix):
    if not (len(choix) == 1 and choix in self.verif_eti):
      affichage_grille_interaction(
        "Choix incorrect : Choissez une colone valide ! ")
      return False
    colone = self.verif_eti.find(choix)
    if np.count_nonzero(self.grille[:, colone]) < self.hauteur:
      return True

    affichage_grille_interaction(
      "La colone est remplie : faites un autre choix")
    return False

  def choix_choix(self):
    if self.tour_de == 1:
      player = "●"
      while True:
        affichage_grille_interaction(
          f"Au tour du joueur {player}, entrez le numéro de la colonne :\n")
        choix = input("".center(matrice_x // 2)).lower()
        if self.verif_choix(choix):
          return choix
    else:
      player = "○"
      best_move = self.max_value()
      return self.verif_eti[best_move]

  def anim_choix_joueur(self, colone: int):

    player = self.tour_de
    dernier_a_fr = np.count_nonzero(self.grille[:, colone])
    grille = self.grille

    for ligne_ in range(self.hauteur - 1, dernier_a_fr, -1):
      grille[ligne_, colone] = player
      self.affichage_grille()
      grille[ligne_, colone] = 0
      time.sleep(0.07)

    grille[dernier_a_fr, colone] = player

  def verif_win(self, player):
    w = self.largeur
    h = self.hauteur
    grille = self.grille

    # horizontal
    for ligne in range(h):
      for col in range(w - 3):
        if grille[ligne, col] == player and grille[
            ligne,
            col + 1] == player and grille[ligne, col +
                                          2] == player and grille[ligne, col +
                                                                  3] == player:
          return True

    # vertical
    for col in range(w):
      for ligne in range(h - 3):
        if grille[ligne, col] == player and grille[
            ligne + 1,
            col] == player and grille[ligne + 2,
                                      col] == player and grille[ligne + 3,
                                                                col] == player:
          return True

    # diagonale-haut
    for ligne in range(3, h):
      for col in range(w - 3):
        if grille[ligne, col] == player and grille[
            ligne - 1, col +
            1] == player and grille[ligne - 2, col +
                                    2] == player and grille[ligne - 3,
                                                            col + 3] == player:
          return True

    # diagonale-bas
    for ligne in range(h - 3):
      for col in range(w - 3):
        if grille[ligne, col] == player and grille[
            ligne + 1, col +
            1] == player and grille[ligne + 2, col +
                                    2] == player and grille[ligne + 3,
                                                            col + 3] == player:
          return True

    return False

  def jeux(self):
    for _ in range(self.largeur * self.hauteur):
      player = self.tour_de

      self.affichage_grille()
      choix = self.choix_choix()
      colone = self.verif_eti.find(choix)
      self.anim_choix_joueur(colone)

      if self.verif_win(player):
        self.affichage_grille()
        affichage_grille_interaction(f"Le joueur {'●○'[player - 1]} a gagné !")
        break

    else:
      self.affichage_grille()
      affichage_grille_interaction("Egalité ! Vous êtes nuls ! ;)")


if __name__ == '__main__':
  PS4().jeux()

#e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
