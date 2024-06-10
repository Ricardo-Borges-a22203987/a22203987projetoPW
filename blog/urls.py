from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/<int:post_id>/', views.post_view, name="post"),

    path('post/novo', views.novo_post_view, name="novo_post"),
    path('comment/<int:post_id>/novo', views.novo_comment_view, name="novo_comment"),
    path('rating/<int:post_id>/novo', views.novo_rating_view, name="novo_rating"),

    path('post/<int:post_id>/apaga', views.apaga_post_view, name="apaga_post"),
    path('comment/<int:comment_id>/apaga', views.apaga_comment_view, name="apaga_comment"),
    path('rating/<int:rating_id>/apaga', views.apaga_rating_view, name="apaga_rating"),

    path('post/<int:post_id>/edita', views.edita_post_view,name="edita_post"),
    path('comment/<int:comment_id>/edita', views.edita_comment_view,name="edita_comment"),
    path('rating/<int:rating_id>/edita', views.edita_rating_view,name="edita_rating"),

    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),


]