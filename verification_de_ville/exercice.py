"""
Écrire un programme qui permet à l'utilisateur de vérifier dans quelle région de la Tunisie se trouve une ville donnée.

Les régions et leurs villes sont les suivantes :
- Nord : Tunis, Bizerte, Ariana
- Centre : Sfax, Kairouan, Sousse
- Sud : Gabès, Medenine, Tataouine

Le programme doit demander à l'utilisateur le nom d'une ville, indiquer sa région ou préciser si la ville n'est pas reconnue, puis proposer de vérifier une autre ville.
"""

# Methode 1

DICTIONNAIRE_DES_REGIONS = {
    "Nord": ["Tunis", "Bizerte", "Ariana"],
    "Centre": ["Sfax", "Kairouan", "Sousse"],
    "Sud": ["Gabès", "Medenine", "Tataouine"]
}

def verifier_region_ville(ville):
    for region, villes in DICTIONNAIRE_DES_REGIONS.items():
        if ville in villes:
            return region
    return "Inconnue"

while True:
    ville = input("Entrez le nom de la ville à vérifier: ").strip()
    
    region = verifier_region_ville(ville)
    
    if region != "Inconnue":
        print(f"La ville {ville} est située dans la région {region}.")
    else:
        print(f"La ville {ville} n'est pas reconnue.")
    
    continuer = input("Voulez-vous vérifier une autre ville ? (oui/non): ").strip().lower()
    if continuer != 'oui':
        break
    
# Methode 2
def verifier_region_ville_methode2(ville):
    if ville in DICTIONNAIRE_DES_REGIONS["Nord"]:
        return "Nord"
    elif ville in DICTIONNAIRE_DES_REGIONS["Centre"]:
        return "Centre"
    elif ville in DICTIONNAIRE_DES_REGIONS["Sud"]:
        return "Sud"
    return "Inconnue"

