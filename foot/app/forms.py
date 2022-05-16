from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from.models import Foot, Club
from django import forms





class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ('nom_club', 'ligue_club','classement_club',)#'coach',) 
        labels = {
            'nom_club' : _('Nom du Club'),
            'ligue_club' : _('Ligue du Club') ,
            'classement_club' : _('Classement du Club'),
            #'coach' : _('Coach du Club'),           

        }


class FootForm(ModelForm):
    class Meta:
        model = Foot
        fields = ('prenom_joueur', 'nom_joueur', 'club',)#'poste',) 
        labels = {
            'prenom_joueur' : _('Prénom du Joueur'),
            'nom_joueur' : _('Nom du Joueur') ,
            'club' : _('Club du Joueur'),
            #'poste' : _('Poste du Joueur'),

        }
