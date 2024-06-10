from django.shortcuts import render
import requests


def tempo_view(request):
    Lisboa_id = 1110600 # id de Lisboa
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{Lisboa_id}.json"
    response = requests.get(url)
    data = response.json()
    url = "https://api.ipma.pt/open-data/distrits-islands.json"
    response = requests.get(url)


    localidades = response.json().get('data', [])
    localidades_lista = [
        {"id": localidade['globalIdLocal'], "nome": localidade['local']}
        for localidade in localidades
    ]


    nome = ""
    for localidade in localidades_lista:
        if localidade['id'] == Lisboa_id:
            nome = localidade['nome']
            break

    for day in data['data']:
        if(day["idWeatherType"] >= 10):
            day["idWeatherType"] = "meteo/w_ic_d_" + str(day["idWeatherType"]) + ".svg"
        else:
            day["idWeatherType"] = "meteo/w_ic_d_0" + str(day["idWeatherType"]) + ".svg"

    context = {
        'city': nome,
        'weather': data['data'],
        'localidades': localidades_lista,
        'id': int(1110600),
    }

    return render(request, "meteo/layout.html", context)


def city_view(request, id):
    global_id = id
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id}.json"
    response = requests.get(url)
    data = response.json()


    url = "https://api.ipma.pt/open-data/distrits-islands.json"


    response = requests.get(url)




    localidades = response.json().get('data', [])  # Acessa a chave 'data' se existir
    localidades_lista = [
        {"id": localidade['globalIdLocal'], "nome": localidade['local']}
        for localidade in localidades
    ]

    nome = ""
    for localidade in localidades_lista:
        if localidade['id'] == id:
            nome = localidade['nome']
            break

    for day in data['data']:
        if(day["idWeatherType"] >= 10):
            day["idWeatherType"] = "meteo/w_ic_d_" + str(day["idWeatherType"]) + ".svg"
        else:
            day["idWeatherType"] = "meteo/w_ic_d_0" + str(day["idWeatherType"]) + ".svg"

    context = {
        'city': nome,
        'weather': data['data'],
        'localidades': localidades_lista,
        'id': int(id),
    }

    return render(request, "meteo/layout.html", context)
