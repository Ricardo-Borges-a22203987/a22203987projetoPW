from django.contrib import admin
from .models import Banda, Album, Musica

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero')
    search_fields = ('nome', 'genero')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'banda', 'ano_lancamento')
    search_fields = ('titulo', 'banda__nome')

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'duracao')
    search_fields = ('titulo', 'album__titulo')

admin.site.register(Banda, BandaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)

