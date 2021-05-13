from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request, "index.html")

def start(request):
    return HttpResponse("<h2>Почати тренування</h2>")

def auth(request):
    return HttpResponse("<h2>Авторизація</h2>")

def settings(request):
    return HttpResponse("<h2>Налаштування</h2>")
