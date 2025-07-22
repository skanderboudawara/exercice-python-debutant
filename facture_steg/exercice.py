"""
Calcul de facture de STEG

< 100 KWh: 0.18 TND par KWh
100-200 KWh: 0.23 TND par KWh
> 200 KWh: 0.28 TND par KWh
"""

def calculer_facture_steg(kwh):
    if kwh < 100:
        return kwh * 0.18
    elif kwh <= 200:
        return (100 * 0.18) + ((kwh - 100) * 0.23)
    else:
        return (100 * 0.18) + (100 * 0.23) + ((kwh - 200) * 0.28)

while True:
    try:
        kwh = float(input("Entrez la consommation en KWh: "))
        if kwh < 0:
            print("Veuillez entrer une valeur positive.")
            continue
        facture = calculer_facture_steg(kwh)
        print(f"La facture STEG pour {kwh} KWh est de {facture:.2f} TND.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")
