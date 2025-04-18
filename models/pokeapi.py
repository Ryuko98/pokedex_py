import requests

def obtener_pokemon(nombre):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre.lower()}'
    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.json()
    return None
