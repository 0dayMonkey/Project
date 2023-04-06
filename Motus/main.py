from random import choice
import unidecode as ud #pip install unidecode // pip3 install unidecode

liste_mot = [word.strip() for word in open("mots.txt", encoding="utf-8")]

"""


Phase 1 : Choix du mot et prérequis


"""


# On verifie si le mot contient bien uniquement des lettres de l'alphabet (sans autres caracteres)
def conditions_lettre(mot):
  for car in mot:
    if not 97 <= ord(car) <= 122:
      return False
  return True


# on verifie si le mot  possede les 7 lettres
def nombre_lettre(mot):
  if len(mot) == 7:
    return True
  if len(mot) > 7 or len(mot) < 7:
    return False


# on verifie les deux ( clareté )
def condi(mot):
  if conditions_lettre(mot) == True and nombre_lettre(mot) == True:
    return True
  else:
    return False


mot_random = choice(liste_mot)


while condi(mot_random) == False:
  mot_random = choice(liste_mot)
  # print(random)

# on attribue chaque lettre à un variable ( utile par la suite )
split_mot_random = list(mot_random)
lettre1 = split_mot_random[0]
lettre2 = split_mot_random[1]
lettre3 = split_mot_random[2]
lettre4 = split_mot_random[3]
lettre5 = split_mot_random[4]
lettre6 = split_mot_random[5]
lettre7 = split_mot_random[6]

# on utilise une class pour gerer les couleurs ( on aurait pu le faire pour la verification mais flemme maintenant ) et eviter d'import
class couleurs:
    GRIS,VERT,RESET,GRAS,SOULIGNER = '\033[30m','\033[92m', '\033[0m', '\033[1m','\033[4m'
   # RESET sinon la couleur continue de se s'afficher


"""

Phase 2 : Initialisation de la vérification


"""

  ##################################### Verifications ########################################


def verif_lettre1(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7):
    if choix_joueur_sous_condition[0] == lettre1:
      ar1 = lettre1.upper()
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition) 
        rt1[0] = lettre1.upper()
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition) 
        rt2[0] = lettre1.upper()
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition) 
        rt3[0] = lettre1.upper()
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition) 
        rt4[0] = lettre1.upper()
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition) 
        rt5[0] = lettre1.upper()
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition) 
        rt6[0] = lettre1.upper()
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition) 
        rt7[0] = lettre1.upper()
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    
    elif choix_joueur_sous_condition[0] in mot_random:
      if essaie == 1:
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    else:
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition)
        rt1[0] = "*"
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition)
        rt2[0] = "*"
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[0] = "*"
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition)
        rt4[0] = "*"
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition)
        rt5[0] = "*"
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition)
        rt6[0] = "*"
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition)
        rt7[0] = "*"
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
 
  
def verif_lettre2(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7):  
    if choix_joueur_sous_condition[1] == lettre2:
      ar2 = lettre2.upper()
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition) 
        rt1[1] = lettre2.upper()
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition) 
        rt2[1] = lettre2.upper()
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition) 
        rt3[1] = lettre2.upper()
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition) 
        rt4[1] = lettre2.upper()
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition) 
        rt5[1] = lettre2.upper()
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition) 
        rt6[1] = lettre2.upper()
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition) 
        rt7[1] = lettre2.upper()
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        
    elif choix_joueur_sous_condition[1] in mot_random:
      ar2 = choix_joueur_sous_condition[1]
      if essaie == 1:
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    else:
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition)
        rt1[1] = "*"
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition)
        rt2[1] = "*"
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[1] = "*"
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition)
        rt4[1] = "*"
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition)
        rt5[1] = "*"
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition)
        rt6[1] = "*"
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition)
        rt7[1] = "*"
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        
def verif_lettre3(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7):
    if choix_joueur_sous_condition[2] == lettre3:
      ar3 = lettre3.upper()
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition) 
        rt1[2] = lettre3.upper()
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition) 
        rt2[2] = lettre3.upper()
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[2] = lettre3.upper()
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition) 
        rt4[2] = lettre3.upper()
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition) 
        rt5[2] = lettre3.upper()
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition) 
        rt6[2] = lettre3.upper()
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition) 
        rt7[2] = lettre3.upper()
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    elif choix_joueur_sous_condition[2] in mot_random:
      ar3 = choix_joueur_sous_condition[2]
      if essaie == 1:
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)  
      if essaie == 7:
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    else:
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition)
        rt1[2] = "*"
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition)
        rt2[2] = "*"
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[2] = "*"
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition)
        rt4[2] = "*"
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition)
        rt5[2] = "*"
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition)
        rt6[2] = "*"
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition)
        rt7[2] = "*"
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        

