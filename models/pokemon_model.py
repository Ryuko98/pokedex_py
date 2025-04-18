from models.pokeapi import get_pokemon, get_type_name, get_ability_name

def get_pokemon_data(name):
    data = get_pokemon(name)
    if not data:
        return None

    return {
        'name': data['name'].capitalize(),
        'id': data['id'],
        'height': data['height'] / 10,
        'weight': data['weight'] / 10,
        'sprites': data['sprites']['front_default'],
        'types': [get_type_name(t['type']['name']) for t in data['types']],
        'abilities': [get_ability_name(a['ability']['name']) for a in data['abilities']]
    }
