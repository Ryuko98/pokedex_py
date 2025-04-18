import requests

def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'].capitalize(),
            'id': data['id'],
            'height': data['height'],
            'weight': data['weight'],
            'sprites': data['sprites']['front_default'],
            'types': [t['type']['name'] for t in data['types']]
        }
    else:
        return None