def verif_lettre4(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7):   
    if choix_joueur_sous_condition[3] == lettre4:
      ar4 = lettre4.upper()
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition) 
        rt1[3] = lettre4.upper()
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition) 
        rt2[3] = lettre4.upper()
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[3] = lettre4.upper()
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition) 
        rt4[3] = lettre4.upper()
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition) 
        rt5[3] = lettre4.upper()
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition) 
        rt6[3] = lettre4.upper()
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition) 
        rt7[3] = lettre4.upper()
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        
    elif choix_joueur_sous_condition[3] in mot_random:
        ar4 = choix_joueur_sous_condition[3]
        if essaie == 1:
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 2:
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 3:
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 4:
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 5:
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 6:
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 7:
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    else:
        if essaie == 1:
          rt1 = list(choix_joueur_sous_condition)
          rt1[3] = "*"
          t1 = ''.join(rt1)
          choix_joueur_sous_condition = t1
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 2:
          rt2 = list(choix_joueur_sous_condition)
          rt2[3] = "*"
          t2 = ''.join(rt2)
          choix_joueur_sous_condition = t2
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 3:
          rt3 = list(choix_joueur_sous_condition)
          rt3[3] = "*"
          t3 = ''.join(rt3)
          choix_joueur_sous_condition = t3
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 4:
          rt4 = list(choix_joueur_sous_condition)
          rt4[3] = "*"
          t4 = ''.join(rt4)
          choix_joueur_sous_condition = t4
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 5:
          rt5 = list(choix_joueur_sous_condition)
          rt5[3] = "*"
          t5 = ''.join(rt5)
          choix_joueur_sous_condition = t5
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 6:
          rt6 = list(choix_joueur_sous_condition)
          rt6[3] = "*"
          t6 = ''.join(rt6)
          choix_joueur_sous_condition = t6
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        if essaie == 7:
          rt7 = list(choix_joueur_sous_condition)
          rt7[3] = "*"
          t7 = ''.join(rt7)
          choix_joueur_sous_condition = t7
          verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
          
