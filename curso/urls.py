# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'cursoapp'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('disciplinas/', views.disciplina_view, name="disciplinas"),
    path('projecto/<int:projc_id>/', views.projeto_view, name="projeto"),
    path('docentes/', views.docentes_view, name="docentes"),

    path('curso/novo', views.novo_curso_view, name="novo_curso"),
    path('disciplina/<int:area_id>/novo_disciplina', views.nova_disciplina_view, name="novo_disciplina"),
    path('projeto/<int:disciplina_id>/novo_projeto', views.novo_projeto_view, name="novo_projeto"),
    path('area/nova_area_cientifica', views.nova_area_cientifica_view, name="nova_area_cientifica"),
    path('docente/novo_docente', views.novo_docente_view, name="novo_docente"),

    path('curso/<int:curso_id>/apaga', views.apaga_curso_view,name="apaga_curso"),
    path('disciplina/<int:disciplina_id>/apaga', views.apaga_disciplina_view,name="apaga_disciplina"),
    path('projecto/<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),
    path('area/<int:area_id>/apaga', views.apaga_area_view,name="apaga_area"),
    path('docente/<int:docente_id>/apaga', views.apaga_docente_view,name="apaga_docente"),

    path('curso/<int:curso_id>/edita', views.edita_curso_view,name="edita_curso"),
    path('disciplina/<int:disciplina_id>/edita', views.edita_disciplina_view,name="edita_disciplina"),
    path('projecto/<int:projeto_id>/edita', views.edita_projeto_view,name="edita_projeto"),
    path('area/<int:area_id>/edita', views.edita_area_view,name="edita_area"),
    path('docente/<int:docente_id>/edita', views.edita_docente_view,name="edita_docente"),











]