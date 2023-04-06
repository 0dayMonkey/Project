
import random
import time
import numpy as np
import sys 
sys.setrecursionlimit(100**4)

prob = [0.4,0.3,0.3]
# nb_pierre, nb_feuille, nb_ciseau
nb_choix = 1
pfc = ["Pierre", "Feuille", "Ciseaux"]

def choix_game(score_bot, score_user, nb_choix,prob,n):
  if nb_choix == n:
    f = open('data.txt','a')
    f.write('\n\n\n' + f"""Nombre de victoire du bot : {score_bot}
      Nombre de victoire du joueur : {score_user}
      Nombre de game : {nb_choix} """)
    f.close()
    n += 200
  prob[0] = round(prob[0],1)
  prob[1] = round(prob[1],1)
  prob[2] = round(prob[2],1)
  print("\033[H\033[J", end="")
  print(f'{score_bot} points pour le bot')
  print(f'{score_user} points pour le joueur')
  print(f'{prob}, {nb_choix}')
  choix_bot = np.random.choice([0, 1, 2], p=prob)
  choix = random.randint(1,3)
  jeux(choix, choix_bot, score_bot, score_user, nb_choix, prob,n)
    
def jeux(choix, choix_bot, score_bot, score_user, nb_choix, prob,n):
  score_bot = score_bot
  score_user = score_user
  print("Le random à choisis", pfc[choix-1])
  if choix == 1:
    if prob[2] == 0:
      prob[1] = prob[1]
      prob[2] = prob[2]
    else:
      prob[1] += 0.1
      prob[2] -= 0.1
    if choix_bot == 0:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Match nul !")
      return choix_game(score_bot, score_user, nb_choix+1,prob,n)
    if choix_bot == 1:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Bot gagne !")
      time.sleep(0.1)
      score_bot += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob,n)
    if choix_bot == 2:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Tu gagne!")
      time.sleep(0.1)
      score_user += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob,n)
  if choix == 2:
    if prob[0] == 0:
      prob[0] = 0
      prob[2] = prob[2]
    else:
      prob[0] -= 0.1   
      prob[2] += 0.1
    if choix_bot == 0:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Tu gagne !")
      score_user += 1
      time.sleep(0.1)
      return choix_game(score_bot, score_user, nb_choix+1,prob,n)
    if choix_bot == 1:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Match nul !")
      time.sleep(0.1)
      return choix_game(score_bot, score_user, nb_choix+1,prob,n)
    if choix_bot == 2:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Bot gagne!")
      time.sleep(0.1)
      score_bot += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob,n)
  if choix == 3:
    if prob[1] == 0:
      prob[1] = prob[1]
      prob[0] = prob[0]
    else:
      prob[1] -= 0.1
      prob[0] += 0.1  
    if choix_bot == 0:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Bot gagne !")
      time.sleep(0.1)
      score_bot += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob,n)
    if choix_bot == 1:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Tu gagne !")
      time.sleep(0.1)
      score_user += 1
      return choix_game(score_bot, score_user, nb_choix+1,prob,n)
    if choix_bot == 2:
      print(f'Bot a joué {pfc[choix_bot]}')
      print("Match nul!")
      time.sleep(0.1)
      return choix_game(score_bot, score_user, nb_choix+1,prob,n)
  if choix == 4:
    return
  else:
    raise RuntimeError("Vous avez choisi un choix invalide")


choix_game(0, 0, nb_choix,prob,200)
