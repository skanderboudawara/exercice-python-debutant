"""
Jeu : Devinez le plat tunisien

L'ordinateur sélectionne aléatoirement un plat typique tunisien parmi une liste.
Votre objectif est de deviner le nom du plat choisi.
À chaque tentative, le programme vous indique si votre réponse est correcte ou non, jusqu'à ce que vous trouviez la bonne réponse.
Bonne chance !
"""
import random

PLATS_TUNISIENS = [
    "Couscous",
    "Brik",
    "Lablabi",
    "Mechouia",
    "Tagine"
]


plat_choisi = random.choice(PLATS_TUNISIENS)
print("Devinez le plat tunisien choisi par l'ordinateur.")
print("Options: " + ", ".join(PLATS_TUNISIENS))
while True:
    reponse = input("Entrez le nom du plat: ").strip()
    if reponse == plat_choisi:
        print(f"Bravo! Vous avez deviné le plat: {plat_choisi}.")
        break
    else:
        print("Ce n'est pas le bon plat. Essayez encore.")