from django.shortcuts import render

from .models import Banda

def bandas_view(request):
   context = {
      'bandas': Banda.objects.all,
   }
   return render(request, 'imagesApp/index.html', context)