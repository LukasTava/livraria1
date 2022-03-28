from .models import Livro
from .form import LivroForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def home(request):
    data = {}
    data['lista'] = ['t1', 't2', 't3']
    return render(request, 'livros/home.html', data)


def listagem(request):
    data = {}
    data['lista'] = Livro.objects.filter()
    return render(request, 'livros/lista.html', data)


def novo_livro(request):
    data = {}
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_lista')
    data['form'] = form
    return render(request, 'livros/form.html', data)


def atualizar(request, pk):
    data = {}
    livro = Livro.objects.get(pk=pk)
    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect('url_lista')

    data['form'] = form
    data['livro'] = livro
    return render(request, 'livros/form.html', data)


def delete(request, pk):
    livro = Livro.objects.get(pk=pk)
    livro.delete()
    return redirect('url_lista')


class PaginaInicial(TemplateView):
    template_name = 'index.html'


