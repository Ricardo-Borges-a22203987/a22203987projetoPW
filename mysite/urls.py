from django.urls import path
from . import views

app_name = 'mainSite'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('html/', views.html5_view, name='html5'),
    path('videos/', views.Tech, name='Tech'),
    path('CV/', views.CV_view, name='CV'),

]