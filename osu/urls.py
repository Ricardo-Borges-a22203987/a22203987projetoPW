# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'osu'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('prometheus/', views.prometheus_view, name='prometheus'),
    path('about/', views.about_view, name='about'),
]