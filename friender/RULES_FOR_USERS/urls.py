from django.urls import path
from .views import *

# маршутизация
urlpatterns = [
    path('acquaintance_rules/', acquaintance_rules),
    path('arrangement_places/', arrangement_places),
]