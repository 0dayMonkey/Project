import sys
from ppadb.client import Client
import time
import cv2
import numpy as np

def connect_device():
    '''
    Je vérifie si un téléphone est connecté, si non je le précise à l'utilisateur, si oui alors je continue
    simplement en renvoyant l'objet Client.
    :return:
    '''
    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()
    if len(devices) == 0:
        print("Aucun téléphone n'est connecté : veuillez en connecter un")
        return False
    return devices[0]


def detect_bonus():
    # Charger l'image de référence
    template = cv2.imread('C:/Users/2vl/Desktop/Ride/bonus_template.jpg')

    # Convertir l'image de référence en niveaux de gris
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Appliquer un filtre de flou à l'image de référence
    template_gray = cv2.GaussianBlur(template_gray, (5, 5), 0)

    # Capturez l'image de l'écran du téléphone
    image_data = device.screencap()
    # Convertissez l'objet bytearray en un objet bytes
    image_data = bytes(image_data)
    # Décodez l'image
    image = cv2.imdecode(np.fromstring(image_data, dtype=np.uint8), cv2.IMREAD_COLOR)
    # Récupérez la taille de l'image
    height, width, _ = image.shape
    # Redimensionnez l'image en cas de besoin
    image = cv2.resize(image, (int(width * 0.5), int(height * 0.5)))
    # Enregistrez l'image dans un fichier
    cv2.imwrite('screenshot.jpg', image)
    # Initialisez la variable game_image_paths avec le chemin d'accès du fichier image
    game_image_paths = ['screenshot.jpg']

    # Bouclez sur chaque image du jeu à traiter
    for game_image_path in game_image_paths:
        # Charger l'image en cours de traitement
        game_image = cv2.imread(game_image_path)

        # Convertir l'image en cours de traitement en niveaux de gris
        game_image_gray = cv2.cvtColor(game_image, cv2.COLOR_BGR2GRAY)

        # Appliquer un filtre de flou à l'image en cours de traitement
        game_image_gray = cv2.GaussianBlur(game_image_gray, (5, 5), 0)

        # Appliquer l'appariement de modèle
        result = cv2.matchTemplate(game_image_gray, template_gray, cv2.TM_CCOEFF_NORMED)

        # Trouvez l'emplacement qui correspond le mieux à l'image de référence
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # Si le niveau de correspondance est supérieur à un seuil défini, dessinez un rectangle autour de l'emplacement correspondant
        if max_val > 0.8:
            top_left = max_loc
            bottom_right = (top_left[0] + template.shape[0], top_left[1] + template.shape[1])
            cv2.rectangle(game_image, top_left, bottom_right, (0, 0, 255), 2)
            cv2.imshow('Detected Bonus', game_image)
            cv2.waitKey(0)
        else:
            print("Aucun bonus détecté dans l'image {}".format(game_image_path))


# Établissez une connection avec votre téléphone via ADB
adb = Client(host='127.0.0.1', port=5037)
device = connect_device()
detect_bonus()