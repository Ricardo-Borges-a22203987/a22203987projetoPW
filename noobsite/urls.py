# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('<str:name>', views.greet, name="greet"),
    path('Sir/<str:name>', views.hello_Sir, name="hello_Sir"),
    path('The_Best/', views.The_Best, name="The_Best")
]