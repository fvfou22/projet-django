from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from.forms import FootForm
from.forms import ClubForm
from.models import Foot
from.models import Club
from.import models
from django import forms



def joueur(request):

    submitted = False
    if request.method == "POST":
        form = FootForm(request.POST)
        if form.is_valid():
            foot = form.save()
            return HttpResponseRedirect('/joueur/')
    else:
        form = FootForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "form.html", {'form': form})
def traitement_joueur(request):
    lform = FootForm(request.POST)
    if lform.is_valid():
        foot = lform.save()
        return HttpResponseRedirect("/")
    else:
        return render(request,"form.html",{"form: form"})
def affiche_joueur(request):
    foot = list(models.Foot.objects.all())
    return render(request, "affiche.html", {"foot": foot})
def delete_joueur(request, id):
    foot = models.Foot.objects.get(pk=id)
    foot.delete()
    return HttpResponseRedirect("/player/")
def update_joueur(request, id):
    foot = models.Foot.objects.get(pk=id)
    lform = FootForm(foot.dico())
    return render(request, "update.html", {"form": lform,"id":id})
def traitementupdate_joueur(request, id):
    lform = FootForm(request.POST)
    if lform.is_valid():
        foot = lform.save(commit=False)
        foot.id = id;
        foot.save()
        return HttpResponseRedirect("/player/")
    else:
        return render(request, "update.html", {"form": lform, "id": id})










def club(request):
    submitted = False
    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            club = form.save()
            return HttpResponseRedirect('/club')
    else:
        form = ClubForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "club.html", {'form': form})
def traitement_club(request):
    lform = ClubForm(request.POST)
    if lform.is_valid():
        club = lform.save()
        return HttpResponseRedirect("/")
    else:
        return render(request,"club.html",{"form: form"})
def affiche_club(request):
    club = list(models.Club.objects.all())
    return render(request, "affiche.html", {"club":club})
def delete_club(request, id):
    club = models.Club.objects.get(pk=id)
    club.delete()
    return HttpResponseRedirect("/affiche/")
def update_club(request, id):
    club = models.Club.objects.get(pk=id)
    lform = ClubForm(club.dico())
    return render(request, "update.html", {"form": lform,"id":id})
def traitementupdate_club(request, id):
    lform = ClubForm(request.POST)
    if lform.is_valid():
        club = lform.save(commit=False)
        club.id = id;
        club.save()
        return HttpResponseRedirect("/affiche/")
    else:
        return render(request, "update.html", {"form": lform, "id": id})










def home(request):
    return render(request, "home.html")

 
def player(request):
    foot = list(models.Foot.objects.all())
    return render(request, "player.html", {"foot": foot})
