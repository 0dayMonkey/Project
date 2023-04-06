import random, math, itertools
import pandas as pd


def generation(n=8):
    # Génère les coordonnées aléatoires pour les 8 villes
    coordinates = []
    for i in range(8):
        x = random.randint(0, 49)
        y = random.randint(0, 19)
        coordinates.append([x, y])
    return coordinates


def display_map(coordinates):
    # Nettoie la console à chaque nouvelle affichage (pour une meilleure lisibilité)
    print("\033[H\033[3J", end="")
    
    # Crée une carte de 50 de largeur et 22 de hauteur remplie d'espaces
    map = [[' ' for x in range(50)] for y in range(22)]

    # Positionne les points sur la carte en utilisant les coordonnées
    for x, y in coordinates:
        map[y][x] = 'X'

    # Crée les bords de la carte
    map[0] = ['-'] * 50
    map[21] = ['-'] * 50
    for i in range(22):
        map[i][0] = '|'
        map[i][49] = '|'

    # Affiche la carte
    for liste in map:
        print(''.join(liste))


def distance(A, B):
    # Calcule la distance entre A et B
    x1, y1 = A
    x2, y2 = B
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d


# Génère la matrice 8x8 des distances
distances = [[0 for x in range(8)] for y in range(8)]
for i in range(8):
    for j in range(8):
        if i != j:
            distances[i][j] = distance(generation()[i], generation()[j])
            distances[j][i] = distances[i][j]

# La distance d'une ville vers elle-même est 0, on met ça à zéro pour chacune des coordonnées
for i in range(8):
    distances[i][i] = 0

# Calcul de la distance jusqu'au point d'origine de la matrice de base
dist_origine = distance((0, 0), generation()[0])

# Liste des chemins possibles
chemins_possibles = []
villes_ = [i for i in range(1, 9)]

# Obtient toutes les permutations possibles des villes
chemins = list(itertools.permutations(villes_))

# Initialise les variables pour stocker le chemin le plus court et sa distance
chemin_p_court = None
distance_p_court = float('inf')

# Parcourt tous les chemins possibles et calcule leur distance totale
for chem in chemins:
    total_distance = dist_origine
    for i in range(len(chem)-1):
        total_distance += distances[chem[i]-1][chem[i+1]-1]

    # Met à jour le chemin le plus court si nécessaire
    if total_distance < distance_p_court:
        distance_p_court = total_distance
        chemin_p_court = chem

# Programme principal
if __name__ == '__main__':
    display_map(generation())
    print("\n Distance avec le point d'origine:", round(dist_origine, 3))

    # Crée une liste avec les noms des villes
    villes = ['Ville ' + str(i+ 1) for i in range(8)]
# Crée un tableau (dataframe de pandas) avec les villes et distances
df = pd.DataFrame(distances, columns=villes, index=villes)
print("\n", df)

"""
Pour afficher tous les chemins possibles, retirer les "#" devant la ligne suivante.
Attention, il y a vraiment beaucoup de chemins. Il faut d'abord augmenter le nombre
d'itérations maximales, sinon l'affichage s'arrêtera.
"""
#for i in chemins:
#  chemins_possibles.append(i)
#  print(i)

# Affiche le chemin le plus court
print("\nLe chemin le plus court est : ", chemin_p_court)
print("Avec une distance totale de :", round(distance_p_court, 3))
