"""
Calcul du temps avant le Nouvel An
"""
import datetime

def temps_avant_nouvel_an():
    # Obtenir la date et l'heure actuelles
    maintenant = datetime.datetime.now()
    
    # Définir la date et l'heure du Nouvel An
    nouvel_an = datetime.datetime(maintenant.year + 1, 1, 1, 0, 0, 0)
    
    # Calculer la différence de temps
    temps_restant = nouvel_an - maintenant
    
    # Afficher le résultat
    jours_restants = temps_restant.days
    heures_restantes, reste_secondes = divmod(temps_restant.seconds, 3600)
    minutes_restantes, secondes_restantes = divmod(reste_secondes, 60)
    
    print(f"Temps restant avant le Nouvel An: {jours_restants} jours, {heures_restantes} heures, {minutes_restantes} minutes et {secondes_restantes} secondes.")
    
    
if __name__ == "__main__":
    temps_avant_nouvel_an()