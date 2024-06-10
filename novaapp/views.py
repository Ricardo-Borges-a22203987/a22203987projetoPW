from django.shortcuts import render

def prometheus(request):
    return render(request, "pwsite/Prometheus.html")