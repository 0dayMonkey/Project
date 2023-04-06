
import random
import time
import numpy as np

prob = [0.4,0.3,0.3]
# nb_pierre, nb_feuille, nb_ciseau
nb_choix = 1
pfc = ["Pierre", "Feuille", "Ciseaux"]


def choix_game(score_bot, score_user, nb_choix,prob):
  prob[0] = round(prob[0],1)
  prob[1] = round(prob[1],1)
  prob[2] = round(prob[2],1)
  print("\033[H\033[J", end="")
  if score_bot == 3:
    print(" Fin du jeux, tu as perdu !")
    rejouer = input("""Rejouer ? y/n : """)
    if rejouer == "y":
      choix_game(0, 0, nb_choix, prob)
    else:
      return
  if score_user == 3:
    print(" Fin du jeux, tu as gagné!")
    rejouer = input("""Rejouer ? y/n : """)
    if rejouer == "y":
      choix_game(0, 0, nb_choix, prob)
    else:
      return
  else:
    print(f'{score_bot} points pour le bot')
    print(f'{score_user} points pour le joueur')
    print(f'{prob}, {nb_choix}')
    choix_bot = np.random.choice([0, 1, 2], p=prob)
    choix = int(
      input("""\n 
    Faites votre choix : 
    [1] Pierre
    [2] Feuille
    [3] Cisceaux 
    [4] Quitter
    \n Choix : """))
    jeux(choix, choix_bot, score_bot, score_user, nb_choix, prob)


def jeux(choix, choix_bot, score_bot, score_user, nb_choix, prob):
  score_bot = score_bot
  score_user = score_user

  if choix == 1:
    if prob[2] == 0:
      prob[1] = prob[1]
      prob[2] = prob[2]
    else:
      prob[1] += 0.1
      prob[2] -= 0.1
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    if choix_bot == 0:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Match nul !")
      return choix_game(score_bot, score_user, nb_choix+1,prob)
    if choix_bot == 1:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Bot gagne !")
      time.sleep(3)
      score_bot += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob)
    if choix_bot == 2:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Tu gagne!")
      time.sleep(3)
      score_user += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob)
  if choix == 2:
    if prob[0] == 0:
      prob[0] = 0
      prob[2] = prob[2]
    else:
      prob[0] -= 0.1   
      prob[2] += 0.1
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    if choix_bot == 0:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Tu gagne !")
      score_user += 1
      time.sleep(3)
      return choix_game(score_bot, score_user, nb_choix+1,prob)
    if choix_bot == 1:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Match nul !")
      time.sleep(3)
      return choix_game(score_bot, score_user, nb_choix+1,prob)
    if choix_bot == 2:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Bot gagne!")
      time.sleep(3)
      score_bot += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob)
  if choix == 3:
    if prob[1] == 0:
      prob[1] = prob[1]
      prob[0] = prob[0]
    else:
      prob[1] -= 0.1
      prob[0] += 0.1  
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    if choix_bot == 0:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Bot gagne !")
      time.sleep(3)
      score_bot += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob)
    if choix_bot == 1:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Tu gagne !")
      time.sleep(3)
      score_user += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob)
    if choix_bot == 2:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Match nul!")
      time.sleep(3)
      return choix_game(score_bot, score_user, nb_choix+1,prob)
  if choix == 4:
    return
  else:
    raise RuntimeError("Vous avez choisi un choix invalide")


choix_game(0, 0, nb_choix,prob)
