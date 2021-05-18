from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request, "index.html")

def start(request):
    return HttpResponse("start.html")

def auth(request):
    return render(request, "auth.html")

def settings(request):
    return HttpResponse("<h2>Налаштування</h2>")
