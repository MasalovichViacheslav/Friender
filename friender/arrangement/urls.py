from django.urls import path,re_path
from .views import *

# маршутизация
urlpatterns = [
    # path('now_time/', current_datetime),
    # path('greeting/<str:name>/', greeting),
    # path('class_view/', Example.as_view()),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', year_archive),
    # path('hosts/', hosts, name="hosts"),
    # path('guests/', guests, name="guests"),
    # path('ratings/', ratings, name="ratings"),
    path('main/', main, name="main"),
    path('users/', allusers, name="users"),
    path('establishments/', establishments, name="establishments"),
]
