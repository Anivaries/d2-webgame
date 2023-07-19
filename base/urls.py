from django.urls import path
from .views import game, get_data, random_heroes
# 

urlpatterns = [
    path('get_data/', get_data, name="get_data"),
    path('game/', game, name="game"),
    path('random_heroes/', random_heroes, name="random_heroes"),
]
