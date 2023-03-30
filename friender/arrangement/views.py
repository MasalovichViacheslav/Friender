from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import datetime


# функция представления (вьюшка)
def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.</body></html>"
    return HttpResponse(html)


def greeting(request, name):
    return HttpResponse(f"<h1>Hello {name}</h1>")


def year_archive(request, year):
    return HttpResponse(f"headers: {year}")


class Example(View):
    def get(self,request, *args,**kwargs):
        return HttpResponse(f"This is class base view")
