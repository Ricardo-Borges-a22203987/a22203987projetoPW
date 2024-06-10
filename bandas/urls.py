from django.urls import path
from . import views

app_name = 'bandasapp'

urlpatterns = [
    path('', views.bandas_view, name='bandas'),

    path('banda/<int:banda_id>/', views.banda_view, name="banda"),
    path('banda/novo', views.nova_banda_view, name="nova_banda"),
    path('banda/<int:banda_id>/apaga', views.apaga_banda_view,name="apaga_banda"),
    path('banda/<int:banda_id>/edita', views.edita_banda_view,name="edita_banda"),

    path('album/<int:album_id>/', views.album_view, name="album"),
    path('album/<int:banda_id>/novo-album/', views.novo_album_view,name="novo_album"),
    path('album/<int:album_id>/apaga', views.apaga_album_view,name="apaga_album"),
    path('album/<int:album_id>/edita', views.edita_album_view,name="edita_album"),

    path('musica/<int:musica_id>/', views.musica_view, name="musica"),
    path('musica/<int:album_id>/novo-musica/', views.novo_musica_view,name="novo_musica"),
    path('musica/<int:musica_id>/apaga', views.apaga_musica_view,name="apaga_musica"),
    path('musica/<int:musica_id>/edita', views.edita_musica_view,name="edita_musica"),


    path('generos/', views.generos_musicais_view, name="generos"),
    path('genero/<str:genero>', views.bandas_genero_view, name="genero"),




]