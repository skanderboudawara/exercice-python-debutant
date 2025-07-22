"""
Deviner un plat tunisien

L'ordinateur choisit un plat tunisien, et l'utilisateur doit deviner le nom du plat.
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