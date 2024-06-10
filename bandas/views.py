from django.shortcuts import render, redirect


from .models import Musica, Banda, Album
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required
from .forms import BandaForm,AlbumForm,MusicaForm

def bandas_view(request):
   context = {
      'bandas': Banda.objects.all,
   }
   return render(request, 'bandas/index.html', context)


def album_view(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id),
    }
    return render(request, "bandas/album.html", context)

def banda_view(request, banda_id):
    context = {
        'banda': Banda.objects.get(id=banda_id),
    }
    return render(request, "bandas/banda.html", context)


def musica_view(request, musica_id):
    context = {
        'musica': Musica.objects.get(id=musica_id),
    }
    return render(request, "bandas/musica.html", context)

def generos_musicais_view(request):

    context = {
        'generos': Banda.objects.values_list('genero', flat=True).distinct()
        }
    return render(request, "bandas/generos_musicais.html", context)

def bandas_genero_view(request,genero):

    context = {
        'genero': genero,
        'bandas': Banda.objects.filter(genero=genero),
    }
    return render(request, "bandas/bandas_genero.html", context)

@login_required
def nova_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandasapp:bandas')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)


@login_required
def novo_album_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)  # Retrieve the Autor object using autor_id
    form = AlbumForm(request.POST or None, request.FILES)

    if form.is_valid():
        album = form.save(commit=False)  # Create a Livro instance without saving to the database yet
        album.banda = banda  # Set the autor attribute of the Livro instance
        album.save()  # Save the Livro instance to the database
        return redirect('bandasapp:bandas')

    context = {'form': form}
    return render(request, 'bandas/novo_album.html', context)

@login_required
def novo_musica_view(request, album_id):
    album = Album.objects.get(id=album_id)  # Retrieve the Autor object using autor_id
    form = MusicaForm(request.POST or None, request.FILES)

    if form.is_valid():
        musica = form.save(commit=False)
        musica.album = album
        musica.save()
        return redirect('bandasapp:bandas')

    context = {'form': form}
    return render(request, 'bandas/novo_musica.html', context)


@login_required
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandasapp:bandas')

@login_required
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandasapp:bandas')

@login_required
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bandasapp:bandas')

@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandasapp:bandas')
    else:
        form = BandaForm(instance=banda)

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/edita_banda.html', context)

@login_required
def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandasapp:bandas')
    else:
        form = AlbumForm(instance=album)

    context = {'form': form, 'album':album}
    return render(request, 'bandas/edita_album.html', context)

@login_required
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandasapp:bandas')
    else:
        form = MusicaForm(instance=musica)

    context = {'form': form, 'musica':musica}
    return render(request, 'bandas/edita_musica.html', context)











