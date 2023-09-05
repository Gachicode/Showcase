from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


# Create your views here.

def about(request):
    return render(request, 'memes/about.html', {'menu': menu, "title": 'О сайте1'})

def kek(request):
    pass

def index(request):
    posts = Memes.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'memes/index.html', context=context)


def login(request):
    return HttpResponse("Авторизация")


def add_page(request):
    return HttpResponse("Добавьте статью")


def contact(request):
    return HttpResponse("Обратная связь")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"Страница не найдена :( {exception}")
