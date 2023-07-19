from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from random import *

BRACKET_LIST = {1:'Herald-Guardian-Crusader',2:'Archon', 3:'Legend', 4:'Ancient', 5:'Divine-Immortal'}


def game(request):
    return render(request, 'game_1.html')

# Download games data to JSON. Use this link once a week or so ( more often if patch is around )
def get_data(request):
    response = requests.get("https://www.dotabuff.com/heroes/meta?view=played&metric=rating_bracket", headers={'User-agent':'your bot 0.1'})
    if response.status_code != 200:
        HttpResponse("Something went wrong")
    else:
        parsed_page = response.content
        soup = bs(parsed_page, "html.parser")
        sdsd = soup.select(selector="td , .link-type-hero")
        img = soup.select(selector='.image-icon')
        names_and_wr = [a.get_text() for a in sdsd]
        names = [a for a in names_and_wr[2::13]]
        herald_guar_crus = [a for a in names_and_wr[4::13]]
        archon = [a for a in names_and_wr[6::13]]
        legend = [a for a in names_and_wr[8::13]]
        ancient = [a for a in names_and_wr[10::13]]
        divine_immo = [a for a in names_and_wr[12::13]]
        imgs = [image['src'] for image in img]

        sorted_dict = dict(zip(names, zip(herald_guar_crus, archon, legend, ancient, divine_immo, imgs)))
        with open('data.json', 'w') as f:
            json.dump(sorted_dict, f, indent=4)
    return JsonResponse(sorted_dict)


@csrf_exempt
def random_heroes(request):
    try:
        is_ajax = request.headers.get('X-Requested-With') == ('XMLHttpRequest')
        if is_ajax:
            if request.method == 'POST':
                data = json.loads(request.body)
                bracket_ind = data['index']
                for index in BRACKET_LIST.keys():
                    if index == bracket_ind:
                        bracket_id = index
        else:
             bracket_id = bracket_id            
        with open ('data.json', 'r') as f:
                f = json.loads(f.read())
        hero_a = choice(list(f.items()))
        hero_b = choice([hero for hero in list(f.items()) if hero != hero_a])
        _wr_a = float(hero_a[1][bracket_id-1][:-1])
        _wr_b = float(hero_b[1][bracket_id-1][:-1])
        if _wr_a > _wr_b:
            winner = hero_a[0]
        else:
            winner = hero_b[0]
        return JsonResponse([{'out_1':hero_a},{'out_2':hero_b},{'winner':winner}], safe=False)
    except:
        return HttpResponse("Nope")


# TO DO:
# Add bracket image during the game
# Make score look nicer / flashier
# Pretify game-over modal. Maybe make it go horizontally from one side to the other