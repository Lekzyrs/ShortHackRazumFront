from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

import requests
def start(request):
    return render(request, 'women/starter.html')


def index(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/')
    data = response.json()
    first_post = data[0]
    context = {
        'userId': first_post['userId'],
        'id': first_post['id'],
    }
    return render(request, 'women/index.html', context)

def categories(request, cat_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{cat_id}')
    data = response.json()
    context = {
        'userId': data['userId'],
        'id': data['id'],
        'title': data['title'],
    }
    return render(request, 'women/cats.html', context)




def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year>=2024:
        uri = reverse('cats', args=('music',))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1><p>id: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def register(request):
    return render(request, 'women/register.html')

def register2(request):
    return render(request, 'women/register2.html')
def blago(request):
    return render(request, 'women/blagodar.html')