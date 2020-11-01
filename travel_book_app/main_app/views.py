from django.shortcuts import render, get_object_or_404

from .models import Travel, Step, Stopover


def index(request):
    # parametrisation de l'affichage: ici les 3 derniers voyages par ordre croissant de date
    derniers_voyages = Travel.objects.all().order_by("-date_start")[:3]
    context = {"derniers_voyages": derniers_voyages}
    return render(request, "main_app/index.html", context)


def old_travels(request):
    anciens_voyages = Travel.objects.all().order_by("-date_start")[3:]
    context = {"anciens_voyages": anciens_voyages}
    return render(request, "main_app/old_travels.html", context)


def test_detail(request):
    derniers_voyages_detail = Travel.objects.get(title="Eté 2018")
    context = {"derniers_voyages": derniers_voyages_detail}
    return render(request, "main_app/test_detail.html", context)


def villes(request):
    return render(request, "main_app/villes.html")


def nantes(request):
    return render(request, "main_app/nantes.html")


def nice(request):
    return render(request, "main_app/nice.html")


def marseille_cassis(request):
    return render(request, "main_app/marseille_cassis.html")


def lehavre(request):
    return render(request, "main_app/lehavre.html")


def vannes(request):
    return render(request, "main_app/vannes.html")


def brest(request):
    return render(request, "main_app/brest.html")


def orleans(request):
    return render(request, "main_app/orleans.html")


def propos(request):
    return render(request, "main_app/propos.html")