def verif_lettre5(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7):
    if choix_joueur_sous_condition[4] == lettre5:
      ar5 = lettre5.upper()
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition) 
        rt1[4] = lettre5.upper()
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition) 
        rt2[4] = lettre5.upper()
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[4] = lettre5.upper()
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition) 
        rt4[4] = lettre5.upper()
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition) 
        rt5[4] = lettre5.upper()
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition) 
        rt6[4] = lettre5.upper()
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition) 
        rt7[4] = lettre5.upper()
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    elif choix_joueur_sous_condition[4] in mot_random:
      ar5 = choix_joueur_sous_condition[4]
      if essaie == 1:
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7) 
      if essaie == 7:
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    else:
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition)
        rt1[4] = "*"
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition)
        rt2[4] = "*"
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[4] = "*"
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition)
        rt4[4] = "*"
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition)
        rt5[4] = "*"
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition)
        rt6[4] = "*"
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition)
        rt7[4] = "*"
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        
def verif_lettre6(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7):
    if choix_joueur_sous_condition[5] == lettre6:
      ar6 = lettre6.upper()
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition) 
        rt1[5] = lettre6.upper()
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition) 
        rt2[5] = lettre6.upper()
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[5] = lettre6.upper()
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition) 
        rt4[5] = lettre6.upper()
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition) 
        rt5[5] = lettre6.upper()
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition) 
        rt6[5] = lettre6.upper()
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition) 
        rt7[5] = lettre6.upper()
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        
    elif choix_joueur_sous_condition[5] in mot_random:
      ar6 = choix_joueur_sous_condition[5]
      if essaie == 1:
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
       verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    else:
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition) 
        rt1[5] = "*"
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition)
        rt2[5] = "*"
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[5] = "*"
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition)
        rt4[5] = "*"
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition)
        rt5[5] = "*"
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition)
        rt6[5] = "*"
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition)
        rt7[5] = "*"
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
        
    
def verif_lettre7(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7):  
    if choix_joueur_sous_condition[6] == lettre7:
      ar7 = lettre7.upper()
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition) 
        rt1[6] = lettre7.upper()
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition) 
        rt2[6] = lettre7.upper()
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[6] = lettre7.upper()
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition) 
        rt4[6] = lettre7.upper()
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition) 
        rt5[6] = lettre7.upper()
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition) 
        rt6[6] = lettre7.upper()
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition) 
        rt7[6] = lettre7.upper()
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
  
    elif choix_joueur_sous_condition[6] in mot_random:
      ar7 = choix_joueur_sous_condition[6]
      if essaie == 1:
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
    else:
      if essaie == 1:
        rt1 = list(choix_joueur_sous_condition) 
        rt1[6] = "*"
        t1 = ''.join(rt1)
        choix_joueur_sous_condition = t1
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 2:
        rt2 = list(choix_joueur_sous_condition) 
        rt2[6] = "*"
        t2 = ''.join(rt2)
        choix_joueur_sous_condition = t2
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 3:
        rt3 = list(choix_joueur_sous_condition)
        rt3[6] = "*"
        t3 = ''.join(rt3)
        choix_joueur_sous_condition = t3
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 4:
        rt4 = list(choix_joueur_sous_condition) 
        rt4[6] = "*"
        t4 = ''.join(rt4)
        choix_joueur_sous_condition = t4
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 5:
        rt5 = list(choix_joueur_sous_condition) 
        rt5[6] = "*"
        t5 = ''.join(rt5)
        choix_joueur_sous_condition = t5
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 6:
        rt6 = list(choix_joueur_sous_condition) 
        rt6[6] = "*"
        t6 = ''.join(rt6)
        choix_joueur_sous_condition = t6
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)
      if essaie == 7:
        rt7 = list(choix_joueur_sous_condition) 
        rt7[6] = "*"
        t7 = ''.join(rt7)
        choix_joueur_sous_condition = t7
        jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7)


######################################################################################################""


"""

Phase 3 : le jeux


"""
# création du jeu de motus

