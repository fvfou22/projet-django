from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('joueur/',views.joueur, name="Joueur"),
    path('club/',views.club,name="Club"), 
    path('player/',views.player,name="Player"),
    path('',views.home, name="Home"),
    path('affiche/',views.affiche_club, name="Affiche_club"),
    path('affiche/',views.affiche_joueur, name="Affiche_joueur"),    
    path("affiche/<int:id>/",views.affiche_club),
    path("affiche/<int:id>/",views.affiche_joueur),
    path("traitement/", views.traitement_club, name="Traitement_club"),
    path("traitement/", views.traitement_joueur, name="Traitement_joueur"),
    path("/delete/<int:id>",views.delete_club, name="Delete_club"),
    path("delete/<int:id>",views.delete_joueur, name="Delete_joueur"),
    path("update/<int:id>",views.update_joueur, name="Update_joueur"),
    path("update/<int:id>",views.update_club, name="Update_club"),
    path("traitementupdate/<int:id>",views.traitementupdate_joueur, name="Traitementupdate_joueur"),
    path("traitementupdate/<int:id>",views.traitementupdate_club, name="Traitementupdate_club"),
    path('admin/', admin.site.urls),
]
