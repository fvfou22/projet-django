from django.db import models


class Club(models.Model): 
    nom_club = models.CharField(max_length=100) 
    classement_club = models.CharField(max_length=100)
    ligue_club = models.CharField(max_length = 100) 
    #coach = models.CharField(max_length = 100, default=None) 

    def __str__(self):
        chaine = f"{self.nom_club} "
        return chaine
    
    def dico(self):
        return {"nom_club" : self.nom_club, "classement_club" : self.classement_club, "ligue_club" : self.ligue_club}#,"coach" : self.coach}



class Foot(models.Model): 
    prenom_joueur = models.CharField(max_length = 100)
    nom_joueur = models.CharField(max_length = 100) 
    club = models.ForeignKey(Club, blank=True, null=True, on_delete=models.CASCADE)
    #poste = models.CharField(max_length=100, default=None)

    def __str__(self):
        chaine = f"{self.prenom_joueur} {self.nom_joueur}"
        return chaine

    def dico(self):
        return {"prenom_joueur" : self.prenom_joueur, "nom_joueur" : self.nom_joueur, "club" : self.club}#"poste" : self.poste }

