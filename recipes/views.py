# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Olá, esta é a página home 1!")


def contato(request):
    return HttpResponse("Olá, esta é a página contato!")


def sobre(request):
    return HttpResponse("Olá, esta é a página sobre!")
