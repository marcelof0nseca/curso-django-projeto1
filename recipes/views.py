from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "recipes/home.html", context={"nome": "Marcelo"})


def contato(request):
    return render(request, "recipes/contato.html")


def sobre(request):
    return HttpResponse("Olá, esta é a página sobre!")
