from models.pokeapi import get_pokemon

def get_pokemon_data(name):
    data = get_pokemon(name)
    if not data:
        return None

    return {
        'name': data['name'].capitalize(),
        'id': data['id'],
        'height': data['height'],
        'weight': data['weight'],
        'sprites': data['sprites']['front_default'],
        'types': [types_dict.get(t['type']['name'], t['type']['name'].capitalize()) for t in data['types']],
        'abilities': [abilities_dict.get(a['ability']['name'], a['ability']['name'].capitalize()) for a in data['abilities']]
    }

types_dict = {
    'fire': 'Fuego',
    'water': 'Agua',
    'grass': 'Planta',
    'electric': 'Eléctrico',
    'dragon': 'Dragón',
    'ground': 'Tierra',
    'fighting': 'Lucha',
    'psychic': 'Psíquico',
    'ghost': 'Fantasma',
    'dark': 'Siniestro',
    'fairy': 'Hada',
    'ice': 'Hielo',
    'rock': 'Roca',
    'steel': 'Acero',
    'bug': 'Bicho',
    'normal': 'Normal',
    'poison': 'Veneno',
    'flying': 'Volador'
}

abilities_dict = {
    'overgrow': 'Espesura',
    'blaze': 'Mar llamas',
    'torrent': 'Torrente',
    'shield-dust': 'Polvo escudo',
    'shed-skin': 'Muda',
    'compound-eyes': 'Ojocompuesto',
    'intimidate': 'Intimidación',
    'static': 'Electricidad estática',
    'levitate': 'Levitación',
    'pressure': 'Presión',
    'synchronize': 'Sincronía',
    'chlorophyll': 'Clorofila',
    'cute-charm': 'Gran encanto',
    'run-away': 'Fuga',
    'keen-eye': 'Vista lince',
    'sand-veil': 'Velo arena',
    'rough-skin': 'Piel tosca',
    'flash-fire': 'Absorbe fuego',
    'swift-swim': 'Nado rápido',
    'poison-point': 'Punto tóxico',
    'inner-focus': 'Foco interno',
    'guts': 'Agallas',
    'adaptability': 'Adaptable',
    'technician': 'Técnico',
    'levitate': 'Levitación'
}
