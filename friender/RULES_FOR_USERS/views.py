from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def acquaintance_rules(request):
    return(HttpResponse(f'<h3> Правила сайта знакомств <h3>'))


def arrangement_places(request):
    return (HttpResponse(f'<h3> Заведения для свиданий <h3>'))
