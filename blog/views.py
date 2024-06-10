from django.shortcuts import render, redirect
from django.contrib.auth import models,logout,authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import PostForm,CommentForm,RatingForm

from .models import Post,Comment,Rating

def home_view(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)


def post_view(request,post_id):
    context = {
        'post': Post.objects.get(id=post_id),
    }
    return render(request, "blog/post.html", context)


@login_required
def novo_post_view(request):

    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user  # Define o autor como o usuário atual
        post.save()
        return redirect('blogapp:home')

    context = {'form': form}
    return render(request, 'blog/novo_post.html', context)

@login_required
def novo_comment_view(request,post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return redirect('blogapp:home')

    context = {'form': form}
    return render(request, 'blog/novo_comment.html', context)

@login_required
def novo_rating_view(request,post_id):
    post = Post.objects.get(id=post_id)
    form = RatingForm(request.POST, request.FILES)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.author = request.user
        rating.post = post
        rating.save()
        return redirect('blogapp:home')

    context = {'form': form}
    return render(request, 'blog/novo_rating.html', context)

def apaga_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blogapp:home')

def apaga_comment_view(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('blogapp:home')

def apaga_rating_view(request, rating_id):
    rating = Rating.objects.get(id=rating_id)
    rating.delete()
    return redirect('blogapp:home')

def edita_post_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.POST:
        form = PostForm(request.POST or None, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = PostForm(instance=post)  # cria formulário com dados da instância autor

    context = {'form': form, 'post':post}
    return render(request, 'blog/edita_post.html', context)

def edita_comment_view(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.POST:
        form = CommentForm(request.POST or None, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment')
    else:
        form = CommentForm(instance=comment)  # cria formulário com dados da instância autor

    context = {'form': form, 'comment':comment}
    return render(request, 'blog/edita_comment.html', context)

def edita_rating_view(request, rating_id):
    rating = Rating.objects.get(id=rating_id)

    if request.POST:
        form = RatingForm(request.POST or None, request.FILES, instance=rating)
        if form.is_valid():
            form.save()
            return redirect('rating')
    else:
        form = RatingForm(instance=rating)  # cria formulário com dados da instância autor

    context = {'form': form, 'rating':rating}
    return render(request, 'blog/edita_rating.html', context)
















def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('login')

    return render(request, 'blog/registo.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'blog/user.html')
        else:
            render(request, 'blog/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'blog/login.html')


def logout_view(request):
    logout(request)
    return redirect('blogapp:home')