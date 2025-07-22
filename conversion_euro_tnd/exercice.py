"""
Exercice: Conversion du dinar Tunisien (TND) en euro (EUR) et vice versa

Objet: écrire un programme qui convertit une somme en dinars tunisiens (TND) en euros (EUR).
Taux de conversion: 1 EUR = 3.41 TND.
"""

def convertir_tnd_en_eur(montant_tnd):
    taux_conversion = 3.41
    montant_eur = montant_tnd / taux_conversion
    return montant_eur

def convertir_eur_en_tnd(montant_eur):
    taux_conversion = 3.41
    montant_tnd = montant_eur * taux_conversion
    return montant_tnd

def check_user_input():
    try:
        montant = float(input("Entrez le montant à convertir: "))
        choix = input("Convertir en (1) EUR ou (2) TND ? (entrez 1 ou 2): ").strip()
        
        if choix == '1':
            montant_eur = convertir_tnd_en_eur(montant)
            print(f"{montant} TND équivaut à {montant_eur:.2f} EUR.")
        elif choix == '2':
            montant_tnd = convertir_eur_en_tnd(montant)
            print(f"{montant} EUR équivaut à {montant_tnd:.2f} TND.")
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")


while True:
    check_user_input()
    continuer = input("Voulez-vous convertir un autre montant ? (oui/non): ").strip().lower()
    if continuer != 'oui':
        breakS