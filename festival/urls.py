from django.urls import path
from . import views

app_name = 'festivalapp'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('festivais/<int:festival_id>/', views.festival_view, name="festival"),


]