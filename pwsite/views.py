from django.shortcuts import render

# Create your views here.
# pwsite/views.py

from django.shortcuts import render

def index_view(request):
    return render(request, "pwsite/index.html")

def Sobre(request):
    return render(request, "pwsite/sobre.html")

def Interesses(request):
    return render(request, "pwsite/interesses.html")