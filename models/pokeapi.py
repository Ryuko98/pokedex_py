import requests

def get_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.json()
    return None