def jeux(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,ar1,ar2,ar3,ar4,ar5,ar6,ar7):

  # on clear le CLI a chaque affichage
  print("\033[H\033[J", end="")

  # t = " tentative"
  
  if essaie ==1:
    qt1,qt1f = couleurs.VERT, couleurs.RESET
    qt2,qt3,qt4,qt5,qt6,qt7,qt2f,qt3f,qt4f,qt5f,qt6f,qt7f = couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.RESET,couleurs.RESET, couleurs.RESET,couleurs.RESET,couleurs.RESET,couleurs.RESET
  if essaie ==2:
    qt1,qt1f = couleurs.GRIS, couleurs.RESET
    qt2, qt2f = couleurs.VERT, couleurs.RESET
    qt3,qt4,qt5,qt6,qt7,qt3f,qt4f,qt5f,qt6f,qt7f = couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.RESET,couleurs.RESET, couleurs.RESET,couleurs.RESET,couleurs.RESET
  if essaie ==3:
    qt1,qt2,qt1f,qt2f = couleurs.GRIS,couleurs.GRIS,couleurs.RESET,couleurs.RESET
    qt3,qt3f = couleurs.VERT, couleurs.RESET
    qt4,qt5,qt6,qt7,qt4f,qt5f,qt6f,qt7f = couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.RESET,couleurs.RESET, couleurs.RESET,couleurs.RESET
  if essaie == 4:
    qt1,qt2,qt3, qt1f,qt2f,qt3f = couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.RESET,couleurs.RESET,couleurs.RESET
    qt4,qt4f = couleurs.VERT, couleurs.RESET
    qt5,qt6,qt7,qt5f,qt6f,qt7f = couleurs.GRIS,couleurs.GRIS,couleurs.GRIS, couleurs.RESET,couleurs.RESET,couleurs.RESET
  if essaie == 5:
    qt1,qt2,qt3,qt4,qt1f,qt2f,qt3f,qt4f = couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.RESET,couleurs.RESET,couleurs.RESET,couleurs.RESET
    qt5,qt5f = couleurs.VERT, couleurs.RESET
    qt6,qt7,qt6f,qt7f = couleurs.GRIS,couleurs.GRIS, couleurs.RESET, couleurs.RESET
  if essaie == 6:
    qt1,qt2,qt3,qt4,qt5,qt1f,qt2f,qt3f,qt4f,qt5f = couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.RESET,couleurs.RESET,couleurs.RESET,couleurs.RESET,couleurs.RESET
    qt6,qt6f = couleurs.VERT, couleurs.RESET
    qt7,qt7f = couleurs.GRIS, couleurs.RESET
  if essaie == 7:
    qt7,qt7f = couleurs.VERT, couleurs.RESET
    qt2,qt3,qt4,qt5,qt6,qt1,qt2f,qt3f,qt4f,qt5f,qt6f,qt1f = couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.GRIS,couleurs.RESET,couleurs.RESET, couleurs.RESET,couleurs.RESET,couleurs.RESET,couleurs.RESET
    

    
  print(f"""
  {couleurs.VERT}                 _             
        /\/\   ___ | |_ _   _ ___ 
       /    \ / _ \| __| | | / __|
      / /\/\ \ (_) | |_| |_| \___\
      
      \/    \/\___/ \__|\__,_|___/ {couleurs.RESET}
                            
         
        |       |       |       |       |       |       |       |
        |   {ar1}   |   {ar2}   |   {ar3}   |   {ar4}   |   {ar5}   |   {ar6}   |   {ar7}   |
        |       |       |       |       |       |       |       |


        {couleurs.GRAS} Choix joueur {couleurs.RESET}: {choix_mot}
        {qt1} Tentative 1 {qt1f}: {t1} 
        {qt2} Tentative 2 {qt2f}: {t2} 
        {qt3} Tentative 3 {qt3f}: {t3} 
        {qt4} Tentative 4 {qt4f}: {t4} 
        {qt5} Tentative 5 {qt5f}: {t5} 
        {qt6} Tentative 6 {qt6f}: {t6} 
        {qt7} Tentative 7 {qt7f}: {t7} 
        
  """)

  essaie += 1
  choix_joueur(essaie,t1,t2,t3,t4,t5,t6,t7)


# on utilise unidecode pour enlever les accents du mot 
  
def choix_joueur(essaie,t1,t2,t3,t4,t5,t6,t7):
  print(mot_random)
  print(f"Le mot commence par un {mot_random[0].upper()}")
  choix_mot = input(couleurs.SOULIGNER + "\n\nEntrez le mot que vous voulez tenter " + couleurs.RESET + ": ")
  if essaie == 7:
    print("\033[H\033[J", end="")
    print(f"""
    C'est perdu ! Nombre d'essaie max atteint !
    
    {couleurs.GRAS}Le mot était :{couleurs.RESET}""")
    print(f"""
               {lettre1.upper()}    {lettre2.upper()}    {lettre3.upper()}    {lettre4.upper()}    {lettre5.upper()}    {lettre6.upper()}    {lettre7.upper()}
              ___  ___  ___  ___  ___  ___  ___
    """)
  else:
    if len(choix_mot) > 7 or len(choix_mot) < 7:
      print("\nLe mot doit contenir 7 lettres")
      choix_joueur(essaie,t1, t2,t3,t4,t5,t6,t7)
    else:
      choix_joueur_sous_condition = ud.unidecode(choix_mot).lower()
      if choix_joueur_sous_condition == mot_random:
        print("\033[H\033[J", end="")
        print("Félicitation vous avez trouver le mot !")
        print(f"""
               {lettre1.upper()}    {lettre2.upper()}    {lettre3.upper()}    {lettre4.upper()}    {lettre5.upper()}    {lettre6.upper()}    {lettre7.upper()}
              ___  ___  ___  ___  ___  ___  ___
    """)
      else:
        verif_lettre1(choix_mot,choix_joueur_sous_condition,essaie,t1,t2,t3,t4,t5,t6,t7,lettre1.upper(),"_","_","_","_","_","_")




choix_joueur(1,"       ", "       ", "       ","       ","       ","       ","       ")

 # ar = " a remplacer "
"""
  ar1 = lettre1
  ar2 = "_"
  ar3 = "_"
  ar4 = "_"
  ar5 = "_"
  ar6 = "_"
  ar7 = "_"
"""