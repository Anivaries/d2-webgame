from django.urls import path
from .views import index, game_1, get_data, random_heroes
# 

urlpatterns = [
    path('', index, name="index"),
    path('get_data/', get_data, name="get_data"),
    path('game/', game_1, name="game"),
    path('random_heroes/', random_heroes, name="random_heroes"),
]
