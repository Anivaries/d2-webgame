from django.urls import path
from .views import index, game_1, get_data, show_data

urlpatterns = [
    path('', index, name="index"),
    path('g-one/', game_1, name="g1"),
    path('get_data/', get_data, name="get_data"),
    path('show_data/', show_data, name="show_data")
]
