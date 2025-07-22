"""
Programme de fidélité - Exercice

Pour chaque multiplicité de 10 cafés achetés, le client reçoit un café offert.
"""

def is_multiplicite_de_dix(cafes_achetes):
    return cafes_achetes % 10 == 0


while True:
    try:
        cafes_achetes = int(input("Entrez le nombre de cafés achetés: "))
        if cafes_achetes < 0:
            print("Veuillez entrer un nombre positif.")
            continue
        
        if is_multiplicite_de_dix(cafes_achetes):
            print(f"Félicitations! Vous avez droit à un café offert pour vos {cafes_achetes} cafés achetés.")
        else:
            print(f"Vous avez acheté {cafes_achetes} cafés, mais vous n'avez pas droit à de café offert.")
        
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entier.")
    
    continuer = input("Voulez-vous vérifier un autre nombre de cafés? (oui/non): ")
    if continuer.lower() != "oui":
        break
