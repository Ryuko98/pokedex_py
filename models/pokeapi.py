import requests

def get_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.json()
    return None

def get_type_name(tipo):
    url = f"https://pokeapi.co/api/v2/type/{tipo}/"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        for name in data['names']:
            if name['language']['name'] == 'es':
                return name['name']
    return None

def get_ability_name(ability):
    url = f"https://pokeapi.co/api/v2/ability/{ability}/"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        for name in data['names']:
            if name['language']['name'] == 'es':
                return name['name']
    return None
