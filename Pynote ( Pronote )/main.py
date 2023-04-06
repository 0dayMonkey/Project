# ======================= PRONOTE ========================
def pynote():
  choix = input("""
    Bienvenue sur Pynote !
    Selectionnez le profil auquel vous souhaitez vous connecter :
    
    1) Prof
    2) Eleve 
  
    Choix : """)
  if choix == "1" or choix == "Prof" or choix == "prof":
    nouvelle_page()
    prof()
  if choix == "2" or choix == "Eleve" or choix == "eleve":  # On part du principe que l'éléve fait partie de la T°B
    nouvelle_page()
    eleve()
  if choix != "1" or choix != "2":
    mauvais_choix()
    nouvelle_page()
    pynote()
# ======================= PROFILES ========================
def prof():
  choix_prof = input("""
    Choisissez parmis les options suivantes ce que vous souhaitez faire :\n
      
      A) Afficher la liste des classes
      B) Revenir en arrière
      \nChoix : """)
  a_b = ["a", "A", "b", "B"]
  if choix_prof == "A" or choix_prof == "a":
    nouvelle_page()
    liste_des_classes()
      
  
  if choix_prof == "B" or choix_prof == "b":
    nouvelle_page()
    pynote()
  if choix_prof not in a_b:
    mauvais_choix()
    prof()


def eleve():
  choix_eleve = input(""" 
      Choisissez parmis les options suivantes ce que vous souhaitez faire :
      
      A) Liste des élèves de ma classe 
      B) Liste de mes spécialités
      C) Liste de mes notes
      D) Liste de mes apréciations 
      E) Voir mes informations
      F) Revenir en arriere 
      
      Choix : """)


# ================== Liste CLASSES ====================
def liste_des_classes():
  print("Liste des classes :\n")
  if len(classroom.liste_classe) == 0:
    print("Aucune classe configurée pour l'instant")
  else:
    for i in range(len(classroom.liste_classe)):
        print( "-", classroom.liste_classe[i])
  
  choix_action_classe = input("""
  Choisissez parmis les options suivante ce que vous souhaitez faire :\n
          1) Gerer une classe
          2) Ajouter une classe
          3) Supprimer une classe
          4) Revenir en arrière

          Choix : """)
  if choix_action_classe == "1":
    if len(classroom.liste_classe) == 0:
      print("\nIl n'y a aucune clase à gerer, créez en une avant")
      mauvais_choix()
      nouvelle_page()
      liste_des_classes()
    elif len(classroom.liste_classe) != 0:
      nouvelle_page()
      gestion_classe()
  if choix_action_classe == "2":
    nom_classe = input("Entrez le nom de la classe que vous souhaitez ajouter : ")
    if nom_classe in classroom.liste_classe:
      input("\n Impossible d'utiliser ce nom car la classe existe déjà.\n\n")
      mauvais_choix()
      nouvelle_page()
      liste_des_classes()
    else:
      classroom.liste_classe.append(str(nom_classe))
      print('\nLa classe "' + nom_classe + '" a bien été ajoutée !')
      pause()
      nouvelle_page()
      liste_des_classes()
  if choix_action_classe == "3":
    print("Quelle classe souhaitez vous supprimer ( entrez le chiffre correspondant ) ?")
    for i in range(len(classroom.liste_classe)):
      print(i + 1, ")", classroom.liste_classe[i])
    delete_classe = input("\nChoix : ")
    classe_suppr = classroom.liste_classe[int(delete_classe)-1]
    classroom.liste_classe.pop(int(delete_classe)-1)
    print('\n La classe "' + classe_suppr  + '" a bien été supprimé')
    pause() + liste_des_classes()
  if choix_action_classe == "4":
    nouvelle_page()
    prof()
  else: 
    mauvais_choix()
    nouvelle_page()
    liste_des_classes()

