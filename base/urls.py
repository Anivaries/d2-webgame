from django.urls import path
from .views import index, game_1, get_data,   random_heroes, check_winner
# game_hero, show_data, 

urlpatterns = [
    path('', index, name="index"),
    path('check_winner/', check_winner, name="check_winner"),
    # path('game/', game_hero, name="g1"),
    path('get_data/', get_data, name="get_data"),
    path('game/', game_1, name="game"),
    # path('show_data/', show_data, name="show_data"),
    # path('/', check_answer, name="button"),
    path('random_heroes/', random_heroes, name="random_heroes"),
]
