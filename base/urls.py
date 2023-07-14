from django.urls import path
from .views import index, game_1, get_data, show_data, game_hero, random_heroes

urlpatterns = [
    path('', index, name="index"),
    path('game/', game_hero, name="g1"),
    path('get_data/', get_data, name="get_data"),
    path('show_data/', show_data, name="show_data"),
    # path('/', check_answer, name="button"),
    path('random_heroes/', random_heroes, name="random_heroes"),
]
