"""
Verifier si une ville est au nord, au centre ou au sud de la Tunisie

Exemple de villes:
Tunis, Bizerte, Ariana (Nord)
Sfax, Kairouan, Sousse (Centre)
Gabès, Medenine, Tataouine (Sud)
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

