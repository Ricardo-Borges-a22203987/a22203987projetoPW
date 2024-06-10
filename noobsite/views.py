from django.shortcuts import render

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def greet(request,name):
    return HttpResponse(f"Olá n00b, tambem conhecido como {name.capitalize()}!")

def hello_Sir(request,name):
    return HttpResponse(f"Olá Sir {name.capitalize()}!")

def The_Best(request):
    return HttpResponse("Olá és o melhor dos piores")
