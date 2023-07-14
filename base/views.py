from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup as bs
import requests
import json

BRACKET_LIST = ["Herald", "Guardian", "Crusader", "Archon", "Legend", "Ancient", "Divine-Immortal"]

def index(request):
    return render(request, 'index.html')


def game_1(request):

    return render(request, 'game_1.html')

def get_data(request):
    response = requests.get("https://www.dotabuff.com/heroes/meta?view=played&metric=rating_bracket", headers={'User-agent':'your bot 0.1'})
    if response.status_code is not 200:
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


def show_data(request):
    with open ('data.json', 'r') as f:
        f = json.loads(f.read())
        return JsonResponse(f, safe=False)