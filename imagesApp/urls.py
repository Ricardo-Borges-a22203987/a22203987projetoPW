from django.urls import path
from . import views

app_name = 'imagesApp'

urlpatterns = [
    path('', views.bandas_view, name='home'),

]