# =============== Gestion  CLASSES ====================
def gestion_classe():
  print("Quelle classe souhaitez vous gerer ( entrez le chiffre correspondant ) ?\n")
  for i in range(len(classroom.liste_classe)):
    print(i + 1, ")", classroom.liste_classe[i])
  classe_gerer = input("\n Choix : ")
  nouvelle_page()
  
  global nom_classe_gerer
  nom_classe_gerer = classroom.liste_classe[int(classe_gerer)-1]

  global choix_gestion_classe
  choix_gestion_classe = f"""
  _____________________________
                               
   Classe séléctionnée : {nom_classe_gerer}     
  _____________________________"""
  print(choix_gestion_classe)
  choix_gestion_classe_action = input("""
  Choisissez l'action que vous souhaitez effectuer :
  
  1) Liste des eleves
  2) Liste des meilleurs eleves
  3) Moyenne de la classe
  4) Modifier le nom de la classe
  5) Modifier l'effectif maximum 
  6) Revenir en arriere

  Choix : """)
  nouvelle_page()
  print(choix_gestion_classe,"\n")
  
  if choix_gestion_classe_action == "1":
    nouvelle_page()
    gestion_eleve()
      
  if choix_gestion_classe_action == "2":
    gestion_classe()
  if choix_gestion_classe_action == "3":
    gestion_classe()
  if choix_gestion_classe_action == "4":
    gestion_classe()
  if choix_gestion_classe_action == "5":
    gestion_classe()
  if choix_gestion_classe_action == "6":
    gestion_classe()

# ================== Gestion ELEVES ===================

def gestion_eleve():
  print(choix_gestion_classe,"\n")
  print("Quel eleves souhaitez vous gerer :\n")
  for i in range(len(classroom.liste_eleve)):
      print(i + 1, ")", classroom.liste_eleve[i])
  choix_gestion_eleve_liste = input("""
  Choix : """)
  """
  input(  
    Choisissez l'action que vous souhaitez effectuer :
  
  1) Ajouter un eleve
  2) Supprimer un eleve
  3) Moyenne de la classe
  4) Modifier le nom de la classe
  5) Modifier l'effectif maximum 
  6) Revenir en arriere

  Choix : )
    """
    
# ================== Fonction ANNEXES ==================
def pause():
  input("\nAppuyez sur la touche ENTRER pour revenir au menu...\n\n")

def mauvais_choix():
  input("\nChoix incorrect, appuyez sur la touche ENTRER pour revenir au menu...\n\n")

def nouvelle_page():
  print("\033[H\033[J", end="")
    

# ======================= Class ========================


class Classe:

  def __init__(self, nom, liste_eleve, liste_classe, effectif_max):
    self.nom = nom
    self.liste_classe = liste_classe
    self.liste_eleve = liste_eleve
    self.effemax = effectif_max

  def ajout_eleve(self):
    if len(self.liste_eleve) == self.effemax:
      print("Impossible d'ajouter plus d'élèves, supprimez en avant")
    else:
      nom = input("Inserez le nom de l'élève : ")
      prenom = input("Inserez le prénom de l'élève : ")
      Elevex(nom, prenom, [], [])
      self.liste_eleve.append(prenom)
      encore = input(""" Voulez vous en ajouter encore ?
      1) Oui
      2) Non
      """)
      if encore == "Non" or encore == "2" or encore == "non":
        pynote()
      elif encore == "Oui" or encore == 1 or encore == "oui":
        etudiant.ajout_eleve()


class Elevex:
  " Ici on peux mettre une definition d'une classe"

  def __init__(self, nom, prenom, note, specialité):
    """"Methode d'initialisation avec les parametres"""
    self.nom = nom
    self.prenom = prenom
    self.note_nsi = note
    self.spé = specialité

  def ajout_note(self, l):
    if type(l) == list:
      for i in l:
        self.note_nsi.append(i)
    else:
      self.note_nsi.append(l)

  def ajout_spé(self, l):
    if type(l) == list:
      for i in l:
        self.spé.append(i)
    else:
      self.spé.append(str(l))

  def moyenne(self):
    self.moyenne = 0
    for i in self.note_nsi:
      self.moyenne += i
    self.moyenne /= len(self.note_nsi)
    self.moyenne = round(self.moyenne, 2)
    print((self.moyenne))

  def __str__(self):
    print("\n Le nom est l'élève est : " + self.nom +
          "\n Le prénom de l'élève est : " + self.prenom +
          "\n La moyenne de l'éleve est : " + str(self.moyenne))


# ======================= Lancement ========================

ajout = [14, 15, 16]
ajoutspé = ["Math", "Français"]
liste = [10, 12, 13]
spé = []
eleves = ["Maelle", "Théo", "Alex", "Simeon"]
classes = ["Tb","Tc","Te"]
# classes = [["Maelle", "Théo", "Alex", "Simeon"], ["Max", "Adam", "Remi", "Anaïs"], ["AlexandreB", "Alexandre L", "Benji", "Paul"]]

eleves = Elevex("Hatchi", "Madrid", liste, spé)
classroom = Classe("", eleves, classes, 8)

pynote()
