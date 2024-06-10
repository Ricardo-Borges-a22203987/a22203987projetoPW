app_name = 'pwsite'

# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('Sobre/', views.Sobre, name='Sobre'),
    path('Inter/', views.Interesses, name='Interesses'),
]