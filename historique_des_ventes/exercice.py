"""
Écrire un programme qui :

1. Demande à l'utilisateur de saisir le nom d'un article parmi une liste proposée.
2. Enregistre chaque article sélectionné, ainsi que son prix, dans un fichier texte nommé ventes.txt.
3. Affiche le total des ventes à la fin de la saisie.
4. Permet à l'utilisateur de terminer la saisie en entrant 'stop'.
"""

ARTICLE_PRIX = {
    "tmatem": 1.5,
    "pain": 0.5,
    "lait": 0.8,
    "pomme": 0.3,
    "banane": 0.4,
}

def write_to_file(article, prix):
    with open("ventes.txt", "a") as file:
        file.write(f"{article} - {prix} TND\n")

def choix_article():
    print("Choisissez un article:")
    for article, prix in ARTICLE_PRIX.items():
        print(f"{article} - {prix} TND")
        
    print("Tapez 'stop' pour terminer.")
    
    somme_totale = 0.0
    
    while True:
        article = input("Entrez le nom de l'article: ").strip().lower()
        
        if article == 'stop':
            break
        
        if article in ARTICLE_PRIX:
            prix = ARTICLE_PRIX[article]
            write_to_file(article, prix)
            print(f"Article ajouté: {article} - {prix} TND")
            somme_totale += prix
        else:
            print("Article non reconnu. Veuillez réessayer.")
    
    print("----------------------------")
    print("-" * 30)
    print(f"Total des ventes: {somme_totale} TND")
    write_to_file("Total", somme_totale)
    
if __name__ == "__main__":
    with open("ticket.txt", "w") as f:
        f.truncate(0)
    choix_article()
    print("Les ventes ont été enregistrées dans le fichier ventes.txt.")