from django.urls import path
from . import views

app_name = 'meteoapp'

urlpatterns = [
    path('', views.tempo_view, name='home'),
    path('tempo/<int:id>/', views.city_view, name="city"),





]