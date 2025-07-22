"""

Programme de fidélité - Exercice

Un café est offert pour chaque 10 cafés achetés.
"""

def calculer_cafes_offerts(cafes_achetes):
    return cafes_achetes // 10

def check_user_input():
    try:
        cafes_achetes = int(input("Entrez le nombre de cafés achetés: "))
        if cafes_achetes < 0:
            print("Le nombre de cafés achetés ne peut pas être négatif.")
            return
        
        cafes_offerts = calculer_cafes_offerts(cafes_achetes)
        print(f"Vous avez droit à {cafes_offerts} café(s) offert(s).")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entier.")
        
while True:
    check_user_input()
    continuer = input("Voulez-vous vérifier un autre nombre de cafés achetés ? (oui/non): ").strip().lower()
    if continuer != 'oui':
        break
