from colorama import Fore
n = 9
positions = [" "]*9

for i in range(9):
    exec(f"pos{i+1} = positions[{i}]")

grille = f"""

            {pos1}  |  {pos2}  |  {pos3}    
           ────────────────
            {pos1}  |  {pos2}  |  {pos3}
           ────────────────
            {pos1}  |  {pos2}  |  {pos3}

"""
print(grille)

joueurs = []

def init():
  j1 = input("Pseudo du joueur numéro 1 : ")
  j2 = input("Pseudo du second joueur : ")
  joueurs.append(j1) and joueurs.append(j2)

def logo():
  print(Fore.LIGHTBLUE_EX + """
                                                                    
                                                                  
█▀▄▀█ ████▄ █▄▄▄▄ █ ▄▄  ▄█ ████▄    ▄   
█ █ █ █   █ █  ▄▀ █   █ ██ █   █     █  
█ ▄ █ █   █ █▀▀▌  █▀▀▀  ██ █   █ ██   █ 
█   █ ▀████ █  █  █     ▐█ ▀████ █ █  █ 
   █          █    █     ▐       █  █ █ 
  ▀          ▀      ▀            █   ██ 
                                        

                          


  
  """)