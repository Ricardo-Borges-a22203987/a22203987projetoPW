from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'pwsite'

urlpatterns = [
    path('prometheus/', views.prometheus, name='prometheus'),
]