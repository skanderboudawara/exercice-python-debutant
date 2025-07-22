"""
Verifier si un numero CIN Tunisien est valide

CIN Validation:
- Composé de 8 chiffres.
- Le premier chiffre doit être compris entre 0 et 1
- Le CIN doit être que des chiffres
"""

def is_cin_valid(cin):
    # Verifier la longueur du CIN et les conditions spécifiques
    if len(cin) != 8:
        return False
    # Verifier le premier chiffre et si tous les caractères sont des chiffres
    if cin[0] not in ['0', '1']:
        return False 
    # Verifier si tous les caractères sont des chiffres 
    if not cin.isdigit():
        return False
    return True

while True:
    cin = input("Entrez le numéro de CIN à vérifier: ").strip()
    
    if is_cin_valid(cin):
        print(f"Le numéro de CIN {cin} est valide.")
    else:
        print(f"Le numéro de CIN {cin} n'est pas valide.")
    
    continuer = input("Voulez-vous vérifier un autre CIN ? (oui/non): ").strip().lower()
    if continuer != 'oui':
        break