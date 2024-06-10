from django.shortcuts import render


from .models import Festival, Localizacao

def index_view(request):
   context = {
      'festivais': Festival.objects.all,
      'locais': Localizacao.objects.all,
   }
   return render(request, 'festival/index.html', context)

def festival_view(request, festival_id):
    context = {
        'festival': Festival.objects.get(id=festival_id),

    }
    return render(request, "festival/festival.html", context)