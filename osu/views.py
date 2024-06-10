from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index_view(request):
    return render(request, "osu/index.html")

def prometheus_view(request):
    return render(request, "osu/prometheus.html")

def about_view(request):
    return render(request, "osu/sobre.html")