from django.http import HttpResponse
from django.shortcuts import render

__all__ = (
    'home',
    'about',
)

def home(request):
    name = 'Artem'
    return render(request, 'home.html', {'name': name})

def about(request):
    name = 'About us!'
    return render(request, 'about.html', {'name': name})
