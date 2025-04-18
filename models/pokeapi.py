import requests
type_cache = {}
ability_cache = {}

def get_pokemon(name):
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
        resp = requests.get(url)

        if resp.status_code == 200:
            return resp.json()
        return None
    except requests.exceptions.RequestException:
        return None

def get_type_name(type):
    if type in type_cache:
        return type_cache[type]

    url = f"https://pokeapi.co/api/v2/type/{type}/"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        for name in data['names']:
            if name['language']['name'] == 'es':
                type_cache[type] = name['name']
                return name['name']
    return None

def get_ability_name(ability):
    if ability in ability_cache:
        return ability_cache[ability]

    url = f"https://pokeapi.co/api/v2/ability/{ability}/"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        for name in data['names']:
            if name['language']['name'] == 'es':
                ability_cache[ability] = name['name']
                return name['name']
    return None
