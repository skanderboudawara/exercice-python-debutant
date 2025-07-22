""""
Liste des invités pour un mariage

L'utilisateur ajoute des invités des noms un par un et quand il tape "stop", le programme affiche:

Le nombre d'invités
et la liste des invités triée par ordre alphabétique.
le nom le plus long
"""

def ajouter_invites():
    invites = []
    
    while True:
        invite = input("Entrez le nom de l'invité (ou tapez 'stop' pour terminer): ").strip()
        if invite.lower() == 'stop':
            break
        if invite:  # Vérifier que le nom n'est pas vide
            invites.append(invite)
    
    return invites

def calculer_informations_invites(invites):
    if not invites:
        return 0, [], ""
    
    invites_triees = sorted(invites)
    nombre_invites = len(invites_triees)
    nom_le_plus_long = max(invites_triees, key=len)
    
    return nombre_invites, invites_triees, nom_le_plus_long

if __name__ == "__main__":
    invites = ajouter_invites()
    nombre_invites, invites_triees, nom_le_plus_long = calculer_informations_invites(invites)
    
    print(f"Nombre d'invités: {nombre_invites}")
    if invites_triees:
        print("Liste des invités (triée par ordre alphabétique):")
        for invite in invites_triees:
            print(invite)
    
    if nom_le_plus_long:
        print(f"Le nom le plus long est: {nom_le_plus_long}")
    else:
        print("Aucun invité n'a été ajouté.")