from django.shortcuts import render

def home_view(request):
   return render(request, 'mysite/index.html')

def html5_view(request):
  return render(request, 'mysite/html5-css.html')

def CV_view(request):
  return render(request, 'mysite/CV.html')

def Tech(request):
  return render(request, 'mysite/Tech-Videos.html')
