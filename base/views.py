from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup as bs
import requests
import json
from random import *

BRACKET_LIST = ["Herald", "Guardian", "Crusader", "Archon", "Legend", "Ancient", "Divine-Immortal"]

def index(request):
    return render(request, 'index.html')

def game_1(request):
    return render(request, 'game_1.html')
    # print(request.__dict__)
    # sd = random_heroes(request)
    # winner = sd[2]['winner']
    # hero_a = sd[0]['out_1'][0]
    # hero_b = sd[1]['out_2'][0]

    

    # context = {
    #     'hero_a':hero_a,
    #     'hero_b':hero_b
    # }
    # return render(request, 'game_1.html', context)

def get_data(request):
    response = requests.get("https://www.dotabuff.com/heroes/meta?view=played&metric=rating_bracket", headers={'User-agent':'your bot 0.1'})
    if response.status_code != 200:
        HttpResponse("Something went wrong")
    else:
        parsed_page = response.content
        soup = bs(parsed_page, "html.parser")
        sdsd = soup.select(selector="td , .link-type-hero")
        
        names_and_wr = [a.get_text() for a in sdsd]
        names = [a for a in names_and_wr[2::13]]
        herald_guar_crus = [a for a in names_and_wr[4::13]]
        archon = [a for a in names_and_wr[6::13]]
        legend = [a for a in names_and_wr[8::13]]
        ancient = [a for a in names_and_wr[10::13]]
        divine_immo = [a for a in names_and_wr[12::13]]

        sorted_dict = dict(zip(names, zip(herald_guar_crus, archon, legend, ancient, divine_immo)))
        with open('data.json', 'w') as f:
            json.dump(sorted_dict, f, indent=4)
    return JsonResponse(sorted_dict)

def random_heroes(request):

    
    with open ('data.json', 'r') as f:
            f = json.loads(f.read())
    hero_a = choice(list(f.items()))
    hero_b = choice([hero for hero in list(f.items()) if hero != hero_a])
    herald_wr_a = float(hero_a[1][0][:-1])
    herald_wr_b = float(hero_b[1][0][:-1])
    if herald_wr_a > herald_wr_b:
        winner = hero_a[0]
    else:
        winner = hero_b[0]
    chckfun(winner, kwargs=winner)
    # print(winner)
    return JsonResponse([{'out_1':hero_a},{'out_2':hero_b}, {'winner':winner}], safe=False)
    # return [{'out_1':hero_a},{'out_2':hero_b}, {'winner':winner}]

def chckfun(*args, **kwargs):
    winner = args[0]
    test_winner = winner
    print("JA SAM POZVAN")

    # print(winner)
def check_winner(request):
    if request.method == "POST":

        pop = request.POST.get('hero_a_button')
        popa = request.POST.get('hero_b_button')
        # print(popa)
        chckfun(pop, popa)
    sd = random_heroes(request)
    winner = sd[2]['winner']
    hero_a = sd[0]['out_1'][0]
    hero_b = sd[1]['out_2'][0]

    

    context = {
        'hero_a':hero_a,
        'hero_b':hero_b,
        'request.POST':request.POST,
        'request.POST':request.POST,
    }
    return render(request, 'game_1.html', context)




# def get_next_pair():
#     random_heroes()





#     if request.method == "POST":
#         if 'hero_a_button' in request.POST:
#             print(request.POST['hero_a_button'])
#             print("ASDASD")
#         elif 'hero_b_button' in request.POST:
#             print(request.POST['hero_b_button'])
#     return game_1(request)
     

    #TO DO:
# DODAJ SKOR
# STAVI MODAL DA PITA ZA BRACKET NA LOAD PAGE ODMA



# def game_hero(request):

#     with open ('data.json', 'r') as f:
#         f = json.loads(f.read())
#     hero_a = choice(list(f))
#     hero_a_wr_hgc = float(f[hero_a][0][:-1])
#     # Just excluding first picked hero so it doesn't show up twice 
#     hero_b = choice([hero for hero in list(f) if hero != hero_a])
#     hero_b_wr_hgc = float(f[hero_b][0][:-1])
#     if hero_a_wr_hgc > hero_b_wr_hgc:
#         winner = hero_a
#     else:
#         winner = hero_b

#     context = {
#         'hero_a':hero_a,
#         'hero_a_wr_hgc':hero_a_wr_hgc,
#         'hero_b':hero_b,
#         'hero_b_wr_hgc':hero_b_wr_hgc,
#         'winner':winner
#     }
#     return render(request, 'game_1.html', context)


# def show_data(request):
#     with open ('data.json', 'r') as f:
#         f = json.loads(f.read())
#     # hero_a = choice(list(f))
#     # hero_b = choice([hero for hero in list(f) if hero != hero_a])
#     return JsonResponse(f, safe=False)