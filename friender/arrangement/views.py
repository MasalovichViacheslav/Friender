from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import datetime
from .models import *


# функция представления (вьюшка)
# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = f"<html><body>It is now {now}.</body></html>"
#     return HttpResponse(html)
#
#
# def greeting(request, name):
#     return HttpResponse(f"<h1>Hello {name}</h1>")
#
#
# def year_archive(request, year):
#     return HttpResponse(f"headers: {year}")
#
#
# class Example(View):
#     def get(self,request, *args,**kwargs):
#         return HttpResponse(f"This is class base view")


def main(request):
    return render(request, "main.html")

def allusers(request):
    return render(request, "users.html", {"allusers": Users.objects.all})

# HOSTS = {
#     "Phoebe": ["Buffay", 27, "female", 4.3],
#     "Ross": ["Geller", 29, "male", 4.4],
#     "Chandler": ["Bing", 27, "male", 4.6]
# }
#
# def hosts(request):
#     return render(request, "hosts.html", context={"HOSTS": HOSTS})
#
#
# GUESTS = {
#     "Rachel": ["Green", 25, "female", 4.9],
#     "Monica": ["Geller", 26, "female", 4.6],
#     "Joey": ["Tribbiani", 25, "female", 4.9]
# }
#
# def guests(request):
#     return render(request, "guests.html", context={"GUESTS": GUESTS})


# Establishments = {
#     "CUPRUM": ["Revolyutsionnaya str., 2", "5-15 BYN", 4.8],
#     "Elementum": ["Internacionalnaya str., 20A", "35-65 BYN", 4.9],
#     "Cripta": ["Tolbuhina str., 18/2", "65-95 BYN", 4.9],
#     "Bar StandUp": ["Partizanski av., 12", "15-35 BYN", 4.9],
#     "Gambrinus": ["Svobody sq., 2", "15-35 BYN", 5.0],
#     "Duduk": ["Bogdanovicha str., 7", "15-35 BYN", 5.0]
# }
def establishments(request):
    return render(request, "establishments.html", {"ESTABLISHMENTS": Establishments.objects.all})


# def ratings(request):
#     return render(request, "ratings.html", context={"ELEMENTS": [HOSTS, GUESTS, Establishments]})
