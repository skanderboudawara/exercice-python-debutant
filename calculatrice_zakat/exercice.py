"""
Calculatrice de Zakat - Exercice

Écrivez un programme qui demande à l'utilisateur un montant en dinars tunisiens (TND) et calcule la Zakat à payer selon les règles suivantes :
- Si le montant est inférieur au Nissab (8400 TND), aucune Zakat n'est due.
- Si le montant est supérieur ou égal au Nissab, la Zakat à payer est égale à 2,5% du montant.
Le programme doit permettre à l'utilisateur de faire plusieurs calculs successifs.
"""
NISSAB = 8400 

def calculer_zakat_method1(montant):
    if montant < NISSAB:
        return 0.0
    else:
        return montant * 0.025  # 2.5%

def calculer_zakat_method2(montant):
    if montant < NISSAB:
        return 0.0
    return montant * 0.025  # 2.5%

def calculer_zakat_methode3(montant):
    return 0.0 if montant < NISSAB else montant * 0.025 
    
while True:
    try:
        montant = float(input("Entrez le montant pour calculer la Zakat: "))
        zakat = calculer_zakat_method1(montant)
        if zakat > 0:
            print(f"La Zakat à payer sur {montant:.2f} TND est de {zakat:.2f} TND.")
        else:
            print("Le montant est inférieur au Nissab, aucune Zakat n'est due.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre valide.")

    continuer = input("Voulez-vous calculer la Zakat pour un autre montant? (oui/non): ")
    if continuer.lower() != "oui":
        break
