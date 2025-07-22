"""
Calculatrice de Zakat - Exercice

Ecrire un programme qui calcule la Zakat à partir d'un montant donné.
La zakat est calculée comme suit:
- Si le montant depasse le Nissab (8400 TND), la Zakat est de 2.5% du montant.
"""

def calculer_zakat(montant):
    NISSAB = 8400  # Nissab en TND
    if montant < NISSAB:
        return 0.0
    else:
        return montant * 0.025  # 2.5%
    
    
while True:
    try:
        montant = float(input("Entrez le montant pour calculer la Zakat: "))
        zakat = calculer_zakat(montant)
        if zakat > 0:
            print(f"La Zakat à payer sur {montant:.2f} TND est de {zakat:.2f} TND.")
        else:
            print("Le montant est inférieur au Nissab, aucune Zakat n'est due.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre valide.")

    continuer = input("Voulez-vous calculer la Zakat pour un autre montant? (oui/non): ")
    if continuer.lower() != "oui":
        break
