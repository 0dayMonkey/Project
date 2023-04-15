# tentatives aléatoires pour redeem un jeu mc

import requests
import time

voucher_codes_file = "voucher_codes.txt"

# https://kqzz.github.io/mc-bearer-token/
access_token = "-"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

api_url = "https://api.minecraftservices.com/productvoucher"

def redeem_voucher(code):
    try:
        code = code[:10]+"**********"
        response = requests.put(f"{api_url}/{code}", headers=headers)

        if response.status_code == 200:
            print(f"Le code {code} a été validé avec succès.")
        elif response.status_code == 403:
            print(f"Accès non autorisé. Vérifiez votre token d'authentification.")
        elif response.status_code == 404:
            print(f"Le code {code} est invalide.")
        else:
            print(f"Erreur inattendue pour le code {code} (code d'erreur: {response.status_code}).")
    except Exception as e:
        print(f"Exception lors du traitement du code {code}: {e}")

# prise en charge avec le fichier de voucher_codes_file
with open(voucher_codes_file, "r") as f:
    voucher_codes = [line.strip() for line in f]

pause_duration = 3

for i, code in enumerate(voucher_codes):
    print(f"Traitement du code {i + 1} sur {len(voucher_codes)}")
    redeem_voucher(code)
    time.sleep(pause_duration)
