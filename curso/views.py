from django.shortcuts import render, redirect
from .models import Curso, Disciplina, Projeto,AreaCientifica,Docente
from django.contrib.auth import models,logout,authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CursoForm,DisciplinaForm,ProjetoForm,AreaCientificaForm,DocenteForm


def index_view(request):
    context = {
        'cursos': Curso.objects.all(),
    }
    return render(request, 'curso/index.html', context)

def disciplina_view(request):
    context = {
        'areascientificas': AreaCientifica.objects.all(),
    }
    return render(request, "curso/disciplina.html", context)

def docentes_view(request):
    context = {
        'docentes': Docente.objects.all(),
    }
    return render(request, "curso/docentes.html", context)


def projeto_view(request, projc_id):
    context = {
        'projeto': Projeto.objects.get(id=projc_id),
    }
    return render(request, "curso/projeto.html", context)

@login_required
def novo_curso_view(request):
    form = CursoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursoapp:home')

    context = {'form': form}
    return render(request, 'curso/novo_curso.html', context)

@login_required
def nova_disciplina_view(request, area_id):
    area = AreaCientifica.objects.get(id=area_id)
    form = DisciplinaForm(request.POST or None, request.FILES)
    if form.is_valid():
        disciplina = form.save(commit=False)
        disciplina.area = area
        form.save()
        return redirect('cursoapp:home')

    context = {'form': form}
    return render(request, 'curso/nova_disciplina.html', context)

@login_required
def novo_projeto_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        projeto = form.save(commit=False)
        projeto.disciplina = disciplina
        form.save()
        return redirect('cursoapp:home')

    context = {'form': form}
    return render(request, 'curso/novo_projeto.html', context)

@login_required
def nova_area_cientifica_view(request):
    form = AreaCientificaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursoapp:home')

    context = {'form': form}
    return render(request, 'curso/nova_area_cientifica.html', context)

@login_required
def novo_docente_view(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursoapp:home')  # Redirect to wherever you want
    else:
        form = DocenteForm()
    context = {'form': form}
    return render(request, 'curso/novo_docente.html', context)

@login_required
def apaga_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('cursoapp:home')

@login_required
def apaga_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('cursoapp:home')

@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('cursoapp:home')

@login_required
def apaga_area_view(request, area_id):
    area = AreaCientifica.objects.get(id=area_id)
    area.delete()
    return redirect('cursoapp:home')

@login_required
def apaga_docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    docente.delete()
    return redirect('cursoapp:home')



@login_required
def edita_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)

    if request.POST:
        form = CursoForm(request.POST or None, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursoapp:home')
    else:
        form = CursoForm(instance=curso)

    context = {'form': form, 'curso':curso}
    return render(request, 'curso/edita_curso.html', context)

@login_required
def edita_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)

    if request.POST:
        form = DisciplinaForm(request.POST or None, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('cursoapp:home')
    else:
        form = CursoForm(instance=disciplina)

    context = {'form': form, 'disciplina':disciplina}
    return render(request, 'curso/edita_disciplina.html', context)

@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('cursoapp:home')
    else:
        form = CursoForm(instance=projeto)

    context = {'form': form, 'projeto':projeto}
    return render(request, 'curso/edita_projeto.html', context)

@login_required
def edita_area_view(request, area_id):
    area = AreaCientifica.objects.get(id=area_id)

    if request.POST:
        form = AreaCientificaForm(request.POST or None, request.FILES, instance=area)
        if form.is_valid():
            form.save()
            return redirect('cursoapp:home')
    else:
        form = CursoForm(instance=area)

    context = {'form': form, 'area':area}
    return render(request, 'curso/edita_area.html', context)

@login_required
def edita_docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)

    if request.POST:
        form = DocenteForm(request.POST or None, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('cursoapp:home')
    else:
        form = CursoForm(instance=docente)

    context = {'form': form, 'docente':docente}
    return render(request, 'curso/edita_docente.html', context)